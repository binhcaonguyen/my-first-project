import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    
    def test_simple_program(self):
        input = """var a: array [-1 .. 2] of integer;"""
        expect = ""
        TestAST.test(input,expect,300)


    # def test_full_15(self):
    #     input = """procedure main (); 
    #     begin
    #         if a>b then 
    #             for id := -1 downto 3 do continue;
    #         else
    #             while (a<>b) do break;
    #     end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             If(BinaryOp(">",Id("a"),Id("b")),[
    #                 For(Id("id"),UnaryOp("-",IntLiteral(1)),IntLiteral(3),"False",["Continue"])],[
    #                 While(BinaryOp("<>",Id("a"),Id("b")),["Break"])])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,300))

    # def test_full_14(self):
    #     input = """procedure main(); 
    #         begin
    #             while (a<>b) do break;
    #             with a:integer; do
    #                 for id := -1 downto 3 do continue;
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             While(BinaryOp("<>",Id("a"),Id("b")),["Break"]),
    #             With([VarDecl(Id("a"),IntType())],[
    #                 For(Id("id"),UnaryOp("-",IntLiteral(1)),IntLiteral(3),"False",["Continue"])])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,301)) 

    # def test_call_7(self):
    #     input = """procedure main(); 
    #         begin
    #             foo(s, "s");
    #             putIntLn(4);
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             CallStmt(Id("foo"),[Id("s"),StringLiteral("s")]),
    #             CallStmt(Id("putIntLn"),[IntLiteral(4)])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,302)) 

    # def test_full_13(self):
    #     input = """procedure main(arg: string);
    #         var arr: array [-1 .. -3] of real; 
    #         begin
    #             id1 := id2 := id3;
    #             while not(a) do b := true;
    #             for id := 3 downto 1 do b:=3.6;
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[VarDecl(Id("arg"),StringType())],
    #             [VarDecl(Id("arr"),ArrayType(IntLiteral(-1),IntLiteral(-3),FloatType()))],[
    #             Assign(Id("id2"),Id("id3")),
    #             Assign(Id("id1"),Id("id2")),
    #             While(UnaryOp("not",Id("a")),[
    #                 Assign(Id("b"),BooleanLiteral("true"))]),
    #             For(Id("id"),IntLiteral(3),IntLiteral(1),"False",[
    #                 Assign(Id("b"),FloatLiteral(3.6))])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,303)) 

    # def test_full_12(self):
    #     input = """var a: array [2 .. 10] of integer;
    #         procedure main(); 
    #         var arr: array [-1 .. -3] of string;
    #         begin
    #         end 
    #         function foo(b: boolean): integer; 
    #         var c,d: real;
    #         begin
    #         end"""
    #     expect = str(Program([
    #             VarDecl(Id("a"),ArrayType(IntLiteral(2),IntLiteral(10),IntType())),
    #             FuncDecl(Id("main"),
    #                 [],
    #                 [VarDecl(Id("arr"),ArrayType(IntLiteral(-1),IntLiteral(-3),StringType()))],
    #                 []),
    #             FuncDecl(Id("foo"),
    #                 [VarDecl(Id("b"),BoolType())],
    #                 [VarDecl(Id("c"),FloatType()),VarDecl(Id("d"),FloatType())],
    #                 [],IntType())
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,304))

    # def test_random_1(self):
    #     input = """var a:boolean;
    #                     b: integer;
    #                 var c: array [-8 .. 8] of real;"""
    #     expect = str(Program([
    #             VarDecl(Id("a"),BoolType()),
    #             VarDecl(Id("b"),IntType()),
    #             VarDecl(Id("c"),ArrayType(IntLiteral(-8),IntLiteral(8),FloatType()))
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,305))

    # def test_full_11(self):
    #     input = """procedure main (); 
    #     begin
    #         if a>b then 
    #             if b>c then min := c;
    #         else
    #             return (a and then b);
    #     end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             If(BinaryOp(">",Id("a"),Id("b")),[
    #                 If(BinaryOp(">",Id("b"),Id("c")),[Assign(Id("min"),Id("c"))],[
    #                 Return(BinaryOp("andthen",Id("a"),Id("b")))])],[])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,306))  

    # def test_comment_3(self):
    #     input = """var a: integer; {b,c: real;
    #                var d: string;}"""
    #     expect = str(Program([VarDecl(Id("a"),IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,307))

    # def test_full_10(self):
    #     input = """Function Factorial(n : Integer) : Integer;
    #         Var Result : Integer;
    #         Begin
    #             If n = 1 Then 
    #                 Factorial := 1;
    #             Else
    #                 Factorial := n*Factorial(n-1);
    #         End"""
    #     expect = str(Program([
    #         FuncDecl(Id("Factorial"),[
    #             VarDecl(Id("n"),IntType())],[
    #             VarDecl(Id("Result"),IntType())],[
    #             If(BinaryOp("=",Id("n"),IntLiteral(1)),[
    #                 Assign(Id("Factorial"),IntLiteral(1))],[
    #                 Assign(Id("Factorial"),BinaryOp("*",Id("n"),
    #                     CallExpr(Id("Factorial"),[
    #                         BinaryOp("-",Id("n"),IntLiteral(1))])))])],IntType())
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,308)) 

    # def test_full_9(self):
    #     input = """procedure main(); 
	#         begin
	#             For Counter := 5 Downto 1 do
	#             Begin  {an example of "downto" instead of "to", note the "gotoxy(_,_)"}
	# 	            gotoxy(32, 11 - Counter);
	# 	            Writeln("I");
	#             End
	#         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             For(Id("Counter"),IntLiteral(5),IntLiteral(1),"False",[
    #                 CallStmt(Id("gotoxy"),[IntLiteral(32),
    #                     BinaryOp("-",IntLiteral(11),Id("Counter"))]),
    #                 CallStmt(Id("Writeln"),[StringLiteral("I")])])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,309))  

    # def test_full_8(self):
    #     input = """Var UFile : String;
    #         Procedure main();
    #         Begin
    #             Assign(UFile, "C:\\\\ADDTEXT.TXT");
    #             ReWrite(UFile); 
    #             Writeln(UFile, "How many sentences " + "are present in this file?");
    #             Close(UFile);
    #         End"""
    #     expect = str(Program([
    #         VarDecl(Id("UFile"),StringType()),
    #         FuncDecl(Id("main"),[],[],[
    #             CallStmt(Id("Assign"),[Id("UFile"),StringLiteral("C:\\\\ADDTEXT.TXT")]),
    #             CallStmt(Id("ReWrite"),[Id("UFile")]),
    #             CallStmt(Id("Writeln"),[Id("UFile"),
    #                 BinaryOp("+",StringLiteral("How many sentences "),
    #                     StringLiteral("are present in this file?"))]),
    #             CallStmt(Id("Close"),[Id("UFile")])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,310)) 

    # def test_full_7(self):
    #     input = """procedure main(); 
	#         begin
	#             for a := 1 to 3 do 
    #                 with a:integer; do
    #                     if (a>b) then a := 3*b;
	#         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             For(Id("a"),IntLiteral(1),IntLiteral(3),"True",[
    #                 With([VarDecl(Id("a"),IntType())],[
    #                     If(BinaryOp(">",Id("a"),Id("b")),[
    #                         Assign(Id("a"),BinaryOp("*",IntLiteral(3),Id("b")))],[])])])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,311))   

    # def test_call_6(self):
    #     input = """procedure main(); 
	#             begin
	#                 foo(5,foo(foo(5,a),b),a[3+a]);
	#             end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             CallStmt(Id("foo"),[IntLiteral(5),CallExpr(Id("foo"),[
    #                 CallExpr(Id("foo"),[IntLiteral(5),Id("a")]),Id("b")]),
    #                     ArrayCell(Id("a"),BinaryOp("+",IntLiteral(3),Id("a")))])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,312))

    # def test_index_5(self):
    #     input = """procedure main();
    #             begin
    #                 foo((+2))[3+x] := a[b[-2]] +3;
    #             end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             Assign(ArrayCell(CallExpr(Id("foo"),[
    #                 UnaryOp("+",IntLiteral(2))]),BinaryOp("+",IntLiteral(3),Id("x"))),
    #             BinaryOp("+",ArrayCell(Id("a"),
    #                 ArrayCell(Id("b"),UnaryOp("-",IntLiteral(2)))),IntLiteral(3)))])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,313))

    # def test_comment_2(self):
    #     input = """var i: array [1 .. 5]// of integer;
    #                     of boolean;"""
    #     expect = str(Program([
    #             VarDecl(Id("i"),ArrayType(IntLiteral(1),IntLiteral(5),BoolType()))
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,314))

    # def test_comment_1(self):
    #     input = """var a: integer; b,c: real;
    #                (*var d: string;*)"""
    #     expect = str(Program([
    #             VarDecl(Id("a"),IntType()),
    #             VarDecl(Id("b"),FloatType()),
    #             VarDecl(Id("c"),FloatType())
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,315))

    # def test_call_5(self):
    #     input = """function foo():INTEGER; 
    #         begin 
    #             foo(a[a[5]]-5);
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("foo"),[],[],[
    #             CallStmt(Id("foo"),[BinaryOp("-",ArrayCell(Id("a"),
    #                 ArrayCell(Id("a"),IntLiteral(5))),IntLiteral(5))])],IntType())
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,316))

    # def test_if_while(self):
    #     input = """procedure main (); 
    #     begin
    #         while (id <> true) do
    #         begin
    #             putIntLn(i);
    #             if a mod b = 2 then
    #                 continue;
    #             a := a + 2;
    #         end
    #     end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             While(BinaryOp("<>",Id("id"),BooleanLiteral("true")),[
    #                 CallStmt(Id("putIntLn"),[Id("i")]),
    #                 If(BinaryOp("=",BinaryOp("mod",Id("a"),Id("b")),IntLiteral(2)),["Continue"],[]),
    #                 Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(2)))])]
    #         )]))
    #     self.assertTrue(TestAST.test(input,expect,317))

    # def test_if_for(self):
    #     input = """procedure main (); 
    #     begin
    #         for id := -1 downto -3 do
    #         begin
    #             putIntLn(i);
    #             if a mod b = 2 then
    #                 break;
    #             a := a + 2;
    #         end
    #     end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             For(Id("id"),UnaryOp("-",IntLiteral(1)),UnaryOp("-",IntLiteral(3)),"False",[
    #                 CallStmt(Id("putIntLn"),[Id("i")]),
    #                 If(BinaryOp("=",BinaryOp("mod",Id("a"),Id("b")),IntLiteral(2)),["Break"],[]),
    #                 Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(2)))])]
    #         )]))
    #     self.assertTrue(TestAST.test(input,expect,318))

    # def test_full_6(self):
    #     input = """Var surname: String;
    #         procedure main();
    #         Begin
    #             Write("Enter your surname:");
    #             readln(surname);
    #             writeln();
    #             writeln();
    #             Writeln("Your full name is: ",name," ",surname);
    #             readln();
    #         End"""
    #     expect = str(Program([
    #         VarDecl(Id("surname"),StringType()),
    #         FuncDecl(Id("main"),[],[],[
    #             CallStmt(Id("Write"),[StringLiteral("Enter your surname:")]),
    #             CallStmt(Id("readln"),[Id("surname")]),
    #             CallStmt(Id("writeln"),[]),
    #             CallStmt(Id("writeln"),[]),
    #             CallStmt(Id("Writeln"),[StringLiteral("Your full name is: "),
    #                 Id("name"),StringLiteral(" "),Id("surname")]),
    #             CallStmt(Id("readln"),[])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,319))

    # def test_if_11(self):
    #     input = """procedure main (); 
    #     begin
    #         if a>b then 
    #             if b>c then
    #                 if c>a then 
    #                     a := c;
    #                 else
    #                     c := a;
    #     end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             If(BinaryOp(">",Id("a"),Id("b")),[
    #                 If(BinaryOp(">",Id("b"),Id("c")),[
    #                     If(BinaryOp(">",Id("c"),Id("a")),[
    #                         Assign(Id("a"),Id("c"))],[
    #                         Assign(Id("c"),Id("a"))])],[])],[])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,320))

    # def test_if_10(self):
    #     input = """procedure main (); 
    #     begin
    #         if a>b then 
    #             if b>c then min:=c; else min:=b;
    #         else
    #             if a>c then min:=c; else min:=a;
    #     end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             If(BinaryOp(">",Id("a"),Id("b")),[
    #                 If(BinaryOp(">",Id("b"),Id("c")),[Assign(Id("min"),Id("c"))],[
    #                     Assign(Id("min"),Id("b"))])],[
    #                 If(BinaryOp(">",Id("a"),Id("c")),[Assign(Id("min"),Id("c"))],[
    #                     Assign(Id("min"),Id("a"))])])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,321))

    # def test_if_9(self):
    #     input = """procedure main (); 
    #     begin
    #         if a>b then 
    #         begin
    #             if b>c then
    #             begin 
    #                 min:=c; 
    #             end    
    #             else min:=b;
    #         end
    #         else
    #         begin
    #             if a>c then min:=c; else 
    #             begin 
    #                 min:=a;
    #             end
    #         end
    #     end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             If(BinaryOp(">",Id("a"),Id("b")),[
    #                 If(BinaryOp(">",Id("b"),Id("c")),[Assign(Id("min"),Id("c"))],[
    #                     Assign(Id("min"),Id("b"))])],[
    #                 If(BinaryOp(">",Id("a"),Id("c")),[Assign(Id("min"),Id("c"))],[
    #                     Assign(Id("min"),Id("a"))])])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,322))

    # def test_if_8(self):
    #     input = """procedure main (); 
    #     begin
    #         if a>b then 
    #             if b>c then min := c;
    #         else
    #             if a>c then min := c;
    #     end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             If(BinaryOp(">",Id("a"),Id("b")),[
    #                 If(BinaryOp(">",Id("b"),Id("c")),[Assign(Id("min"),Id("c"))],[
    #                 If(BinaryOp(">",Id("a"),Id("c")),[Assign(Id("min"),Id("c"))],[])])],[])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,323))

    # def test_if_7(self):
    #     input = """procedure main (); 
    #     begin
    #         if a>b then 
    #             min := b;
    #         else
    #             if a<b then min := a;
    #     end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             If(BinaryOp(">",Id("a"),Id("b")),[
    #                 Assign(Id("min"),Id("b"))],[
    #             If(BinaryOp("<",Id("a"),Id("b")),[
    #                 Assign(Id("min"),Id("a"))],[])])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,324))

    # def test_if_6(self):
    #     input = """procedure main (); 
    #     begin
    #         if a>b then 
    #             min := b;
    #         else
    #             min := a;
    #     end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             If(BinaryOp(">",Id("a"),Id("b")),[
    #                 Assign(Id("min"),Id("b"))],[
    #                 Assign(Id("min"),Id("a"))])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,325))

    # def test_if_5(self):
    #     input = """procedure main (); 
    #     begin
    #         if a>b then 
    #             if b>c then  min := c; 
    #     end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             If(BinaryOp(">",Id("a"),Id("b")),[
    #                 If(BinaryOp(">",Id("b"),Id("c")),[
    #                     Assign(Id("min"),Id("c"))],[])],[])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,326))

    # def test_with_5(self):
    #     input = """procedure main(); 
    #         begin
    #             with a:integer; do
    #             begin
    #                 a := 5;
    #                 b := 6;
    #             end
    #             c := 7;
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             With([VarDecl(Id("a"),IntType())],[
    #                 Assign(Id("a"),IntLiteral(5)),
    #                 Assign(Id("b"),IntLiteral(6))]),
    #             Assign(Id("c"),IntLiteral(7))])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,327))

    # def test_if_4(self):
    #     input = """procedure main (); 
    #     begin
    #         if a>b then 
    #             begin
    #                 if b>c then min := c;
    #             end
    #     end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             If(BinaryOp(">",Id("a"),Id("b")),[
    #                 If(BinaryOp(">",Id("b"),Id("c")),[Assign(Id("min"),Id("c"))],[])],
    #                 [])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,328))

    # def test_if_3(self):
    #     input = """procedure main (); 
    #     begin
    #         if a>b then min := b;
    #         if a<b then min := a;
    #     end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             If(BinaryOp(">",Id("a"),Id("b")),[
    #                 Assign(Id("min"),Id("b"))],[]),
    #             If(BinaryOp("<",Id("a"),Id("b")),[
    #                 Assign(Id("min"),Id("a"))],[])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,329))

    # def test_if_2(self):
    #     input = """procedure main (); 
    #     begin
    #         if a>b then min := b; else min := a;
    #     end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             If(BinaryOp(">",Id("a"),Id("b")),[
    #                 Assign(Id("min"),Id("b"))],[
    #                 Assign(Id("min"),Id("a"))])])]))
    #     self.assertTrue(TestAST.test(input,expect,330))

    # def test_if_1(self):
    #     input = """procedure main (); 
    #     begin
    #         if a>b then min := b;
    #     end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             If(BinaryOp(">",Id("a"),Id("b")),[
    #                 Assign(Id("min"),Id("b"))],[])])]))
    #     self.assertTrue(TestAST.test(input,expect,331))

    # def test_full_5(self):
    #     input = """procedure main (); 
    #     begin
    #         getIntLn();
    #     end
    #     function foo ():INTEGER; 
    #     begin
    #         putIntLn(4);
    #     end"""
    #     expect = str(Program([
    #             FuncDecl(Id("main"),[],[],[CallStmt(Id("getIntLn"),[])]),
    #             FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,332))

    # def test_full_4(self):
    #     input = """function foo ():INTEGER; 
    #         begin
    #         putIntLn(4);
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("foo"),[],[],[
    #             CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,333))

    # def test_index_with(self):
    #     input = """procedure main(); 
    #         begin
    #             with a, b: integer; c: array [1 .. 2] of real; do
    #                 d := c[a] + b;
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             With([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),
    #                 VarDecl(Id("c"),ArrayType(IntLiteral(1),IntLiteral(2),FloatType()))],[
    #                 Assign(Id("d"),BinaryOp("+",ArrayCell(Id("c"),Id("a")),Id("b")))])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,334))

    # def test_index_4(self):
    #     input = """procedure main(); 
    #         begin
    #             foo(2)[3+x] := a[b[2]] +3;
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[Assign(ArrayCell(
    #             CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),
    #             BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3)))])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,335))

    # def test_index_3(self):
    #     input = """procedure main(); 
    #         begin
    #             a := b[10] := foo()[3] := x := 1;
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             Assign(Id("x"),IntLiteral(1)),
    #             Assign(ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(3)),Id("x")),
    #             Assign(ArrayCell(Id("b"),IntLiteral(10)),
    #                 ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(3))),
    #             Assign(Id("a"),ArrayCell(Id("b"),IntLiteral(10)))])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,336))

    # def test_index_2(self):
    #     input = """procedure main(); 
    #         begin
    #             foo[a or else b] := goo[1];
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             Assign(ArrayCell(Id("foo"),BinaryOp("orelse",Id("a"),Id("b"))),
    #             ArrayCell(Id("goo"),IntLiteral(1)))])]))
    #     self.assertTrue(TestAST.test(input,expect,337))

    # def test_index_1(self):
    #     input = """procedure main(); 
    #         begin
    #             foo[0] := 1;
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             Assign(ArrayCell(Id("foo"),IntLiteral(0)),IntLiteral(1))])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,338)) 

    # def test_call_4(self):
    #     input = """procedure main(); 
    #         begin
    #             foo(3 ,a+1, m(2));
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             CallStmt(Id("foo"),[IntLiteral(3),
    #                 BinaryOp("+",Id("a"),IntLiteral(1)),
    #                 CallExpr(Id("m"),[IntLiteral(2)])])])
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,339)) 

    # def test_call_3(self):
    #     input = """procedure main(); 
    #         begin
    #             foo(x, "x");
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[CallStmt(Id("foo"),[Id("x"),StringLiteral("x")])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,340)) 

    # def test_call_2(self):
    #     input = """procedure main(); 
    #         begin
    #             foo(x);
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[CallStmt(Id("foo"),[Id("x")])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,341))     

    # def test_call_1(self):
    #     input = """procedure main(); 
    #         begin
    #             foo();
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[CallStmt(Id("foo"),[])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,342)) 

    # def test_with_4(self):
    #     input = """procedure main(); 
    #         begin
    #             while (a<>b) do 
    #                 with a:integer; do
    #                     for id := -1 downto 3 do return;
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             While(BinaryOp("<>",Id("a"),Id("b")),[
    #                 With([VarDecl(Id("a"),IntType())],[
    #                     For(Id("id"),UnaryOp("-",IntLiteral(1)),IntLiteral(3),"False",[
    #                         Return()])])])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,343)) 

    # def test_full_3(self):
    #     input = """procedure main(arg: string);
    #         var arr: array [-1 .. -3] of real; 
    #         begin
    #             id1 := id2 := id3;
    #             while not(a) do break;
    #             for id := 3 downto 1 do continue;
    #             with a:boolean; do a := true; 
    #             return "binh";
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[VarDecl(Id("arg"),StringType())],[
    #             VarDecl(Id("arr"),ArrayType(IntLiteral(-1),IntLiteral(-3),FloatType()))],[
    #             Assign(Id("id2"),Id("id3")),Assign(Id("id1"),Id("id2")),
    #             While(UnaryOp("not",Id("a")),["Break"]),
    #             For(Id("id"),IntLiteral(3),IntLiteral(1),"False",["Continue"]),
    #             With([VarDecl(Id("a"),BoolType())],[Assign(Id("a"),BooleanLiteral("true"))]),
    #             Return(StringLiteral("binh"))])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,344))

    # def test_with_3(self):
    #     input = """procedure main(); 
    #         begin
    #             while (a<>b) do break;
    #             with a:integer; do
    #                 for id := -1 downto 3 do continue;
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             While(BinaryOp("<>",Id("a"),Id("b")),["Break"]),
    #             With([VarDecl(Id("a"),IntType())],[
    #                 For(Id("id"),UnaryOp("-",IntLiteral(1)),IntLiteral(3),"False",["Continue"])])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,345)) 

    # def test_with_2(self):
    #     input = """procedure main(); 
    #         begin
    #             with a:integer; arr: array [-3 .. 9] of real; do
    #                 a := b := "binh";
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             With([VarDecl(Id("a"),IntType()),
    #                 VarDecl(Id("arr"),ArrayType(IntLiteral(-3),IntLiteral(9),FloatType()))],[
    #                     Assign(Id("b"),StringLiteral("binh")),
    #                     Assign(Id("a"),Id("b"))])])]))
    #     self.assertTrue(TestAST.test(input,expect,346)) 

    # def test_with_1(self):
    #     input = """procedure main(); 
    #         begin
    #             with a:integer; do
    #                 a := 5;
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #                 With([VarDecl(Id("a"),IntType())],[
    #                     Assign(Id("a"),IntLiteral(5))])])]))
    #     self.assertTrue(TestAST.test(input,expect,347)) 

    # def test_full_2(self):
    #     input = """procedure main(arg: string);
    #         var arr: array [-1 .. -3] of real; 
    #         begin
    #             id1 := id2 := id3;
    #             while not(a) do break;
    #             for id := 3 downto 1 do continue;
    #             return "binh";
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[VarDecl(Id("arg"),StringType())],
    #             [VarDecl(Id("arr"),ArrayType(IntLiteral(-1),IntLiteral(-3),FloatType()))],[
    #             Assign(Id("id2"),Id("id3")),
    #             Assign(Id("id1"),Id("id2")),
    #             While(UnaryOp("not",Id("a")),[
    #                 "Break"]),
    #             For(Id("id"),IntLiteral(3),IntLiteral(1),"False",[
    #                 "Continue"]),
    #             Return(StringLiteral("binh"))])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,348)) 

    # def test_return_2(self):
    #     input = """procedure main(); 
    #         begin
    #             return (a and then b);
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             Return(BinaryOp("andthen",Id("a"),Id("b")))])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,349))

    # def test_return_1(self):
    #     input = """procedure main(); 
    #         begin
    #             return;
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[Return()])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,350))

    # def test_continue_while(self):
    #     input = """procedure main(); 
    #         begin
    #             while (-id) do 
    #                 cOnTiNue;
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[While(UnaryOp("-",Id("id")),["Continue"])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,351)) 

    # def test_continue_for(self):
    #     input = """procedure main(); 
    #         begin
    #             for id := 1 to 3 do 
    #                 cOnTiNue;
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             For(Id("id"),IntLiteral(1),IntLiteral(3),"True",["Continue"])])
    #           ]))
    #     self.assertTrue(TestAST.test(input,expect,352)) 

    # def test_break_while(self):
    #     input = """procedure main(); 
    #         begin
    #             while (-id) do 
    #                 bReAk;
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[While(UnaryOp("-",Id("id")),["Break"])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,353)) 

    # def test_break_for(self):
    #     input = """procedure main(); 
    #         begin
    #             for id := 1 to 3 do 
    #                 bReAk;
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             For(Id("id"),IntLiteral(1),IntLiteral(3),"True",["Break"])])
    #           ]))
    #     self.assertTrue(TestAST.test(input,expect,354)) 

    # def test_full_1(self):
    #     input = """procedure main(arg: string);
    #         var arr: array [-1 .. -3] of real; 
    #         begin
    #             id1 := id2 := id3;
    #             while not(a) do b := true;
    #             for id := 3 downto 1 do b:=3.6;
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[VarDecl(Id("arg"),StringType())],
    #             [VarDecl(Id("arr"),ArrayType(IntLiteral(-1),IntLiteral(-3),FloatType()))],[
    #             Assign(Id("id2"),Id("id3")),
    #             Assign(Id("id1"),Id("id2")),
    #             While(UnaryOp("not",Id("a")),[
    #                 Assign(Id("b"),BooleanLiteral("true"))]),
    #             For(Id("id"),IntLiteral(3),IntLiteral(1),"False",[
    #                 Assign(Id("b"),FloatLiteral(3.6))])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,355)) 

    # def test_for_var(self):
    #     input = """procedure main(); 
    #         begin
    #             id1 := id2 := id3;
    #             for id := 3 downto 1 do b:=3.6;
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             Assign(Id("id2"),Id("id3")),
    #             Assign(Id("id1"),Id("id2")),
    #             For(Id("id"),IntLiteral(3),IntLiteral(1),"False",[
    #                 Assign(Id("b"),FloatLiteral(3.6))])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,356)) 

    # def test_for_while_4(self):
    #     input = """procedure main(); 
    #         begin
    #             id1 := id2 := id3;
    #             while not(a) do b := true;
    #             for id := 3 downto 1 do b:=3.6;
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             Assign(Id("id2"),Id("id3")),
    #             Assign(Id("id1"),Id("id2")),
    #             While(UnaryOp("not",Id("a")),[
    #                 Assign(Id("b"),BooleanLiteral("true"))]),
    #             For(Id("id"),IntLiteral(3),IntLiteral(1),"False",[
    #                 Assign(Id("b"),FloatLiteral(3.6))])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,357)) 

    # def test_for_while_3(self):
    #     input = """procedure main(); 
    #         begin
    #             while not(a) do b := true;
    #             for id := 3 downto 1 do b:=3.6;
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             While(UnaryOp("not",Id("a")),[
    #                 Assign(Id("b"),BooleanLiteral("true"))]),
    #             For(Id("id"),IntLiteral(3),IntLiteral(1),"False",[
    #                 Assign(Id("b"),FloatLiteral(3.6))])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,358))  

    # def test_for_while_2(self):
    #     input = """procedure main(); 
    #         begin
    #             while not(a) do 
    #             begin
    #                 for id := 3 downto 1 do b:=3.6;
    #             end
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             While(UnaryOp("not",Id("a")),[
    #                 For(Id("id"),IntLiteral(3),IntLiteral(1),"False",[
    #                     Assign(Id("b"),FloatLiteral(3.6))])])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,359))

    # def test_for_while_1(self):
    #     input = """procedure main(); 
    #         begin
    #             for id := 1 to 3 do 
    #             begin
    #                 while not(a) do b:=3.6;
    #             end
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             For(Id("id"),IntLiteral(1),IntLiteral(3),"True",[
    #                 While(UnaryOp("not",Id("a")),[
    #                     Assign(Id("b"),FloatLiteral(3.6))])])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,360))

    # def test_for_4(self):
    #     input = """procedure main(); 
    #         begin
    #             for id := (3.6) downto (a mod b) do 
    #             begin
    #                 for id := 1 to 3 do a:=5;
    #             end
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             For(Id("id"),FloatLiteral(3.6),
    #                 BinaryOp("mod",Id("a"),Id("b")),"False",[
    #                     For(Id("id"),IntLiteral(1),IntLiteral(3),"True",[
    #                     Assign(Id("a"),IntLiteral(5))])])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,361))

    # def test_for_3(self):
    #     input = """procedure main(); 
    #         begin
    #             for id := (3.6) downto (a mod b) do c := d:= "binh";
    #             for id := 1 to 3 do a:=5;
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             For(Id("id"),FloatLiteral(3.6),
    #                 BinaryOp("mod",Id("a"),Id("b")),"False",[
    #                 Assign(Id("d"),StringLiteral("binh")),
    #                     Assign(Id("c"),Id("d"))]),
    #             For(Id("id"),IntLiteral(1),IntLiteral(3),"True",[
    #                  Assign(Id("a"),IntLiteral(5))])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,362))

    # def test_for_2(self):
    #     input = """procedure main(); 
    #         begin
    #             for id := (3.6) downto (a mod b) do c := d:= "binh";
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             For(Id("id"),FloatLiteral(3.6),
    #                 BinaryOp("mod",Id("a"),Id("b")),"False",[
    #                 Assign(Id("d"),StringLiteral("binh")),
    #                     Assign(Id("c"),Id("d"))])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,363))

    # def test_for_1(self):
    #     input = """procedure main(); 
    #         begin
    #             for id := 1 to 3 do a:=5;
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             For(Id("id"),IntLiteral(1),IntLiteral(3),"True",[
    #                 Assign(Id("a"),IntLiteral(5))])])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,364))

    # def test_expr_2(self):
    #     input = """procedure main(); 
    #         begin
    #             a := (5 * id) mod (true and 3.6);
    #             b := ("binh" div 3) / 4;
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             Assign(Id("a"),
    #                 BinaryOp("mod",BinaryOp("*",IntLiteral(5),Id("id")),
    #                     BinaryOp("and",BooleanLiteral("true"),FloatLiteral(3.6)))),
    #             Assign(Id("b"),BinaryOp("/",
    #                 BinaryOp("div",StringLiteral("binh"),IntLiteral(3)),IntLiteral(4)))])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,365))

    # def test_expr_1(self):
    #     input = """procedure main(); 
    #         begin
    #             a := (5 + true) and then 3.6;
    #             b := ("binh" or else false) - 4;
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             Assign(Id("a"),
    #                 BinaryOp("andthen",
    #                     BinaryOp("+",IntLiteral(5),BooleanLiteral("true")),FloatLiteral(3.6))),
    #             Assign(Id("b"),
    #                 BinaryOp("-",
    #                     BinaryOp("orelse",StringLiteral("binh"),BooleanLiteral("false")),IntLiteral(4)))])
    #         ]))
    #     self.assertTrue(TestAST.test(input,expect,366))

    # def test_while_assign(self):
    #     input = """procedure main(); 
    #         begin
    #             b := c := arr;
    #             while a<=3 do
    #                 e := f := 4;
    #         end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),[],[],[
    #             Assign(Id("c"),Id("arr")),
    #                 Assign(Id("b"),Id("c")),
    #             While(BinaryOp("<=",Id("a"),IntLiteral(3)),[
    #                 Assign(Id("f"),IntLiteral(4)),
    #                     Assign(Id("e"),Id("f"))])])]))
    #     self.assertTrue(TestAST.test(input,expect,367))

    # def test_while_3(self):
    #     input = """procedure main(); 
    #         begin
    #             while a<>b do
    #                 begin
    #                     while -e do
    #                         b := c := true;
    #                 end
    #         end"""
    #     expect = str(Program([
    #             FuncDecl(Id("main"),[],[],
    #                 [While(BinaryOp("<>",Id("a"),Id("b")),
    #                     [While(UnaryOp("-",Id("e")),
    #                         [Assign(Id("c"),BooleanLiteral("true")),
    #                         Assign(Id("b"),Id("c"))])])])
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,368))

    # def test_while_2(self):
    #     input = """procedure main(); 
    #         begin
    #             while a=b do
    #                 a := "pass";
    #             while not(e) do
    #                 b := c := 3.14;
    #         end"""
    #     expect = str(Program([
    #             FuncDecl(Id("main"),[],[],
    #             [While(BinaryOp("=",Id("a"),Id("b")),
    #                 [Assign(Id("a"),StringLiteral("pass"))]),
    #             While(UnaryOp("not",Id("e")),
    #                 [Assign(Id("c"),FloatLiteral("3.14")),
    #                 Assign(Id("b"),Id("c"))])])
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,369))

    # def test_while_1(self):
    #     input = """procedure main(); 
    #         begin
    #             while (a>b) do
    #                 a := "pass";
    #         end"""
    #     expect = str(Program([
    #             FuncDecl(Id("main"),[],[],
    #             [While(BinaryOp(">",Id("a"),Id("b")),
    #                 [Assign(Id("a"),StringLiteral("pass"))])])
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,370))

    # def test_assign_3(self):
    #     input = """procedure main(); 
    #         begin
    #         a := b := true;
    #         c := 5E-3;
    #         end"""
    #     expect = str(Program([
    #             FuncDecl(Id("main"),[],[],
    #                 [Assign(Id("b"),BooleanLiteral("true")),
    #                 Assign(Id("a"),Id("b")),
    #                 Assign(Id("c"),FloatLiteral(5E-3))])
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,371))

    # def test_assign_2(self):
    #     input = """procedure main(); 
    #         begin
    #         a := b := false;
    #         end"""
    #     expect = str(Program([
    #             FuncDecl(Id("main"),[],[],
    #                 [Assign(Id("b"),BooleanLiteral("false")),
    #                 Assign(Id("a"),Id("b"))])
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,372))

    # def test_assign_1(self):
    #     input = """procedure main(); 
    #         begin
    #         a := 5;
    #         end"""
    #     expect = str(Program([
    #             FuncDecl(Id("main"),[],[],
    #                 [Assign(Id("a"),IntLiteral(5))])
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,373))

    # def test_proc_func_var(self):
    #     input = """var a: array [2 .. 10] of integer;
    #         procedure main(); 
    #         var arr: array [-1 .. -3] of string;
    #         begin
    #         end 
    #         function foo(b: boolean): integer; 
    #         var c,d: real;
    #         begin
    #         end"""
    #     expect = str(Program([
    #             VarDecl(Id("a"),ArrayType(IntLiteral(2),IntLiteral(10),IntType())),
    #             FuncDecl(Id("main"),
    #                 [],
    #                 [VarDecl(Id("arr"),ArrayType(IntLiteral(-1),IntLiteral(-3),StringType()))],
    #                 []),
    #             FuncDecl(Id("foo"),
    #                 [VarDecl(Id("b"),BoolType())],
    #                 [VarDecl(Id("c"),FloatType()),VarDecl(Id("d"),FloatType())],
    #                 [],IntType())
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,374))

    # def test_proc_func(self):
    #     input = """procedure main(); 
    #         var arr: array [-1 .. -3] of string;
    #         begin
    #         end 
    #         function foo(b: boolean): integer; 
    #         var c,d: real;
    #         begin
    #         end"""
    #     expect = str(Program([
    #             FuncDecl(Id("main"),
    #                 [],
    #                 [VarDecl(Id("arr"),ArrayType(IntLiteral(-1),IntLiteral(-3),StringType()))],
    #                 []),
    #             FuncDecl(Id("foo"),
    #                 [VarDecl(Id("b"),BoolType())],
    #                 [VarDecl(Id("c"),FloatType()),VarDecl(Id("d"),FloatType())],
    #                 [],IntType())
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,375))

    # def test_proc_proc(self):
    #     input = """procedure main(); 
    #         var arr: array [-1 .. -3] of string;
    #         begin
    #         end 
    #         procedure foo(b: boolean); 
    #         begin
    #         end"""
    #     expect = str(Program([
    #             FuncDecl(Id("main"),
    #                 [],
    #                 [VarDecl(Id("arr"),ArrayType(IntLiteral(-1),IntLiteral(-3),StringType()))],
    #                 []),
    #             FuncDecl(Id("foo"),
    #                 [VarDecl(Id("b"),BoolType())],
    #                 [],
    #                 [])
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,376))

    # def test_proc_var_2(self):
    #     input = """var a,c: string;
    #                     d: integer;
    #         procedure main(b: boolean); 
    #         var arr: array [-1 .. -3] of string;
    #         begin
    #         end"""
    #     expect = str(Program([
    #             VarDecl(Id("a"),StringType()),
    #             VarDecl(Id("c"),StringType()),
    #             VarDecl(Id("d"),IntType()),
    #             FuncDecl(Id("main"),
    #                 [VarDecl(Id("b"),BoolType())],
    #                 [VarDecl(Id("arr"),ArrayType(IntLiteral(-1),IntLiteral(-3),StringType()))],
    #                 [])
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,377))

    # def test_proc_var_1(self):
    #     input = """var a: array [-1 .. -3] of string;
    #         procedure main(b: boolean); 
    #         begin
    #         end"""
    #     expect = str(Program([
    #             VarDecl(Id("a"),ArrayType(IntLiteral(-1),IntLiteral(-3),StringType())),
    #             FuncDecl(Id("main"),
    #                 [VarDecl(Id("b"),BoolType())],
    #                 [],
    #                 [])
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,378))

    # def test_proc_4(self):
    #     input = """procedure main(a: array [-1 .. -3] of string); 
    #         var b: boolean;
    #         begin
    #         end"""
    #     expect = str(Program([
    #             FuncDecl(Id("main"),
    #                 [VarDecl(Id("a"),ArrayType(IntLiteral(-1),IntLiteral(-3),StringType()))],
    #                 [VarDecl(Id("b"),BoolType())],
    #                 [])
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,379))

    # def test_proc_3(self):
    #     input = """procedure main(); 
    #         var c: array [-1 .. -3] of string;
    #         begin
    #         end"""
    #     expect = str(Program([
    #             FuncDecl(Id("main"),[],
    #                 [VarDecl(Id("c"),ArrayType(IntLiteral(-1),IntLiteral(-3),StringType()))],
    #                 [])
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,380))

    # def test_proc_2(self):
    #     input = """procedure main(a: integer); 
    #         begin
    #         end"""
    #     expect = str(Program([
    #             FuncDecl(Id("main"),
    #                 [VarDecl(Id("a"),IntType())],
    #                 [],[])
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,381))

    # def test_proc_1(self):
    #     input = """procedure main(); 
    #         begin
    #         end"""
    #     expect = str(Program([
    #             FuncDecl(Id("main"),[],[],[])
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,382))

    # def test_func_func(self):
    #     input = """function foo1():integer; 
    #         var arr: array [-1 .. -3] of string;
    #         begin
    #         end 
    #         function foo2(b: boolean):real; 
    #         begin
    #         end"""
    #     expect = str(Program([
    #             FuncDecl(Id("foo1"),
    #                 [],
    #                 [VarDecl(Id("arr"),ArrayType(IntLiteral(-1),IntLiteral(-3),StringType()))],
    #                 [],IntType()),
    #             FuncDecl(Id("foo2"),
    #                 [VarDecl(Id("b"),BoolType())],
    #                 [],
    #                 [],FloatType())
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,383))

    # def test_func_var_2(self):
    #     input = """var a,c: string;
    #                     d: integer;
    #         function foo(b: boolean):real; 
    #         var arr: array [-1 .. -3] of string;
    #         begin
    #         end"""
    #     expect = str(Program([
    #             VarDecl(Id("a"),StringType()),
    #             VarDecl(Id("c"),StringType()),
    #             VarDecl(Id("d"),IntType()),
    #             FuncDecl(Id("foo"),
    #                 [VarDecl(Id("b"),BoolType())],
    #                 [VarDecl(Id("arr"),ArrayType(IntLiteral(-1),IntLiteral(-3),StringType()))],
    #                 [],FloatType())
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,384))

    # def test_func_var_1(self):
    #     input = """var a: array [-1 .. -3] of string;
    #         function foo(b: boolean):real; 
    #         begin
    #         end"""
    #     expect = str(Program([
    #             VarDecl(Id("a"),ArrayType(IntLiteral(-1),IntLiteral(-3),StringType())),
    #             FuncDecl(Id("foo"),
    #                 [VarDecl(Id("b"),BoolType())],
    #                 [],
    #                 [],FloatType())
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,385))

    # def test_func_4(self):
    #     input = """function foo(a: array [-1 .. -3] of string):real; 
    #         var b: boolean;
    #         begin
    #         end"""
    #     expect = str(Program([
    #             FuncDecl(Id("foo"),
    #                 [VarDecl(Id("a"),ArrayType(IntLiteral(-1),IntLiteral(-3),StringType()))],
    #                 [VarDecl(Id("b"),BoolType())],
    #                 [],FloatType())
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,386))

    # def test_func_3(self):
    #     input = """function foo():real; 
    #         var c: array [-1 .. -3] of string;
    #         begin
    #         end"""
    #     expect = str(Program([
    #             FuncDecl(Id("foo"),[],
    #                 [VarDecl(Id("c"),ArrayType(IntLiteral(-1),IntLiteral(-3),StringType()))],
    #                 [],FloatType())
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,387))

    # def test_func_2(self):
    #     input = """function foo(a: integer):real; 
    #         begin
    #         end"""
    #     expect = str(Program([
    #             FuncDecl(Id("foo"),
    #                 [VarDecl(Id("a"),IntType())],
    #                 [],[],FloatType())
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,388))

    # def test_func_1(self):
    #     input = """function foo():INTEGER; 
    #         begin
    #         end"""
    #     expect = str(Program([
    #             FuncDecl(Id("foo"),[],[],[],IntType())
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,389))

    # def test_array_5(self):
    #     input = """var a:boolean;
    #                     b: integer;
    #                 var c: array [-8 .. 8] of real;"""
    #     expect = str(Program([
    #             VarDecl(Id("a"),BoolType()),
    #             VarDecl(Id("b"),IntType()),
    #             VarDecl(Id("c"),ArrayType(IntLiteral(-8),IntLiteral(8),FloatType()))
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,390))

    # def test_array_4(self):
    #     input = """var a:boolean;
    #                 var c: array [0 .. 8] of real;"""
    #     expect = str(Program([
    #             VarDecl(Id("a"),BoolType()),
    #             VarDecl(Id("c"),ArrayType(IntLiteral(0),IntLiteral(8),FloatType()))
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,391))

    # def test_array_3(self):
    #     input = """var a:array [-1 ..6] of real;
    #                     b: array [1 .. 5] of string;"""
    #     expect = str(Program([
    #             VarDecl(Id("a"),ArrayType(IntLiteral(-1),IntLiteral(6),FloatType())),
    #             VarDecl(Id("b"),ArrayType(IntLiteral(1),IntLiteral(5),StringType()))
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,392))

    # def test_array_2(self):
    #     input = """var a:array [-1 ..-10] of integer;"""
    #     expect = str(Program([
    #             VarDecl(Id("a"),ArrayType(IntLiteral(-1),IntLiteral(-10),IntType()))
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,393))

    # def test_array_1(self):
    #     input = """var a:array [1 .. 5] of integer;"""
    #     expect = str(Program([
    #             VarDecl(Id("a"),ArrayType(IntLiteral(1),IntLiteral(5),IntType()))
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,394))

    # def test_var_5(self):
    #     input = """var a: integer;
    #                 var b: string;
    #                     c,d: real;"""
    #     expect = str(Program([
    #             VarDecl(Id("a"),IntType()),
    #             VarDecl(Id("b"),StringType()),
    #             VarDecl(Id("c"),FloatType()),
    #             VarDecl(Id("d"),FloatType())
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,395))

    # def test_var_4(self):
    #     input = """var a: integer;
    #                 var b: string;"""
    #     expect = str(Program([
    #             VarDecl(Id("a"),IntType()),
    #             VarDecl(Id("b"),StringType())
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,396))

    # def test_var_3(self):
    #     input = """var a,b: boolean;
    #                     c: string;"""
    #     expect = str(Program([
    #             VarDecl(Id("a"),BoolType()),
    #             VarDecl(Id("b"),BoolType()),
    #             VarDecl(Id("c"),StringType())
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,397))

    # def test_var_2(self):
    #     input = """var a, b, c:real;"""
    #     expect = str(Program([
    #             VarDecl(Id("a"),FloatType()),
    #             VarDecl(Id("b"),FloatType()),
    #             VarDecl(Id("c"),FloatType())
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,398))

    # def test_var_1(self):
    #     input = """var a:integer;"""
    #     expect = str(Program([
    #             VarDecl(Id("a"),IntType())
    #             ]))
    #     self.assertTrue(TestAST.test(input,expect,399))
   