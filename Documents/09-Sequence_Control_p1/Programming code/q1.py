class Program: #decl:List[ClassDecl]
    pass
class Decl(ABC): #abstract class
    pass

class ClassDecl:#name:str,parent:str,mem:List[Decl]
    pass

class VarDecl(Decl): #name:str,typ:Type
    pass

class FuncDecl(Decl): #name:str,param:List[VarDecl],returnType:Type,body:Tuple(List[Decl],List[Expr])
    pass

class Type(ABC): #abstract class
    pass

class IntType(Type):
    pass

class FloatType(Type):
    pass

class ClassType(Type):#name:str
    pass

class Expr(ABC): #abstract class
    pass

class Lit(Expr): #abstract class
    pass

class IntLit(Lit): #val:int
    pass

class FloatLit(Lit): #val:float
    pass

class Id(Expr): #name:str
    pass

class Self(Expr):
    pass

class Call(Expr): #exp:Expr,name:str,args:List[Expr]
    pass

class UndeclaredMethod(Exception): #name:str
    pass

class TypeMismatch(Exception):
    pass


# -----------------------------------------------------------------------

from typing import Dict, List, Tuple

class Scope(object):
    def get_ctx_by_name(self,name:str):
        pass

class ProgramScope(Scope):
    def __init__(self,program:Program):
        self.env:Dict[str,ClassDecl] = {}
        self.this = program
    def get_ctx_by_name(self,name:str):
        return self.env[name] if name in self.env else None

class ClassScope(Scope):
    def __init__(self,this:ClassDecl,program:ProgramScope):
        self.env:Dict[str,Decl] = {}
        self.program = program
        self.this = this
    
    def get_ctx_by_name(self,name:str):
        return self.env[name] if name in self.env else \
            (self.program.env[name] if name in self.program.env else None)

class FuncScope(Scope):
    def __init__(self,this:FuncDecl,obj:ClassScope):
        self.obj = obj
        self.this = this
        self.env:Dict[str,Decl] = {}

    def get_ctx_by_name(self, name: str):
        return self.env[name] if name in self.env else \
            (self.obj.env[name] if name in self.obj.env else \
                (self.obj.program.env[name] if name in self.obj.program.env else None))

class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        scope = ProgramScope(ctx)
        
        for classDecl in ctx.decl:
            if classDecl.name in scope.env:
                raise Exception("Redeclare " + classDecl.name)
            scope.env[classDecl.name] = classDecl

        return [self.visit(classDecl,scope) for classDecl in ctx.decl]
    
    def visitClassDecl(self,ctx:ClassDecl,o:ProgramScope):
        scope = ClassScope(ctx,o)
        for dec in ctx.mem:
            if dec.name in scope.env:
                raise Exception("Redeclare " + dec.name)
            scope.env[dec.name] = dec
        
        for dec in ctx.mem:
            self.visit(dec,scope)
        
    def visitVarDecl(self,ctx:VarDecl,o:object):
        return
    
    def visitFuncDecl(self,ctx:FuncDecl,o:ClassScope):
        scope = FuncScope(ctx,o) 
        scope.env[ctx.name] = ctx # assign it-self to this-scope

        params, (decls, exprs) = ctx.param, ctx.body

        is_param = True
        for par in params + decls:
            if par.name in scope.env:
                raise Exception("Redeclare " + par.name)
            scope.env[par.name] = par

        for stmt in ctx.stmts:    
            self.visit(stmt,scope)

        
        
    def visitCall(self,ctx:Call,o:Scope):
        obj = self.visit(ctx.expr,o)
        if isinstance(obj,ClassDecl):
            pass
        elif isinstance(obj, Call):
            pass
        else:
             raise TypeMismatch(ctx)
        
        func = o.get_ctx_by_name(ctx.name)
        if not isinstance(obj,ClassType):
            raise TypeMismatch(ctx)

        for par in func.param:

        
        
    def visitIntType(self,ctx:IntType,o:object):
        return int

    def visitFloatType(self,ctx:FloatType,o:object):
        return float

    def visitClassType(self,ctx:ClassType,o:object):
        return ClassType

    def visitIntLit(self,ctx:IntLit,o:object):
        return int

    def visitSelf(self,ctx:IntLit,o:object):
        return o.this if isinstance(o,ClassScope) else o.obj

    def visitId(self,ctx,o:Scope):
        val = o.get_ctx_by_name(ctx.name)
        if val is None:
            raise Exception("Undeclare: " + ctx.name)
        return val