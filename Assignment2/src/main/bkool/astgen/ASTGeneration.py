from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *

class ASTGeneration(BKOOLVisitor):

    def visitProgram(self,ctx:BKOOLParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.classDecl()])

    def visitClassDecl(self,ctx:BKOOLParser.ClassDeclContext):
        parent = Id(ctx.ID(1).getText()) if ctx.ID(1) else None
        return ClassDecl(Id(ctx.ID(0).getText()),[self.visit(x) for x in ctx.memberDecl()], parent)

    def visitMemberDecl(self,ctx:BKOOLParser.MemberDeclContext):
        return AttributeDecl(Instance(),VarDecl(Id(ctx.ID().getText()),self.visit(ctx.bkoolType())))

    def visitBkoolType(self,ctx:BKOOLParser.BkoolTypeContext):
        return IntType() if ctx.INTTYPE() else VoidType()
        

    
