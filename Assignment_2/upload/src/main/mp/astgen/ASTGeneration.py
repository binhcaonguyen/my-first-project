from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

class ASTGeneration(MPVisitor):
    #program  : decl+ EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        list_decl = [self.visit(x) for x in ctx.decl()]
        return Program([i for j in list_decl for i in j])

    #decl: varDecl | funcDecl | procDecl;
    def visitDecl(self, ctx:MPParser.DeclContext):
        if ctx.varDecl():
            return self.visit(ctx.varDecl())
        elif ctx.funcDecl():
            return self.visit(ctx.funcDecl())
        else:
            return self.visit(ctx.procDecl())

    #varDecl: VAR varTypeDeclList SEMI;
    def visitVarDecl(self, ctx:MPParser.VarDeclContext):
        return self.visit(ctx.varTypeDeclList())

    #varTypeDeclList: varTypeDecl (SEMI varTypeDecl)*;
    def visitVarTypeDeclList(self, ctx:MPParser.VarTypeDeclListContext):
        list_varTypeDecl = [self.visit(x) for x in ctx.varTypeDecl()]
        return [i for j in list_varTypeDecl for i in j]

    #varTypeDecl:  idList COLON dataType;
    def visitVarTypeDecl(self, ctx:MPParser.VarTypeDeclContext):
        list_id = self.visit(ctx.idList())
        return [VarDecl(id, self.visit(ctx.dataType())) for id in list_id]

    #idList: IDENTIFIER (COMMA IDENTIFIER)*;
    def visitIdList(self, ctx:MPParser.IdListContext):
        return [Id(x.getText()) for x in ctx.IDENTIFIER()]

    #dataType: primType | arrayType ;
    def visitDataType(self, ctx:MPParser.DataTypeContext):
        if ctx.primType():
            return self.visit(ctx.primType())
        else:
            return self.visit(ctx.arrayType())
        
    #primType: BOOLEAN | INTEGER | REAL | STRING;
    def visitPrimType(self, ctx:MPParser.PrimTypeContext):
        if ctx.INTEGER():
            return IntType()
        elif ctx.REAL():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        else:
            return StringType()

    #arrayType: ARRAY LQ upperBound DOUBLE_DOT lowerBound RQ OF primType;
    def visitArrayType(self, ctx:MPParser.ArrayTypeContext):
        id1 = self.visit(ctx.upperBound())
        id2 = self.visit(ctx.lowerBound())
        return ArrayType(IntLiteral(id1),IntLiteral(id2),self.visit(ctx.primType()))
    
    #upperBound: SUBOP? INTLIT;
    def visitUpperBound(self, ctx:MPParser.UpperBoundContext):
        id = int(ctx.INTLIT().getText())
        if ctx.SUBOP() and ctx.SUBOP().getText() == '-':
            id = -id
        return id;
    #lowerBound: SUBOP? INTLIT;
    def visitLowerBound(self, ctx:MPParser.LowerBoundContext):
        id = int(ctx.INTLIT().getText())
        if ctx.SUBOP() and ctx.SUBOP().getText() == '-':
            id = -id
        return id;

    #funcDecl: FUNCTION IDENTIFIER LB varTypeDeclList? RB COLON dataType SEMI (varDecl)? compoundStmt;
    def visitFuncDecl(self, ctx:MPParser.FuncDeclContext):
        param = self.visit(ctx.varTypeDeclList()) if ctx.varTypeDeclList() else []
        local = self.visit(ctx.varDecl()) if ctx.varDecl() else []
        cpstmt = self.visit(ctx.compoundStmt())
        return [FuncDecl(Id(ctx.IDENTIFIER().getText()),
                        param,
                        local,
                        cpstmt,
                        self.visit(ctx.dataType()))]

    #procDecl: PROCEDURE IDENTIFIER LB varTypeDeclList? RB SEMI (varDecl)? compoundStmt;
    def visitProcDecl(self, ctx:MPParser.ProcDeclContext):
        param = self.visit(ctx.varTypeDeclList()) if ctx.varTypeDeclList() else []
        local = self.visit(ctx.varDecl()) if ctx.varDecl() else []
        cpstmt = self.visit(ctx.compoundStmt())
        return [FuncDecl(Id(ctx.IDENTIFIER().getText()),
                        param,
                        local,
                        cpstmt)]

    #compoundStmt: BEGIN (stmtsList)? END;
    def visitCompoundStmt(self, ctx:MPParser.CompoundStmtContext):
        if ctx.stmtsList():
            return self.visit(ctx.stmtsList())
        return []

    #expr: expr (AND THEN| OR ELSE) expr1 | expr1;
    def visitExpr(self, ctx:MPParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1())
        else:
            if ctx.AND() and ctx.THEN():
                op = "andthen"
            else:
                op = "orelse"
            return BinaryOp(op, self.visit(ctx.expr()), self.visit(ctx.expr1()))

    #expr1: expr2 (EQUAL|NOT_EQUAL|GREATER|LESS|GREATER_OR_EQUAL|LESS_OR_EQUAL) expr2 | expr2;
    def visitExpr1(self, ctx:MPParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2(0))
        else:
            if ctx.EQUAL():
                op = ctx.EQUAL().getText()
            elif ctx.NOT_EQUAL():
                op = ctx.NOT_EQUAL().getText()
            elif ctx.GREATER():
                op = ctx.GREATER().getText()
            elif ctx.LESS():
                op = ctx.LESS().getText()
            elif ctx.GREATER_OR_EQUAL():
                op = ctx.GREATER_OR_EQUAL().getText()
            else:
                op = ctx.LESS_OR_EQUAL().getText()
            return BinaryOp(op, self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))

    #expr2: expr2 (ADDOP|SUBOP|OR) expr3 | expr3;
    def visitExpr2(self, ctx:MPParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        else:
            if ctx.ADDOP():
                op = ctx.ADDOP().getText()
            elif ctx.SUBOP():
                op = ctx.SUBOP().getText()
            else:
                op = ctx.OR().getText()
            return BinaryOp(op, self.visit(ctx.expr2()), self.visit(ctx.expr3()))

    #expr3: expr3 (DIVOP|MULOP|DIV|MOD|AND) expr4 |expr4;
    def visitExpr3(self, ctx:MPParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        else:
            if ctx.DIVOP():
                op = ctx.DIVOP().getText()
            elif ctx.MULOP():
                op = ctx.MULOP().getText()
            elif ctx.DIV():
                op = ctx.DIV().getText()
            elif ctx.MOD():
                op = ctx.MOD().getText()
            else:
                op = ctx.AND().getText()
            return BinaryOp(op, self.visit(ctx.expr3()), self.visit(ctx.expr4()))

    #expr4: (NOT|ADDOP|SUBOP) expr4 | expr5;
    def visitExpr4(self, ctx:MPParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        else:
            if ctx.NOT():
                op = ctx.NOT().getText()
            elif ctx.ADDOP():
                op = ctx.ADDOP().getText()
            else:
                op = ctx.SUBOP().getText()
            return UnaryOp(op, self.visit(ctx.expr4()))

    #expr5: LB expr RB | (INTLIT|FLOATLIT|IDENTIFIER|indexExpr|BOOLLIT|callExpr|STRINGLIT);
    def visitExpr5(self, ctx:MPParser.Expr5Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expr())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLiteral(ctx.BOOLLIT().getText())
        elif ctx.STRINGLIT():
            return StringLiteral(str(ctx.STRINGLIT().getText()))
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.callExpr():
            return self.visit(ctx.callExpr())
        elif ctx.indexExpr():
            return self.visit(ctx.indexExpr())

    #stmtsList: stmts+;
    def visitStmtsList(self, ctx:MPParser.StmtsListContext):
        list_stmts = [self.visit(x) for x in ctx.stmts()]
        return [i for j in list_stmts for i in j]

    #stmts: assignStmt|callStmt|returnStmt|whileStmt|withStmt|forStmt|breakStmt|continueStmt|ifStmt;
    def visitStmts(self, ctx:MPParser.StmtsContext):
        if ctx.assignStmt():
            return self.visit(ctx.assignStmt())
        elif ctx.whileStmt():
            return [self.visit(ctx.whileStmt())]
        elif ctx.forStmt():
            return [self.visit(ctx.forStmt())]
        elif ctx.breakStmt():
            return [self.visit(ctx.breakStmt())]
        elif ctx.continueStmt():
            return [self.visit(ctx.continueStmt())]
        elif ctx.returnStmt():
            return [self.visit(ctx.returnStmt())]
        elif ctx.withStmt():
            return [self.visit(ctx.withStmt())]
        elif ctx.callStmt():
            return [self.visit(ctx.callStmt())]
        elif ctx.ifStmt():
            return [self.visit(ctx.ifStmt())]

    #assignStmt: (assignOperand ASSIGN)+ expr SEMI;
    def visitAssignStmt(self, ctx:MPParser.AssignStmtContext):
        list_assignOp = ctx.assignOperand()
        list_assignOp.append(ctx.expr())
        length = len(list_assignOp)
        out = []
        while length > 1:
            length -= 1
            out.append(Assign(self.visit(list_assignOp[length - 1]), self.visit(list_assignOp[length])))
        return out

    #assignOperand: IDENTIFIER|indexExpr;
    def visitAssignOperand(self, ctx:MPParser.AssignOperandContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        else:
            return self.visit(ctx.indexExpr())

    #ifStmt: unMatchIfStmt|matchIfStmt;
    def visitIfStmt(self, ctx:MPParser.IfStmtContext):
        if ctx.unMatchIfStmt():
            return self.visit(ctx.unMatchIfStmt())
        else:
            return self.visit(ctx.matchIfStmt())

    # matchIfStmt: IF expr THEN matchIfStmt ELSE matchIfStmt
	# 		| (assignStmt|whileStmt|forStmt|withStmt|returnStmt|callStmt|breakStmt|continueStmt)
	# 		| BEGIN (assignStmt|whileStmt|forStmt|withStmt|returnStmt|callStmt|breakStmt|continueStmt) END
	# 		| BEGIN stmtsList END;
    def visitMatchIfStmt(self, ctx:MPParser.MatchIfStmtContext):
        if ctx.getChildCount() == 6:
            ls_left = [self.visit(ctx.matchIfStmt(0))]
            if type(ls_left[0]) is list:
                ls_left_fixed = [i for j in ls_left for i in j]
            else:
                ls_left_fixed = ls_left
            ls_right = [self.visit(ctx.matchIfStmt(1))]
            if type(ls_right[0]) is list:
                ls_right_fixed = [i for j in ls_right for i in j]
            else:
                ls_right_fixed = ls_right
            return If(self.visit(ctx.expr()), ls_left_fixed, ls_right_fixed)
        elif ctx.assignStmt():
            return self.visit(ctx.assignStmt())
        elif ctx.whileStmt():
            return [self.visit(ctx.whileStmt())]
        elif ctx.forStmt():
            return [self.visit(ctx.forStmt())]
        elif ctx.breakStmt():
            return [self.visit(ctx.breakStmt())]
        elif ctx.continueStmt():
            return [self.visit(ctx.continueStmt())]
        elif ctx.returnStmt():
            return [self.visit(ctx.returnStmt())]
        elif ctx.withStmt():
            return [self.visit(ctx.withStmt())]
        elif ctx.callStmt():
            return [self.visit(ctx.callStmt())]
        elif ctx.stmtsList():
            return self.visit(ctx.stmtsList())

    #unMatchIfStmt: IF expr THEN ifStmt | IF expr THEN matchIfStmt ELSE unMatchIfStmt;
    def visitUnMatchIfStmt(self, ctx:MPParser.UnMatchIfStmtContext):
        if ctx.getChildCount() == 4:
            ls = [self.visit(ctx.ifStmt())]
            if type(ls[0]) is list:
                ls_fixed = [i for j in ls for i in j]
            else:
                ls_fixed = ls
            return If(self.visit(ctx.expr()), ls_fixed, [])
        else:
            ls_left = [self.visit(ctx.matchIfStmt())]
            if type(ls_left[0]) is list:
                ls_left_fixed = [i for j in ls_left for i in j]
            else:
                ls_left_fixed = ls_left
            ls_right = [self.visit(ctx.unMatchIfStmt())]
            if type(ls_right[0]) is list:
                ls_right_fixed = [i for j in ls_right for i in j]
            else:
                ls_right_fixed = ls_right
            return If(self.visit(ctx.expr()), ls_left_fixed, ls_right_fixed)

    #whileStmt: WHILE expr DO bodyIter;
    def visitWhileStmt(self, ctx:MPParser.WhileStmtContext):
        return While(self.visit(ctx.expr()), self.visit(ctx.bodyIter()))

    #bodyIter: BEGIN stmtsList END | BEGIN stmts END | stmts;
    def visitBodyIter(self, ctx:MPParser.BodyIterContext):
        if ctx.stmtsList():
            return self.visit(ctx.stmtsList())          
        else:
            return self.visit(ctx.stmts())

    #forStmt: FOR forCondition DO bodyIter;
    def visitForStmt(self, ctx:MPParser.ForStmtContext):
        id, expr1, up, expr2 = self.visit(ctx.forCondition())
        return For(id, expr1, expr2, up, self.visit(ctx.bodyIter()))

    #forCondition: IDENTIFIER ASSIGN expr (TO|DOWNTO) expr;
    def visitForCondition(self, ctx:MPParser.ForConditionContext):
        up = True
        if ctx.DOWNTO():
            up = False
        return Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expr(0)), up, self.visit(ctx.expr(1))

    #breakStmt: BREAK SEMI;
    def visitBreakStmt(self, ctx:MPParser.BreakStmtContext):
        return Break()

    #continueStmt: CONTINUE SEMI;
    def visitContinueStmt(self, ctx:MPParser.ContinueStmtContext):
        return Continue()

    #returnStmt: RETURN (expr)? SEMI;
    def visitReturnStmt(self, ctx:MPParser.ReturnStmtContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        return Return()

    #withStmt: WITH (withVarDecl)? DO bodyIter;
    def visitWithStmt(self, ctx:MPParser.WithStmtContext):
        return With(self.visit(ctx.withVarDecl()), self.visit(ctx.bodyIter()))

    #withVarDecl: varTypeDeclList SEMI | LB varTypeDeclList SEMI RB;
    def visitWithVarDecl(self, ctx:MPParser.WithVarDeclContext):
        return self.visit(ctx.varTypeDeclList())

    #callStmt: invoExpr SEMI;
    def visitCallStmt(self, ctx:MPParser.CallStmtContext):
        return self.visit(ctx.invoExpr())

    #invoExpr: IDENTIFIER LB (exprList)? RB;
    def visitInvoExpr(self, ctx:MPParser.InvoExprContext):
        if ctx.exprList():
            return CallStmt(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.exprList()))
        return CallStmt(Id(ctx.IDENTIFIER().getText()), [])

    #exprList: expr (COMMA expr)*;
    def visitExprList(self, ctx:MPParser.ExprListContext):
        return [self.visit(x) for x in ctx.expr()]

    #indexExpr: (IDENTIFIER|callExpr) LQ expr RQ;
    def visitIndexExpr(self, ctx:MPParser.IndexExprContext):
        if ctx.IDENTIFIER():
            return ArrayCell(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expr()))
        else:
            return ArrayCell(self.visit(ctx.callExpr()), self.visit(ctx.expr()))
    
    #callExpr: IDENTIFIER LB (exprList)? RB;
    def visitCallExpr(self, ctx:MPParser.CallExprContext):
        if ctx.exprList():
            return CallExpr(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.exprList()))
        return CallExpr(Id(ctx.IDENTIFIER().getText()), [])

    # def visitFuncall(self,ctx:MPParser.FuncallContext):
    #     return CallStmt(Id(ctx.ID().getText()),[self.visit(ctx.exp())] if ctx.exp() else [])



        
