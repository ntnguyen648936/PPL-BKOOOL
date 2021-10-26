

from abc import ABC
from typing import Dict, List, Tuple, Type

class Decl:
    pass

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

class UndeclaredMethod(Exception):
    pass

class TypeMismatch(Exception):
    pass
#----------------------------------------------------------------



from typing import Dict, List, Tuple, Type

class MType:
    def __init__(self,partype:List[Type],rettype:Type):
        self.partype = partype
        self.rettype = rettype
    def __str__(self):
        return "Type(["+",".join(str(t) for t in self.partype)+"],"+str(self.rettype)+")"

class Symbol:
    def __init__(self,name:str,mtype:MType,value):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Sym("+self.name+","+str(self.mtype)+","+str(self.value)+")"

class Scope:
    def __init__(self, ctype:Type):
        self.ctype:Type = ctype
        self.outer:Scope = None
        self.env:List[Symbol] = []
    
    def __str__(self):
        return "Scope("+str(self.ctype)+","+str(self.outer)+",["+",".join(str(s) for s in self.env)+"])"

    def get_sympol(self,name:str):
        current = self
        while current:
            for s in current.env:
                if s.name == name:
                    return s
            current = current.outer
        return None

_types = {
    "int": IntType(),
    "float": FloatType(),
}

class StaticCheck(Visitor):

    types = {}   

    def visitProgram(self,ctx:Program,o:object):
        StaticCheck.types = _types

        scope = Scope(Program)
        for x in ctx.decl:
            self.visit(x,(False,scope))

        return [self.visit(x,(True,scope)) for x in ctx.decl]

    def visitClassDecl(self,ctx:ClassDecl,o:Tuple[bool,Scope]):
        #name:str,parent:str,mem:List[Decl]
        depth, outer_scope = o
        if depth:
            scope = Scope(ClassDecl)
            scope.outer = outer_scope

            if ctx.parent:
                parent = outer_scope.get_sympol(ctx.parent)
                if parent is None:
                    raise Exception("Un")
                scope.outer = parent.value #scope

            outer_scope.get_sympol(ctx.name).value = scope

            for mem in ctx.mem:
                self.visit(mem,(False,scope))

            for mem in ctx.mem:
                self.visit(mem,(True,scope))
            
        else:

            if outer_scope.get_sympol(ctx.name):
                raise Exception("Re")
            if ctx.parent and not outer_scope.get_sympol(ctx.parent):
                raise Exception("Un")
            StaticCheck.types["class({ctx.name})"] = ClassType(ctx.name)
            outer_scope.env.append(Symbol(ctx.name,MType([],None),None))


    def visitVarDecl(self,ctx:VarDecl,o:Tuple[bool,Scope]):
        #name:str,typ:Type
        depth, scope = o  
        if scope.get_sympol(ctx.name):
            raise Exception("Re")
        v = None
        if isinstance(ctx.typ,ClassType):
            v = scope.get_sympol(ctx.typ.name).value
        scope.env.append(Symbol(ctx.name,MType([],self.visit(ctx.typ)),v))
        if depth:
            #visit asign
            return

    def visitFuncDecl(self,ctx:FuncDecl,o:Tuple[bool,Scope]):
        #name:str,param:List[VarDecl],returnType:Type,body:Tuple(List[Decl],List[Expr])
        depth, outer_scope = o
        if depth:
            scope = Scope(FuncDecl)
            scope.outer = outer_scope
            scope.env.append(outer_scope.get_sympol(ctx.name))
            for p in ctx.param:
                self.visit(p,(False,scope))

            decs, stmts = ctx.body
            for dec in decs:
                self.visit(dec,(True,scope))

            for stmt in stmts:
                self.visit(stmt,(True,scope))

        else:
            if outer_scope.get_sympol(ctx.name):
                raise Exception("Re")
            outer_scope.env.append(
                Symbol(
                    ctx.name,
                    MType([self.visit(p.typ,None) for p in ctx.param],self.visit(ctx.returnType,None)),
                    ctx))

    def visitIntType(self,ctx:IntType,o:object):
        return StaticCheck.types["int"]

    def visitFloatType(self,ctx:FloatType,o:object):
        return StaticCheck.types["float"]

    def visitClassType(self,ctx:ClassType,o:object):
        return StaticCheck.types[f"class({ctx.name})"]

    def visitIntLit(self,ctx:IntLit,o:object):
        return StaticCheck.types["int"]

    def visitSelf(self,ctx:IntLit,o:Tuple[bool,Scope]):
        _, scope = o
        return scope if scope.ctype is ClassDecl else scope.outer

    def visitId(self,ctx:Id,o:Tuple[bool,Scope]):
        depth,scope = o
        id = scope.get_sympol(ctx.name)
        if id:
            if depth:
                return scope.get_sympol(ctx.name)
            return scope.get_sympol(ctx.name).mtype.rettype
        raise Exception("Un")

    def visitCall(self,ctx:Call,o:Tuple[bool,Scope]):
        depth,scope = o 

        obj_type = self.visit(ctx.exp,(False,scope)) # get type
        obj_scope = None
        if obj_type is ClassType:
            obj_scope = self.visit(ctx.exp,(True,scope)) # get full
        else:
            raise TypeMismatch(ctx)

        func = obj_scope.get_sympol(ctx.name) 
        if func == None or not isinstance(func.value, FuncDecl):
            raise UndeclaredMethod(ctx.name)
        
        if len(ctx.args)!=len(func.mtype.partype):
            raise TypeMismatch(ctx)
        
        for arg,typ in zip(ctx.args,func.mtype.partype):
            arg_typ = self.visit(arg,(False,scope))

            if arg_typ != typ:
                raise TypeMismatch(ctx)
            
        if depth==False:
            return func.mtype.rettype
        return func
