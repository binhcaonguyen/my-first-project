# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#decl.
    def visitDecl(self, ctx:MPParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#varDecl.
    def visitVarDecl(self, ctx:MPParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#varTypeDeclList.
    def visitVarTypeDeclList(self, ctx:MPParser.VarTypeDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#varTypeDecl.
    def visitVarTypeDecl(self, ctx:MPParser.VarTypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#idList.
    def visitIdList(self, ctx:MPParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#dataType.
    def visitDataType(self, ctx:MPParser.DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#primType.
    def visitPrimType(self, ctx:MPParser.PrimTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#arrayType.
    def visitArrayType(self, ctx:MPParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#upperBound.
    def visitUpperBound(self, ctx:MPParser.UpperBoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#lowerBound.
    def visitLowerBound(self, ctx:MPParser.LowerBoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcDecl.
    def visitFuncDecl(self, ctx:MPParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#procDecl.
    def visitProcDecl(self, ctx:MPParser.ProcDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compoundStmt.
    def visitCompoundStmt(self, ctx:MPParser.CompoundStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr.
    def visitExpr(self, ctx:MPParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr1.
    def visitExpr1(self, ctx:MPParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr2.
    def visitExpr2(self, ctx:MPParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr3.
    def visitExpr3(self, ctx:MPParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr4.
    def visitExpr4(self, ctx:MPParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr5.
    def visitExpr5(self, ctx:MPParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#stmtsList.
    def visitStmtsList(self, ctx:MPParser.StmtsListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#stmts.
    def visitStmts(self, ctx:MPParser.StmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#bodyIter.
    def visitBodyIter(self, ctx:MPParser.BodyIterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignStmt.
    def visitAssignStmt(self, ctx:MPParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignOperand.
    def visitAssignOperand(self, ctx:MPParser.AssignOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ifStmt.
    def visitIfStmt(self, ctx:MPParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#matchIfStmt.
    def visitMatchIfStmt(self, ctx:MPParser.MatchIfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#unMatchIfStmt.
    def visitUnMatchIfStmt(self, ctx:MPParser.UnMatchIfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#whileStmt.
    def visitWhileStmt(self, ctx:MPParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#forStmt.
    def visitForStmt(self, ctx:MPParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#forCondition.
    def visitForCondition(self, ctx:MPParser.ForConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#breakStmt.
    def visitBreakStmt(self, ctx:MPParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#continueStmt.
    def visitContinueStmt(self, ctx:MPParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#returnStmt.
    def visitReturnStmt(self, ctx:MPParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#withStmt.
    def visitWithStmt(self, ctx:MPParser.WithStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#withVarDecl.
    def visitWithVarDecl(self, ctx:MPParser.WithVarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#callStmt.
    def visitCallStmt(self, ctx:MPParser.CallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#indexExpr.
    def visitIndexExpr(self, ctx:MPParser.IndexExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#invoExpr.
    def visitInvoExpr(self, ctx:MPParser.InvoExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#callExpr.
    def visitCallExpr(self, ctx:MPParser.CallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exprList.
    def visitExprList(self, ctx:MPParser.ExprListContext):
        return self.visitChildren(ctx)



del MPParser