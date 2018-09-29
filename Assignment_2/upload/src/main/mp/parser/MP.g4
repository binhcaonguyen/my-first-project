/*
Cao Nguyen Binh
MSSV: 1610228
*/
grammar MP;

@lexer::header {
#MSSV 1610228
from lexererr import *
}

options{
	language=Python3;
}

program  : decl+ EOF;
decl: varDecl | funcDecl | procDecl;

varDecl: VAR varTypeDeclList SEMI;
varTypeDeclList: varTypeDecl (SEMI varTypeDecl)*;
varTypeDecl:  idList COLON dataType;
idList: IDENTIFIER (COMMA IDENTIFIER)*;
dataType: primType | arrayType ;
primType: BOOLEAN | INTEGER | REAL | STRING;

arrayType: ARRAY LQ upperBound DOUBLE_DOT lowerBound RQ OF primType;
upperBound: SUBOP? INTLIT;
lowerBound: SUBOP? INTLIT;

funcDecl: FUNCTION IDENTIFIER LB varTypeDeclList? RB COLON dataType SEMI (varDecl)? compoundStmt;

procDecl: PROCEDURE IDENTIFIER LB varTypeDeclList? RB SEMI (varDecl)? compoundStmt;



compoundStmt: BEGIN (stmtsList)?  END;

expr: expr (AND THEN| OR ELSE) expr1
	| expr1;
expr1: expr2 (EQUAL|NOT_EQUAL|GREATER|LESS|GREATER_OR_EQUAL|LESS_OR_EQUAL) expr2
 	| expr2;
expr2: expr2 (ADDOP|SUBOP|OR) expr3
	| expr3;
expr3: expr3 (DIVOP|MULOP|DIV|MOD|AND) expr4
	|expr4;
expr4: (NOT|ADDOP|SUBOP) expr4 | expr5;
expr5: LB expr RB
	| (INTLIT|FLOATLIT|IDENTIFIER|indexExpr|BOOLLIT|callExpr|STRINGLIT);




stmtsList: stmts+;
stmts: assignStmt|callStmt|returnStmt|whileStmt|withStmt|forStmt|breakStmt|continueStmt|ifStmt;
bodyIter: BEGIN stmtsList END
		| BEGIN stmts END
		| stmts;

assignStmt: (assignOperand ASSIGN)+ expr SEMI;
assignOperand: IDENTIFIER|indexExpr;

ifStmt: unMatchIfStmt|matchIfStmt;
matchIfStmt: IF expr THEN matchIfStmt ELSE matchIfStmt
			| (assignStmt|whileStmt|forStmt|withStmt|returnStmt|callStmt|breakStmt|continueStmt)
			| BEGIN (assignStmt|whileStmt|forStmt|withStmt|returnStmt|callStmt|breakStmt|continueStmt) END
			| BEGIN stmtsList END;
unMatchIfStmt: IF expr THEN ifStmt 
			| IF expr THEN matchIfStmt ELSE unMatchIfStmt;

whileStmt: WHILE expr DO bodyIter;

forStmt: FOR forCondition DO bodyIter;
forCondition: IDENTIFIER ASSIGN expr (TO|DOWNTO) expr;

breakStmt: BREAK SEMI;
continueStmt: CONTINUE SEMI;

returnStmt: RETURN (expr)? SEMI;

withStmt: WITH (withVarDecl)? DO bodyIter;
withVarDecl: varTypeDeclList SEMI
			| LB varTypeDeclList SEMI RB;

callStmt: invoExpr SEMI;
indexExpr: (IDENTIFIER|callExpr) LQ expr RQ;
invoExpr: IDENTIFIER LB (exprList)? RB;
callExpr: IDENTIFIER LB (exprList)? RB;
exprList: expr (COMMA expr)*;


/*	3.3 Token Set	*/
BREAK:	B R E A K;
CONTINUE:	C O N T I N U E;
FOR:	F O R;
TO:		T O;
DOWNTO: D O W N T O;
DO:		D O;
IF:		I F;
THEN:	T H E N;
ELSE:	E L S E;
RETURN:	R E T U R N;
WHILE:	W H I L E;
WITH: W I T H;
BEGIN:	B E G I N;
END:	E N D;
FUNCTION: F U N C T I O N;
PROCEDURE:	P R O C E D U R E;
VAR: 	V A R;
ARRAY:	A R R A Y;
OF:		O F;
REAL:	R E A L;
fragment TRUE:	T R U E;
fragment FALSE:	F A L S E;
BOOLEAN:	B O O L E A N;
INTEGER:	I N T E G E R;
STRING:		S T R I N G;
NOT:	N O T;
AND:	A N D;
OR:		O R;
DIV:	D I V;
MOD:	M O D;


