from os import name
from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *


def flatten(lst):
    if not isinstance(lst, list):
        return [lst]

    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return flatten(lst[0])

    head, tail = lst[0], lst[1:]
    return flatten(head) + flatten(tail)


class ASTGeneration(BKOOLVisitor):

    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.classDecl()])

    def visitClassDecl(self, ctx: BKOOLParser.ClassDeclContext):
        parent = Id(ctx.ID(1).getText()) if ctx.ID(1) else None
        return ClassDecl(
            classname=Id(ctx.ID(0).getText()),
            memlist=flatten([self.visit(x) for x in ctx.memberDecl()]),
            parentname=parent
        )

    def visitMemberDecl(self, ctx: BKOOLParser.MemberDeclContext):
        methodDeclContext = ctx.methodDecl()
        if methodDeclContext:
            return self.visit(methodDeclContext)

        return self.visit(ctx.attrDecl())

    def visitAttrDecl(self, ctx: BKOOLParser.AttrDeclContext):

        preAttrDeclContext = ctx.preAttrDecl()
        _static, _final = self.visit(
            preAttrDeclContext) if preAttrDeclContext else (None, None)
        _varDecl = self.visit(ctx.varDecl())
        kind = Static() if _static else Instance()
        decls = _varDecl
        return [AttributeDecl(kind, decl) for decl in decls]

    def visitMethodDecl(self, ctx: BKOOLParser.MethodDeclContext):

        preMethodDeclContext = ctx.preMethodDecl()
        paramDeclContext = ctx.paramDecl()

        _static, _type = self.visit(
            preMethodDeclContext) if preMethodDeclContext else (None, None)

        kind = Static() if _static else Instance()
        name = Id(ctx.ID().getText())
        param = flatten(self.visit(paramDeclContext)
                        ) if paramDeclContext else []
        body = self.visit(ctx.blockStmt())
        returnType = _type
        return MethodDecl(kind, name, param, body, returnType)

    def visitVarDecl(self, ctx: BKOOLParser.VarDeclContext):
        listVarContext = ctx.listVarDecl()

        _bkoolType = self.visit(ctx.bkoolType())
        _decls = [self.visit(ctx.oneVarDecl())] + \
            (self.visit(listVarContext) if listVarContext else [])

        return [VarDecl(
            variable=_name,
            varType=_bkoolType,
            varInit=_init
        ) for _name, _init in _decls]

    #
    #
    #

    def visitParamDecl(self, ctx: BKOOLParser.ParamDeclContext):
        listParamDeclContext = ctx.listParamDecl()
        return [self.visit(ctx.oneParamDecl())] + \
            (self.visit(listParamDeclContext) if listParamDeclContext else [])

    def visitListParamDecl(self, ctx: BKOOLParser.ListParamDeclContext):
        oneVarContext = ctx.oneParamDecl()
        if oneVarContext == None:
            return []

        listVarContext = ctx.listParamDecl()
        return [self.visit(oneVarContext)] \
            + (self.visit(listVarContext) if listVarContext else [])

    def visitOneParamDecl(self, ctx: BKOOLParser.OneParamDeclContext):
        listIdContext = ctx.listID()
        listVariable = [Id(ctx.ID().getText())] + \
            (self.visit(listIdContext) if listIdContext else [])

        varType = self.visit(ctx.bkoolType())
        return [VarDecl(variable, varType) for variable in listVariable]

    def visitListID(self, ctx: BKOOLParser.ListIDContext):
        IdContext = ctx.ID()
        if IdContext == None:
            return []

        listIdContext = ctx.listID()
        return [Id(IdContext.getText())] + (self.visit(listIdContext) if listIdContext else [])

    def visitStatement(self, ctx: BKOOLParser.StatementContext):
        blockStmtContext = ctx.blockStmt()
        if blockStmtContext:
            return self.visit(blockStmtContext)

        ifStmtContext = ctx.ifStmt()
        if ifStmtContext:
            return self.visit(ifStmtContext)

        forStmtContext = ctx.forStmt()
        if forStmtContext:
            return self.visit(forStmtContext)

        funcCallStmtContext = ctx.funcCallStmt()
        if funcCallStmtContext:
            return self.visit(funcCallStmtContext)

        assignStmtContext = ctx.assignStmt()
        if assignStmtContext:
            return self.visit(assignStmtContext)

        breakStmtContext = ctx.breakStmt()
        if breakStmtContext:
            return self.visit(breakStmtContext)

        continueStmtContext = ctx.continueStmt()
        if continueStmtContext:
            return self.visit(continueStmtContext)

        returnStmtContext = ctx.returnStmt()
        if returnStmtContext:
            return self.visit(returnStmtContext)

    def visitBlockStmt(self, ctx: BKOOLParser.BlockStmtContext):

        listVarDeclsContext = ctx.varDeclStmt()
        listStatementContext = ctx.statement()

        return Block(
            decl=[self.visit(
                i) for i in listVarDeclsContext] if listVarDeclsContext else [],
            stmt=[self.visit(
                i) for i in listStatementContext] if listStatementContext else []
        )

    def visitOneVarDecl(self, ctx: BKOOLParser.OneVarDeclContext):
        declAssignmentContext = ctx.declAssignment()
        return Id(ctx.ID().getText()), self.visit(ctx.declAssignment()) if declAssignmentContext else None

    def visitListVarDecl(self, ctx: BKOOLParser.ListVarDeclContext):
        oneVarContext = ctx.oneVarDecl()
        if oneVarContext == None:
            return []

        listVarContext = ctx.listVarDecl()
        return [self.visit(oneVarContext)] \
            + (self.visit(listVarContext) if listVarContext else [])

    def visitDeclAssignment(self, ctx: BKOOLParser.DeclAssignmentContext):
        arrayLitContext = ctx.arrayLit()
        if arrayLitContext:
            return self.visit(arrayLitContext)

        return self.visit(ctx.expr())

    def visitPreAttrDecl(self, ctx: BKOOLParser.PreAttrDeclContext):
        return ctx.STATIC(), ctx.FINAL()

    def visitPreMethodDecl(self, ctx: BKOOLParser.PreMethodDeclContext):
        bkoolTypeContext = ctx.bkoolType()
        _static = ctx.STATIC()
        _type = self.visit(bkoolTypeContext) if bkoolTypeContext else None
        return _static != None, _type

    def visitPrimLit(self, ctx: BKOOLParser.PrimLitContext):

        intLitContext = ctx.INT_LIT()
        if intLitContext:
            return IntLiteral(int(self.visit(intLitContext)))

        floatLitContext = ctx.FLOAT_LIT()
        if floatLitContext:
            return FloatLiteral(float(self.visit(floatLitContext)))

        boolLitContext = ctx.BOOL_LIT()
        if boolLitContext:
            return BooleanLiteral(self.visit(boolLitContext) == "true")

        strLitContext = ctx.STRING_LIT()
        if strLitContext:
            return StringLiteral(self.visit(strLitContext))

    def visitBkoolType(self, ctx: BKOOLParser.BkoolTypeContext):

        primType = str(ctx.PRIMITIVE())
        if primType == "int":
            return IntType()
        if primType == 'float':
            return FloatType()
        if primType == 'boolean':
            return BoolType()
        if primType == 'string':
            return StringType()
        if primType == 'void':
            return VoidType()

        id = ctx.ID()
        if id:
            return Id(ctx.ID())

        return self.visit(ctx.arrayType())
