
"""
 * @author nhphung
 * @extended by: ngthquocminh
"""
from types import FunctionType
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

class MType:
    def __init__(self,partype:List[Type],rettype:Type):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name:str,mtype:MType,kind:Kind,value=None):
        self.name = name
        self.mtype = mtype
        self.kind = kind
        self.value = value

class Scope:
    def __init__(self):
        self.ctx:AST = None
        self.outer:Scope = None
        self.env:List[Symbol] = []
    
    def get_sympol(self,name:str) -> Symbol:
        current = self
        while current:
            for s in current.env:
                if s.name == name:
                    return s
            current = current.outer
        return None

class StaticChecker(BaseVisitor,Utils):

    def __init__(self,ast):
        self.ast = ast

    def visit(self,ast:AST,param):
        return ast.accept(self,param)

    def check(self):
        io_scope = Scope()
        io_scope.ctx = ClassDecl(Id("io"),[])
        io_scope.env = [
            Symbol("readInt",MType([],IntType()), Static()),
            Symbol("writeInt",MType([IntType()],VoidType()), Static()),
            Symbol("writeIntLn",MType([IntType()],VoidType()), Static()),
            Symbol("readFloat",MType([],FloatType()), Static()),
            Symbol("writeFloat",MType([FloatType()],VoidType()), Static()),
            Symbol("writeFloatLn",MType([FloatType()],VoidType()), Static()),
            Symbol("readBool",MType([],BoolType()), Static()),
            Symbol("writeBool",MType([BoolType()],VoidType()), Static()),
            Symbol("writeBoolLn",MType([BoolType()],VoidType()), Static()),
            Symbol("readStr",MType([],StringType()), Static()),
            Symbol("writeStr",MType([StringType()],VoidType()), Static()),
            Symbol("writeStrLn",MType([StringType()],VoidType()), Static())
        ]
        io_class = Symbol("io",MType([],ClassType(Id("io"))),Class(),io_scope)
        return self.visit(self.ast,[io_class])

    def visitProgram(self, ast:Program, buildIn:List[Symbol]):
        scope = Scope()
        scope.env.extend(global_env)
        return [self.visit(x,scope) for x in ast.decl]
        
    def visitVarDecl(self, ast:VarDecl, param):

        return None

    def visitConstDecl(self, ast, param):
        return None

    def visitClassDecl(self, ast:ClassDecl, param):
        return Symbol(ast.classname,MType([],ClassType(Id(ast.classname))),Class(),None)

    def visitStatic(self, ast, param):
        return None

    def visitInstance(self, ast, param):
        return None

    def visitMethodDecl(self, ast:MethodDecl, param):
        return None

    def visitAttributeDecl(self, ast, param):
        return None

    def visitIntType(self, ast, param):
        return None

    def visitFloatType(self, ast, param):
        return None

    def visitBoolType(self, ast, param):
        return None

    def visitStringType(self, ast, param):
        return None

    def visitVoidType(self, ast, param):
        return None

    def visitArrayType(self, ast, param):
        return None

    def visitClassType(self, ast, param):
        return None

    def visitBinaryOp(self, ast, param):
        return None

    def visitUnaryOp(self, ast, param):
        return None

    def visitCallExpr(self, ast, param):
        return None

    def visitNewExpr(self, ast, param):
        return None

    def visitId(self, ast, param):
        return None

    def visitArrayCell(self, ast, param):
        return None

    def visitFieldAccess(self, ast, param):
        return None

    def visitBlock(self, ast, param):
        return None

    def visitIf(self, ast, param):
        return None

    def visitFor(self, ast, param):
        return None

    def visitContinue(self, ast, param):
        return None

    def visitBreak(self, ast, param):
        return None

    def visitReturn(self, ast, param):
        return None

    def visitAssign(self, ast, param):
        return None

    def visitCallStmt(self, ast, param):
        return None

    def visitIntLiteral(self, ast, param):
        return None

    def visitFloatLiteral(self, ast, param):
        return None

    def visitBooleanLiteral(self, ast, param):
        return None

    def visitStringLiteral(self, ast, param):
        return None

    def visitNullLiteral(self, ast, param):
        return None

    def visitSelfLiteral(self, ast, param):
        return None 

    def visitArrayLiteral(self, ast, param):
        return None 