ADDOP:	'+';
SUBOP:	'-';
MULOP:	'*';
DIVOP:	'/';
NOT_EQUAL:		'<>';
EQUAL:			'=';
LESS:		'<';
GREATER:	'>';
LESS_OR_EQUAL:	'<=';
GREATER_OR_EQUAL:	'>=';
ASSIGN: ':=';







	/*	3.2 Comments	*/
TRADITIONAL_BLOCK_COMMENT
	:	'(*'.*?'*)' -> skip ;
BLOCK_COMMENT
	:	'{' .*? '}'	-> 	skip ;
LINE_COMMENT
	:	'//' ~[\r\n]* -> skip ;
	

	/*	3.4 Separators	*/
LB: '(' ;
RB: ')' ;
LQ: '[';
RQ: ']';
COLON: ':' ;
SEMI: ';' ;
DOUBLE_DOT: '.'[ ]*'.';
COMMA: ',' ;
QUOTES: '"';

	/*	3.5 Literals	*/
INTLIT
	:  DIGIT_SEQUENCE;
FLOATLIT
    :   FRACTIONAL_CONSTANT EXPONENT_PART?
    |   DIGIT_SEQUENCE EXPONENT_PART
    ;
fragment FRACTIONAL_CONSTANT
    :   DIGIT_SEQUENCE? '.' DIGIT_SEQUENCE
    |   DIGIT_SEQUENCE '.';
fragment EXPONENT_PART	
	:  'e' SIGN? DIGIT_SEQUENCE
   	|  'E' SIGN? DIGIT_SEQUENCE;
fragment SIGN
	:	[+-];
fragment DIGIT_SEQUENCE
	:   DIGIT+;
fragment DIGIT
	:   [0-9];


BOOLLIT
	:	(TRUE|FALSE);
IDENTIFIER
	:	[a-zA-Z_][a-zA-Z0-9_]*;
STRINGLIT
	:	QUOTES STRING_CHARACTERS? QUOTES{
 self.text = self.text[1:-1]
 };
fragment STRING_CHARACTERS
	:	STRING_CHARACTER+;
fragment STRING_CHARACTER
	:	~[\b\f\r\n\t'"\\]
	|	ESCAPE_SEQUENCE;
fragment ESCAPE_SEQUENCE
 	:	'\\' [bfrnt'"\\];


    
// case insensitive chars
fragment A:('A'|'a');
fragment B:('b'|'B');
fragment C:('c'|'C');
fragment D:('d'|'D');
fragment E:('e'|'E');
fragment F:('f'|'F');
fragment G:('g'|'G');
fragment H:('h'|'H');
fragment I:('i'|'I');
fragment J:('j'|'J');
fragment K:('k'|'K');
fragment L:('l'|'L');
fragment M:('m'|'M');
fragment N:('n'|'N');
fragment O:('o'|'O');
fragment P:('p'|'P');
fragment Q:('q'|'Q');
fragment R:('r'|'R');
fragment S:('s'|'S');
fragment T:('t'|'T');
fragment U:('u'|'U');
fragment V:('v'|'V');
fragment W:('w'|'W');
fragment X:('x'|'X');
fragment Y:('y'|'Y');
fragment Z:('z'|'Z');



WS : [ \t\f\r\n]+ -> skip ; // skip spaces, tabs, newlines
UNCLOSE_STRING: ('"' STRING_CHARACTER*'\n'{raise UncloseString(self.text[1:-1])}|
				 '"' STRING_CHARACTER*EOF{raise UncloseString(self.text[1:])});
ILLEGAL_ESCAPE: '"' STRING_CHARACTER* ('\\' ~["'rbtf\\]|~'"' |'\''|'\\'EOF){raise IllegalEscape(self.text[1:])};

ERROR_CHAR: . {raise ErrorToken(self.text)};