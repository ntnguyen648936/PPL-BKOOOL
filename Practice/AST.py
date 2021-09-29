# 6
def flatten(lst):

    if not isinstance(lst,list):
        return [lst]
    if len(lst)==0:
        return []
    if len(lst)==1:
        return flatten(lst[0])
    
    return flatten(lst[0]) + flatten(lst[1:])
      
class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):

        return Program(flatten([self.visit(x) for x in ctx.vardecl()]))

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return [VarDecl(_id,self.visit(ctx.mptype())) for _id in self.visit(ctx.ids())]

    def visitMptype(self,ctx:MPParser.MptypeContext):
        if ctx.INTTYPE():
            return IntType()
        if ctx.FLOATTYPE():
            return FloatType()

    def visitIds(self,ctx:MPParser.IdsContext):
        
        return [Id(x.getText()) for x in ctx.ID()] 


# 5
from functools import reduce
class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):

        return self.visit(ctx.exp())

    def visitExp(self,ctx:MPParser.ExpContext):

        return reduce(lambda acc,ele:
            Binary(ele[0].getText(),
            ele[1].accept(self),
            acc),
            zip (ctx.ASSIGN()[::-1], list(ctx.term()[0:-1])[::-1]),
            ctx.term()[-1].accept(self))

    def visitTerm(self,ctx:MPParser.TermContext): 
        if ctx.getChildCount() == 1:
            return self.visit(ctx.factor()[0])
        return Binary(ctx.COMPARE().getText(),self.visit(ctx.factor()[0]),self.visit(ctx.factor()[1]))

    def visitFactor(self,ctx:MPParser.FactorContext):
        return reduce(lambda acc ,ele:
            Binary(ele[0].getText(),
            acc,
            ele[1].accept(self)),
            zip (ctx.ANDOR(), ctx.operand()[1:]),
            ctx.operand(0).accept(self))

    def visitOperand(self,ctx:MPParser.OperandContext):
        if ctx.exp():
            return self.visit(ctx.exp())
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        if ctx.BOOLIT():
            return BooleanLiteral(True if ctx.BOOLIT().getText()=="True" else False)

# 4
class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        
        return Program(self.visit(ctx.vardecls()))

    def visitVardecls(self,ctx:MPParser.VardeclsContext):

        return self.visit(ctx.vardecl()) + (self.visit(ctx.vardecltail()) if ctx.vardecltail() else [])

    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 

        return (self.visit(ctx.vardecl()) if ctx.vardecl() else []) + \
            (self.visit(ctx.vardecltail()) if ctx.vardecltail() else [])

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return [VarDecl(_id,self.visit(ctx.mptype())) for _id in self.visit(ctx.ids())]

    def visitMptype(self,ctx:MPParser.MptypeContext):
        if ctx.INTTYPE():
            return IntType()
        if ctx.FLOATTYPE():
            return FloatType()

    def visitIds(self,ctx:MPParser.IdsContext):
        
        return [Id(ctx.ID().getText())] + (self.visit(ctx.ids()) if ctx.ids() else [])

# 3

class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):

        return self.visit(ctx.exp())

    def visitExp(self,ctx:MPParser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.term())

        return Binary(ctx.ASSIGN().getText(),self.visit(ctx.term()),self.visit(ctx.exp()))

    def visitTerm(self,ctx:MPParser.TermContext): 
        if ctx.getChildCount() == 1:
            return self.visit(ctx.factor()[0])
        return Binary(ctx.COMPARE().getText(),self.visit(ctx.factor()[0]),self.visit(ctx.factor()[1]))

    def visitFactor(self,ctx:MPParser.FactorContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.operand())
        return Binary(ctx.ANDOR().getText(),self.visit(ctx.factor()),self.visit(ctx.operand()))

    def visitOperand(self,ctx:MPParser.OperandContext):
        if ctx.exp():
            return self.visit(ctx.exp())
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        if ctx.BOOLIT():
            return BooleanLiteral(True if ctx.BOOLIT().getText()=="True" else False)

# 2

class TerminalCount(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.vardecls())
    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        _1 = self.visit(ctx.vardecl())
        _2 = self.visit(ctx.vardecltail())
        return 1 + (_1 if _1 >= _2 else _2)
    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        if ctx.getChildCount() == 0:
            return 1
        _1 = self.visit(ctx.vardecl())
        _2 = self.visit(ctx.vardecltail())
        return 1 + (_1 if _1 >= _2 else _2)
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        _1 = self.visit(ctx.mptype())
        _2 = self.visit(ctx.ids())
        return 1 + (_1 if _1 >= _2 else _2)
    def visitMptype(self,ctx:MPParser.MptypeContext):
        return 2
    def visitIds(self,ctx:MPParser.IdsContext):
        if ctx.getChildCount() == 1:
            return 2
        return 1 + self.visit(ctx.ids())

# 1

class TerminalCount(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.vardecls())
    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        if ctx.getChildCount() == 0:
            return 1
        return (self.visit(ctx.vardecl()) if ctx.vardecl() else 0) + (self.visit(ctx.vardecltail()) if ctx.vardecltail() else 0)
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return 1 + self.visit(ctx.mptype()) + self.visit(ctx.ids())
    def visitMptype(self,ctx:MPParser.MptypeContext):
        return 1
    def visitIds(self,ctx:MPParser.IdsContext):
        if ctx.getChildCount() == 1:
            return 1
        return 2 + (self.visit(ctx.ids()) if ctx.ids() else 0)