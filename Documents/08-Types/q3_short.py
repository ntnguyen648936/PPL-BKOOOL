op_rules = {
    '+': (int,int),
    '-': (int,int),
    '*': (int,int),
    '/': (int,int),
    '+.': (float,float),
    '-.': (float,float),
    '*.': (float,float),
    '/.': (float,float),
    '>': (int,bool),
    '=': (int,bool),
    '>.': (float,bool),
    '=.': (float,bool),
    '=b': (bool,bool),
    '>b': (bool,bool),
    '!': (bool,bool),
    '&&': (bool,bool),
    '||': (bool,bool),
    'i2f': (int,float),
    'floor': (float,int),
}

class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        scope = {} #id:type
        for dec in ctx.decl:
            self.visit(dec,scope)
        for stmt in ctx.stmts:    
            self.visit(stmt,scope)
        
    def visitVarDecl(self,ctx:VarDecl,o):
        o[ctx.name] = None
        
    def visitAssign(self,ctx:Assign,o):
        r = self.visit(ctx.rhs, o) # visit RHS first
        l = self.visit(ctx.lhs, o)
        if r is None:
            if type(ctx.rhs)==Id:
                if l is not None:
                    o[ctx.rhs.name] = l
                    return
                raise TypeCannotBeInferred(ctx)
            raise TypeMismatchInStatement(ctx)
            
        if l is None:
            o[ctx.lhs.name] = r
            return
        
        if l != r:
            raise TypeMismatchInStatement(ctx)
                
    def visitBinOp(self,ctx:BinOp,o):
        leftType = ctx.e1.accept(self, o)
        rightType = ctx.e2.accept(self, o)
        if ctx.op in op_rules:
            _accept, _return = op_rules[ctx.op]
            if leftType is None:
                leftType = _accept
                o[ctx.e1.name] = _accept
            if rightType is None:
                rightType = _accept
                o[ctx.e2.name] = _accept
            if leftType is _accept and rightType is _accept:
                return _return
        
        raise TypeMismatchInExpression(ctx)
                
    def visitUnOp(self,ctx:UnOp,o):
        ele = ctx.e.accept(self,o)
        if ctx.op in op_rules:
            _accept, _return = op_rules[ctx.op]

            if ele is None:
                o[ctx.e.name] = _accept
                return _return
                
            if ele is _accept:
                return _return
            
        raise TypeMismatchInExpression(ctx)

    def visitIntLit(self,ctx:IntLit,o):
        return int

    def visitFloatLit(self,ctx,o):
        return float

    def visitBoolLit(self,ctx,o):
        return bool

    def visitId(self,ctx,o):
        if ctx.name in o:
            return o[ctx.name]
        raise UndeclaredIdentifier(ctx.name)