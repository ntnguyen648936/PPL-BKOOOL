

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
        if ctx.op in ['+', '-', '*','/']:
            if leftType is None:
                leftType = int
                o[ctx.e1.name] = int
            if rightType is None:
                rightType = int
                o[ctx.e2.name] = int
                
            if leftType is int and rightType is int:
                return int
                
        elif ctx.op in ['+.','-.','*.','/.']:
            if leftType is None:
                leftType = float
                o[ctx.e1.name] = float
            if rightType is None:
                rightType = float
                o[ctx.e2.name] = float
                
            if leftType is float and rightType is float:
                return float
        elif ctx.op in ['=','>']:
            if leftType is None:
                leftType = int
                o[ctx.e1.name] = int
            if rightType is None:
                rightType = int
                o[ctx.e2.name] = int
                
            if leftType is int and rightType is int:
                return bool
                
        elif ctx.op in ['=.','>.']:
            if leftType is None:
                leftType = float
                o[ctx.e1.name] = float
            if rightType is None:
                rightType = float
                o[ctx.e2.name] = float
                
            if leftType is float and rightType is float:
                return bool
                
        elif ctx.op in ['&&','||','>b','=b']:
            if leftType is None:
                leftType = bool
                o[ctx.e1.name] = bool
            if rightType is None:
                rightType = bool
                o[ctx.e2.name] = bool
                
            if leftType is bool and rightType is bool:
                return bool
 
        raise TypeMismatchInExpression(ctx)
                
    def visitUnOp(self,ctx:UnOp,o):
        ele = ctx.e.accept(self,o)
        if ctx.op in ['-','+']:
            if ele == None:
                o[ctx.e.name] = int
                return int
            elif ele == int:
                return int
                
        elif ctx.op in ['-.','+.']:
            if ele == None:
                o[ctx.e.name] = float
                return float
            if ele == float:
                return float
                
        elif ctx.op == '!':
            if ele == None:
                o[ctx.e.name] = bool
                return bool
            if ele == bool:
                return bool
                
        elif ctx.op == 'i2f':
            if ele == None:
                o[ctx.e.name] = int
                return float
            if ele == int:
                return float
                
        elif ctx.op == 'floor':
            if ele == None:
                o[ctx.e.name] = float
                return int
            if ele == int:
                return int
            
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