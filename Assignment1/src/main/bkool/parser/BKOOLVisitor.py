# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#decl.
    def visitDecl(self, ctx:BKOOLParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardecl.
    def visitVardecl(self, ctx:BKOOLParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#funcdecl.
    def visitFuncdecl(self, ctx:BKOOLParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#funcDeclParams.
    def visitFuncDeclParams(self, ctx:BKOOLParser.FuncDeclParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#listFuncDeclParams.
    def visitListFuncDeclParams(self, ctx:BKOOLParser.ListFuncDeclParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#listVardecl.
    def visitListVardecl(self, ctx:BKOOLParser.ListVardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#body.
    def visitBody(self, ctx:BKOOLParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#listStmt.
    def visitListStmt(self, ctx:BKOOLParser.ListStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#funcCall.
    def visitFuncCall(self, ctx:BKOOLParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#term.
    def visitTerm(self, ctx:BKOOLParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#factor.
    def visitFactor(self, ctx:BKOOLParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assignment.
    def visitAssignment(self, ctx:BKOOLParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#funcCallStmt.
    def visitFuncCallStmt(self, ctx:BKOOLParser.FuncCallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#retStmt.
    def visitRetStmt(self, ctx:BKOOLParser.RetStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#funcCallParams.
    def visitFuncCallParams(self, ctx:BKOOLParser.FuncCallParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#listFuncCallParams.
    def visitListFuncCallParams(self, ctx:BKOOLParser.ListFuncCallParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visitChildren(ctx)



del BKOOLParser