from os import name
from functools import reduce
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


def str_to_primitive(primType):
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
        _bkoolType = self.visit(ctx.bkoolType())

        kind = Static() if _static else Instance()
        decls = _varDecl

        if _final:
            return [AttributeDecl(
                    kind=kind,
                    decl=ConstDecl(
                        constant=_name,
                        constType=_bkoolType,
                        value=_init,
                    )
                    ) for _name, _init in decls]

        return [AttributeDecl(
            kind=kind,
            decl=VarDecl(
                variable=_name,
                varType=_bkoolType,
                varInit=_init,
            )
        ) for _name, _init in decls]

    def visitMethodDecl(self, ctx: BKOOLParser.MethodDeclContext):

        preMethodDeclContext = ctx.preMethodDecl()
        paramDeclContext = ctx.paramDecl()

        _methodName = ctx.ID().getText()
        _static, _type = self.visit(
            preMethodDeclContext) if preMethodDeclContext else (None, None)

        kind = Static() if _static else Instance()
        name = Id(_methodName if _type else "<init>")
        param = flatten(self.visit(paramDeclContext)
                        ) if paramDeclContext else []
        body = self.visit(ctx.blockStmt())
        returnType = _type

        if _methodName == "main":
            kind = Static()  # main method is static
            param = []  # main method has no parameters
            returnType = VoidType()

        return MethodDecl(
            kind=kind,
            name=name,
            param=param,
            body=body,
            returnType=returnType)

    def visitBlockStmt(self, ctx: BKOOLParser.BlockStmtContext):

        listVarDeclsContext = ctx.varDeclStmt()
        listStatementContext = ctx.statement()

        return Block(
            decl=flatten([self.visit(i) for i in listVarDeclsContext]) 
                if listVarDeclsContext else [],
            stmt=flatten([self.visit(i) for i in listStatementContext]) 
                if listStatementContext else []
        )

    def visitArrayType(self, ctx: BKOOLParser.ArrayTypeContext):
        return ArrayType(
            eleType=str_to_primitive(ctx.PRIMITIVE().getText()),
            size=int(ctx.INT_LIT().getText())
        )

    #
    #
    #

    def visitVarDecl(self, ctx: BKOOLParser.VarDeclContext):
        listVarContext = ctx.listVarDecl()

        _decls = [self.visit(ctx.oneVarDecl())] + \
            (self.visit(listVarContext) if listVarContext else [])

        return _decls

    def visitParamDecl(self, ctx: BKOOLParser.ParamDeclContext):
        listParamDeclContext = ctx.listParamDecl()
        return [self.visit(ctx.oneParamDecl())] + \
            (self.visit(listParamDeclContext) if listParamDeclContext else [])

    def visitListParamDecl(self, ctx: BKOOLParser.ListParamDeclContext):
        listParamDeclContext = ctx.listParamDecl()
        return ([self.visit(ctx.oneParamDecl())] +
                self.visit(listParamDeclContext)) if listParamDeclContext else []

    def visitOneParamDecl(self, ctx: BKOOLParser.OneParamDeclContext):
        listIdContext = ctx.listID()
        listVariable = [Id(ctx.ID().getText())] + \
            (self.visit(listIdContext) if listIdContext else [])

        varType = self.visit(ctx.bkoolType())
        return [VarDecl(variable, varType) for variable in listVariable]

    def visitListID(self, ctx: BKOOLParser.ListIDContext):
        listIdContext = ctx.listID()
        return ([Id(ctx.ID().getText())] +
                self.visit(listIdContext)) if listIdContext else []

    def visitOneVarDecl(self, ctx: BKOOLParser.OneVarDeclContext):
        declAssignmentContext = ctx.declAssignment()
        return Id(ctx.ID().getText()), self.visit(declAssignmentContext) if declAssignmentContext else None

    def visitListVarDecl(self, ctx: BKOOLParser.ListVarDeclContext):
        listVarContext = ctx.listVarDecl()
        return [self.visit(ctx.oneVarDecl())] \
            + (self.visit(listVarContext)) if listVarContext else []

    def visitDeclAssignment(self, ctx: BKOOLParser.DeclAssignmentContext):
        arrayLitContext = ctx.arrayLit()
        if arrayLitContext:
            return self.visit(arrayLitContext)
        return self.visit(ctx.expr())

    def visitPreAttrDecl(self, ctx: BKOOLParser.PreAttrDeclContext):
        return ctx.STATIC() != None, ctx.FINAL() != None

    def visitPreMethodDecl(self, ctx: BKOOLParser.PreMethodDeclContext):
        bkoolTypeContext = ctx.bkoolType()
        _static = ctx.STATIC()
        _type = self.visit(bkoolTypeContext) if bkoolTypeContext else None
        return _static != None, _type

    def visitArrayLit(self, ctx: BKOOLParser.ArrayLitContext):
        listOfPrimLitContext = ctx.listOfPrimLit()
        return ArrayLiteral(
            [self.visit(ctx.primLit())] +
            (self.visit(listOfPrimLitContext) if listOfPrimLitContext else [])
        )

    def visitListOfPrimLit(self, ctx: BKOOLParser.ListOfPrimLitContext):
        listOfPrimLitContext = ctx.listOfPrimLit()
        return ([self.visit(ctx.primLit())] + self.visit(listOfPrimLitContext)) \
            if listOfPrimLitContext else []

    def visitLhs(self, ctx: BKOOLParser.LhsContext):
        indexExprContext = ctx.indexExpr()
        if indexExprContext:
            return [self.visit(indexExprContext)]

        termMemAccessContext = ctx.termMemAccess()
        if termMemAccessContext:
            return FieldAccess(
                obj=self.visit(termMemAccessContext),
                fieldname=Id(ctx.ID().getText())
            )

        return Id(ctx.ID().getText()) 


    def visitMemAccess(self, ctx: BKOOLParser.MemAccessContext):
        termObjCreationContext = ctx.termObjCreation()
        if termObjCreationContext:
            return self.visit(termObjCreationContext)

        listExprContext = ctx.listExpr()
        if listExprContext:
            return CallExpr(
                obj=self.visit(ctx.memAccess()),
                method=Id(ctx.ID().getText()),
                param=self.visit(listExprContext)
            )

        return FieldAccess(
            obj=self.visit(ctx.memAccess()),
            fieldname=Id(ctx.ID().getText()))

    #
    # Statements
    #
    def visitVarDeclStmt(self, ctx: BKOOLParser.VarDeclStmtContext):

        _final = ctx.FINAL()!=None
        _varDecls = self.visit(ctx.varDecl())
        _bkoolType = self.visit(ctx.bkoolType())

        if _final:
            return [ConstDecl(
                        constant=_name,
                        constType=_bkoolType,
                        value=_init,
                    ) for _name, _init in _varDecls]

        return [VarDecl(
                variable=_name,
                varType=_bkoolType,
                varInit=_init,
            ) for _name, _init in _varDecls]

    def visitAssignStmt(self, ctx: BKOOLParser.AssignStmtContext):
        return Assign(
            lhs=self.visit(ctx.lhs()),
            exp=self.visit(ctx.expr())
        )

    def visitIfStmt(self, ctx: BKOOLParser.IfStmtContext):
        statementContext = ctx.statement()
        return If(
            expr=self.visit(ctx.expr()),
            thenStmt=self.visit(statementContext[0]),
            elseStmt=self.visit(statementContext[1]) 
                if len(statementContext) == 2 else None
        )

    def visitForStmt(self, ctx: BKOOLParser.ForStmtContext):
        exprContext = ctx.expr()
        return For(
            id=Id(ctx.ID().getText()),
            expr1=self.visit(exprContext[0]),
            expr2=self.visit(exprContext[1]),
            up=ctx.TO()!=None,
            loop=self.visit(ctx.statement())
        )

    def visitFuncCallStmt(self, ctx: BKOOLParser.FuncCallStmtContext):
        return CallStmt(
            obj=self.visit(ctx.memAccess()),
            method=Id(ctx.ID().getText()),
            param=self.visit(ctx.listExpr())
        )

    def visitReturnStmt(self, ctx: BKOOLParser.ReturnStmtContext):
        return Return(self.visit(ctx.expr()))

    def visitBreakStmt(self, ctx: BKOOLParser.BreakStmtContext):
        return Break()

    def visitContinueStmt(self, ctx: BKOOLParser.ContinueStmtContext):
        return Continue()    

    #
    # Expressions
    #
    def visitExpr(self, ctx: BKOOLParser.ExprContext):
        term0Context = ctx.term0()
        if len(term0Context) == 1:
            return self.visit(term0Context[0])
        return BinaryOp(
            op=ctx.compOp().getText(),
            left=self.visit(term0Context[0]),
            right=self.visit(term0Context[1])
        )

    def visitTerm0(self, ctx: BKOOLParser.Term0Context):
        term1Context = ctx.term1()
        if len(term1Context) == 1:
            return self.visit(term1Context[0])

        return BinaryOp(
            op=ctx.qualsOp().getText(),
            left=self.visit(term1Context[0]),
            right=self.visit(term1Context[1])
        )

    def visitTerm1(self, ctx: BKOOLParser.Term1Context):
        return reduce(
            lambda term, ele: BinaryOp(
                ele[1].getText(),
                term,
                ele[0].accept(self)
            ),
            zip(ctx.term2()[1:], ctx.andorOp()),
            ctx.term2()[0].accept(self)
        )

    def visitTerm2(self, ctx: BKOOLParser.Term2Context):
        return reduce(
            lambda term, ele: BinaryOp(
                ele[1].getText(),
                term,
                ele[0].accept(self)
            ),
            zip(list(ctx.term3()[1:]), ctx.addOp()),
            ctx.term3()[0].accept(self)
        )

    def visitTerm3(self, ctx: BKOOLParser.Term3Context):
        return reduce(
            lambda term, ele: BinaryOp(
                ele[1].getText(),
                term,
                ele[0].accept(self)
            ),
            zip(ctx.term4()[1:], ctx.mulsOp()),
            ctx.term4()[0].accept(self)
        )

    def visitTerm4(self, ctx: BKOOLParser.Term4Context):
        return reduce(
            lambda term, ele: BinaryOp(
                ele[1].getText(),
                term,
                ele[0].accept(self)
            ),
            zip(ctx.term5()[1:], ctx.CONCAT()),
            ctx.term5()[0].accept(self)
        )

    def visitTerm5(self, ctx: BKOOLParser.Term5Context):
        term6Context = ctx.term6()
        if term6Context:
            return self.visit(term6Context)

        return UnaryOp(ctx.NOT().getText(), self.visit(ctx.term5()))

    def visitTerm6(self, ctx: BKOOLParser.Term6Context):
        termIndexExprContext = ctx.termIndexExpr()
        if termIndexExprContext:
            return self.visit(termIndexExprContext)

        return UnaryOp(ctx.signOp().getText(), self.visit(ctx.term6()))

    def visitTermIndexExpr(self, ctx: BKOOLParser.TermIndexExprContext):
        termMemAccessContext = ctx.termMemAccess()
        if termMemAccessContext:
            return self.visit(termMemAccessContext)

        return self.visit(ctx.indexExpr())

    def visitIndexExpr(self, ctx: BKOOLParser.IndexExprContext):
        return ArrayCell(self.visit(ctx.termMemAccess()), self.visit(ctx.expr()))

    def visitTermMemAccess(self, ctx: BKOOLParser.TermMemAccessContext):
        termObjCreationContext = ctx.termObjCreation()
        if termObjCreationContext:
            return self.visit(termObjCreationContext)

        listExprContext = ctx.listExpr()
        if listExprContext:
            return CallExpr(
                obj=self.visit(ctx.termMemAccess()),
                method=Id(ctx.ID().getText()),
                param=self.visit(listExprContext)
            )

        return FieldAccess(
            obj=self.visit(ctx.termMemAccess()),
            fieldname=Id(ctx.ID().getText()))

    def visitTermObjCreation(self, ctx: BKOOLParser.TermObjCreationContext):
        operandsContext = ctx.operands()
        if operandsContext:
            return self.visit(operandsContext)

        return NewExpr(
            classname=Id(ctx.ID().getText()),
            param=self.visit(ctx.listExpr())
        )

    def visitFuncCallExpr(self, ctx: BKOOLParser.FuncCallExprContext):
        return CallExpr(
            obj=self.visit(ctx.termMemAccess()),
            method=Id(ctx.ID().getText()),
            param=self.visit(ctx.listExpr()) if ctx.listExpr() else []
        )

    def visitListExpr(self, ctx: BKOOLParser.ListExprContext):
        return ([self.visit(ctx.expr())] + \
            self.visit(ctx.nextExpr())) if ctx.nextExpr() else []

    def visitNextExpr(self, ctx: BKOOLParser.NextExprContext):
        return ([self.visit(ctx.expr())] + \
            self.visit(ctx.nextExpr())) if ctx.nextExpr() else []

    #
    # 
    #
    def visitOperands(self, ctx: BKOOLParser.OperandsContext):
        if ctx.expr():
            return self.visit(ctx.expr())
        if ctx.primLit():
            return self.visit(ctx.primLit())
        if ctx.NIL():
            return NullLiteral()
        if ctx.THIS():
            return SelfLiteral()
        if ctx.ID():
            return Id(ctx.ID().getText())

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

    def visitPrimLit(self, ctx: BKOOLParser.PrimLitContext):

        intLitContext = ctx.INT_LIT()
        if intLitContext:
            return IntLiteral(int(intLitContext.getText()))

        floatLitContext = ctx.FLOAT_LIT()
        if floatLitContext:
            return FloatLiteral(float(floatLitContext.getText()))

        boolLitContext = ctx.BOOL_LIT()
        if boolLitContext:
            return BooleanLiteral(boolLitContext.getText() == "true")

        strLitContext = ctx.STRING_LIT()
        if strLitContext:
            return StringLiteral(strLitContext.getText())

    def visitBkoolType(self, ctx: BKOOLParser.BkoolTypeContext):

        primitive = ctx.PRIMITIVE()
        if primitive:
            return str_to_primitive(primitive.getText())

        id = ctx.ID()
        if id:
            return ClassType(Id(id.getText()))

        return self.visit(ctx.arrayType())
