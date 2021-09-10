grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : classDecl+ EOF ;

// CLASS DECLAR

classDecl
	: CLASS ID classDeclExtension? LCB classBody RCB
	;

classDeclExtension
	: EXTENDS ID
	;

classBody
	: members*
	; // nullable list of members 

members
	: attrDecl 
	| methodDecl
	;

// ATTRIBUTE MEMBER

attrDecl
	: attrPreDecl? varDeclStmt
	; 

attrPreDecl
	: STATIC FINAL? 
	| FINAL? STATIC
	;

oneAttr
	: ID declAssignment?
	;

listAttr
	: COMMA oneAttr listAttr 
	| 
	;

declAssignment
	: EQUATION expr
	| EQUATION arrayLit
	;

// METHOD MEMBER

methodDecl
	: preMethodDecl ID LP paramDecl? RP blockStmt
	| ID LP paramDecl? RP blockStmt
	; 

preMethodDecl
	: langTYPE
	| VOID
	| STATIC langTYPE
	| STATIC VOID
	;

paramDecl
	: langTYPE oneAttr listAttr listParamDecl
	;

listParamDecl
	: SIMI langTYPE oneAttr listAttr listParamDecl |
	;


// STATEMENT

blockStmt
	: LCB singleStmt* RCB
	;

varDeclStmt
	: FINAL? langTYPE oneAttr listAttr SIMI
	;

assignStmt
	: lhs ASSIGN expr SIMI
	;

lhs
	: scalarVar
	| indexExpr
	;

scalarVar
	: term_MemAccess DOT ID
	| ID
	;


singleStmt
	: IF expr THEN statement ELSE statement
	| IF expr THEN statement
	| otherStmt
	;

/*
singleStmt
	: matchStmt
	| unmatchStmt
	;

matchStmt
	: IF expr THEN matchStmt ELSE matchStmt
	| otherStmt
	;

unmatchStmt
	: IF expr THEN statement
	| IF expr THEN matchStmt ELSE unmatchStmt
	;

otherStmt
	: forStmt
	| attrDecl 
	| assignStmt 
	| funcCallStmt
	| retStmt
	;
*/
forStmt
	: FOR scalarVar ASSIGN expr TO_DOWNTO expr DO statement
	;

// Method invocation
funcCallStmt
	: funcCallExpr SIMI
	| term_MemAccess DOT funcCallExpr SIMI
	; 

retStmt
	: RETURN expr SIMI
	;

continueStmt
	: CONTINUE SIMI
	;

breakStmt
	: BREAK SIMI
	;

statement
	: blockStmt
	| singleStmt
	;

otherStmt
	: forStmt
	| varDeclStmt 
	| assignStmt 
	| funcCallStmt
	| breakStmt
	| continueStmt
	| retStmt
	;

// EXPRESSION

expr
	: term_0 (LOWER | GREATER | LOWER_E | GREATER_E) term_0
	| term_0
	; // < > <= >=

term_0
	: term_1 (EQUALS | NOT_EQUALS) term_1
	| term_1
	; // == !=

term_1
	: term_1 (AND | OR) term_2
	| term_2
	; // && || @left
	
term_2
	: term_2 (PLUS | MINUS) term_3
	| term_3
	; // + - (binary) @left

term_3
	: term_3 (MUL | INT_DIV | FLOAT_DIV | PERCENT) term_4
	| term_4
	; //  * / \ & @left

term_4
	: term_4 CONCAT term_5
	| term_5
	; // ^ (concat string) @left

term_5
	: NOT term_5
	| term_6
	; // ! (not) @right

term_6
	: (PLUS | MINUS) term_6
	| term_IndexExpr
	; // + - (unary) @right

term_IndexExpr
	: indexExpr
	| term_MemAccess
	; // INDEX expr

indexExpr
	: ID LSB expr RSB
	| funcCallExpr LSB expr RSB
	| term_MemAccess DOT ID LSB expr RSB
	| term_MemAccess DOT funcCallExpr LSB expr RSB
	;

term_MemAccess
	: term_MemAccess DOT ID 
	| term_MemAccess DOT funcCallExpr
	| term_ObjCreation
	; // Member access @left

term_ObjCreation
	: NEW ID LP listExpr? RP
	| operands
	; // Object Creation @right
	
operands
	: LP expr RP
	| INT_LIT 
	| FLOATLIT 
	| BOOL_LIT
	| STRING_LIT
	| NIL
	| funcCallExpr
	| ID
	;

funcCallExpr
	: ID LP listExpr? RP
	; 

listExpr
	: expr nextExpr
	;

nextExpr
	: COMMA expr nextExpr 
	|
	;

// Literals
/*
intArray: LCB INT_LIT listIntLit RCB;
listIntLit: COMMA INT_LIT listIntLit |;

floatArray: LCB FLOAT_LIT listFloatLit RCB;
listFloatLit: COMMA FLOAT_LIT listFloatLit |;

stringArray: LCB STRING_LIT listStringLit RCB;
listStringLit: COMMA STRING_LIT listStringLit | ;

boolArray: LCB BOOLEAN_LIT listBoolLit RCB;
listBoolLit: COMMA BOOLEAN_LIT listBoolLit |;

arrayLit
	: intArray
	| floatArray
	| stringArray
	| boolArray
	;
*/

arrayLit
	: LCB primLit listOfPrimLit RCB
	;
	
listOfPrimLit
	: COMMA primLit listOfPrimLit 
	|
	; 

primLit	
	: INT_LIT 
	| STRING_LIT 
	| FLOATLIT 
	| BOOL_LIT 
	;

literal
	: primLit
	| arrayLit
	;

arrayType
	: PRIMITIVE LSB INT_LIT RSB
	| ID LSB INT_LIT RSB
	;

langTYPE
	: PRIMITIVE
	| arrayType
	| ID
	;

// ----------- TOKENS ---------------------------------------------

FLOATLIT: DIGIT+ (DECIMAL | EXPONENT | DECIMAL EXPONENT);
fragment DECIMAL: DOT DIGIT*; // ditgit after decimal point is optinal
fragment EXPONENT: [Ee] ('+'|'-')? DIGIT+;

INT_LIT: DIGIT+;
fragment DIGIT: [0-9];

STRING_LIT: '"' STR_CHAR* '"';
BOOL_LIT: 'true' | 'false';

PRIMITIVE
	: 'int' 
	| 'float' 
	| 'boolean' 
	| 'string'
	;

VOID: 'void';
CLASS: 'class';
FINAL: 'final';
STATIC: 'static';
EXTENDS: 'extends';
//MAIN: 'main';
NEW: 'new';
RETURN: 'return';
FOR: 'for';
THEN: 'then';
NIL: 'nil';
IF: 'if';
TO_DOWNTO: 'to' | 'downto';
DO: 'do';
BREAK: 'break';
ELSE: 'else';
CONTINUE: 'continue';
//THIS: 'this';

COMMA: ',';
SIMI: ';';
LP: '(';
RP: ')';
LCB: '{';
RCB: '}';
LSB: '[';
RSB: ']';
EQUATION: '=';
PLUS: '+';
MINUS: '-';
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
