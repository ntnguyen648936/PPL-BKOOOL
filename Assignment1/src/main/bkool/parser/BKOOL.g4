grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : ;// classDecl+ EOF ;
/*
classDecl: CLASS ID classDeclExtension LB classBody RB;

classDeclExtension: EXTEND ID | ;

classBody: members*; // nullable list of members 

members: attrDecl | methodDecl;

attrDecl: STATIC? FINAL? TYPE listAttrDecl SIMI; // 
methodDecl: STATIC (returnMethodDecl | voidMethodDecl);
returnMethodDecl: TYPE ID LP paramDecl RP returnBody;
voidMethodDecl: VOID ID LP paramDecl RP noReturnBody;

paramDecl: TYPE listAttrDecl listParamDecl | ;

listParamDecl: SIMI TYPE listAttrDecl listParamDecl |;
listAttrDecl: ID declAssignment COMMA listAttrDecl | ID;

declAssignment: EQUATION expr | ;

returnBody: LB listStmt retStmt RB;
noReturnBody: LB listStmt RB;

listStmt: stmt listStmt | ;
funcCall: ID LP funcCallParams RP; 

expr: expr DIV term | expr MUL term | term;
term: factor ADD term | factor SUB factor | factor;
factor: LP expr RP | INTLIT | FLOATLIT | funcCall | ID;

assignment: ID ASSIGN expr SIMI;

funcCallStmt: funcCall SIMI; 

retStmt: RETURN expr SIMI;

funcCallParams: expr listFuncCallParams | ;
listFuncCallParams: COMMA expr listFuncCallParams | ;
stmt: attrDecl | assignment | funcCallStmt;
*/

//literal: intLit | stringLit | floatLit | boolLit | arrayLit;

FLOATLIT: DIGIT+ (DECIMAL | EXPONENT | DECIMAL EXPONENT);
fragment DECIMAL: DOT DIGIT*; // ditgit after decimal point is optinal
fragment EXPONENT: [Ee] ('+'|'-')? DIGIT+;
INTLIT: DIGIT+;
fragment DIGIT: [0-9];

STRING_LIT: '"' STR_CHAR* '"';

TYPE: 'int' | 'float' | 'boolean' | 'string';
CLASS: 'class';
FINAL: 'final';
STATIC: 'static';
EXTEND: 'extends';
VOID: 'void';
MAIN: 'main';
NEW: 'new';
RETURN: 'return';
TRUE: 'true';
FALSE: 'false';
FOR: 'for';
THEN: 'then';
NIL: 'nil';
IF: 'if';
DOWNTO: 'downto';
TO: 'to';
BREAK: 'break';
ELSE: 'else';
CONTINUE: 'continue';
THIS: 'this';



COMMA: ',';
SIMI: ';';
LP: '(';
RP: ')';
LB: '{';
RB: '}';
LSB: '[';
RSB: ']';
EQUATION: '=';
ADD: '+';
SUB: '-';
MUL: '*';
INT_DIV: '/';
FLOAT_DIV: '\\';
ASSIGN: ':=';
LOWER_E: '<=';
GREATER_E: '>=';
NOT_EQUALS: '!=';
EQUALS : '==' ;
LOWER : '<' ;
GREATER : '>' ;
PERCENT: '%';
DOT: '.';
AND: '&&';
NOT: '!';
OR: '||';
CONCAT: '^';

ID: [_a-zA-Z][_a-zA-Z0-9]*;

// Skip comments
BLOCK_COMMENT: '/*' .*? '*/' -> skip ;
LINE_COMMENT : '#' ~[\r\n]* ([\r\n]|EOF) -> skip ;


WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines


UNCLOSE_STRING: '"' STR_CHAR* 
	{
		y = str(self.text)
		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
		if y[-1] in possible:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:])
	}
	;
ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	}
	;
fragment STR_CHAR: ~[\b\t\n\f\r"\\] | ESC_SEQ ;

fragment ESC_SEQ: '\\' ([btnfr"\\] | '\'') ;

fragment ESC_ILLEGAL: '\\' (~[btnfr"\\] | ~'\\') ;

ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	}
	;
