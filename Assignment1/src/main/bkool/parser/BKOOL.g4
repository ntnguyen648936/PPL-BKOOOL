/*
** - Author: Nguyen Thanh Quoc Minh
** - ID: 1752349
*/

grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : classDecl+ EOF ;

// CLASS DECLARE

classDecl
	: CLASS ID (EXTENDS ID)? LCB memberDecl* RCB
	;

memberDecl
	: attrDecl 
	| methodDecl
	;

// ATTRIBUTE MEMBER

attrDecl
	: varDecl SIMI
	| preAttrDecl varDecl SIMI
	; 

preAttrDecl
	: FINAL
	| STATIC
	| STATIC FINAL
	| FINAL STATIC
	;

varDecl
	: bkoolType oneVarDecl listVarDecl
	; 

oneVarDecl
	: ID 
	| ID declAssignment
	;

listVarDecl
	: COMMA oneVarDecl listVarDecl 
	| 
	;

declAssignment
	: EQUATION expr
	| EQUATION arrayLit
	;

// METHOD MEMBER

methodDecl
	: preMethodDecl ID LP paramDecl RP blockStmt
	| preMethodDecl ID LP RP blockStmt
	| ID LP paramDecl RP blockStmt
	| ID LP RP blockStmt
	; 

preMethodDecl
	: bkoolType
	| STATIC bkoolType
	;

paramDecl
	: oneParamDecl listParamDecl
	;

listParamDecl
	: SIMI oneParamDecl listParamDecl 
	|
	;

oneParamDecl
	: bkoolType ID listID
	;

listID
	: COMMA ID listID
	|
	;

// STATEMENT

statement
	: blockStmt
	| ifStmt
	| forStmt
	| funcCallStmt
	| assignStmt 
	| breakStmt
	| continueStmt
	| returnStmt
	;

blockStmt
	: LCB varDeclStmt* statement* RCB
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
*/

varDeclStmt
	: varDecl SIMI
	| FINAL varDecl SIMI
	;

assignStmt
	: lhs ASSIGN expr SIMI
	;

lhs
	: indexExpr
	| termMemAccess DOT ID
	| ID
	;

ifStmt
	: IF expr THEN statement (ELSE statement)*
	;

forStmt
	: FOR ID ASSIGN expr TO_DOWNTO expr DO statement
	;

funcCallStmt
	: ID LP listExpr RP SIMI
	| memAccess DOT ID LP listExpr RP SIMI
	; // Method invocation

memAccess
	: memAccess DOT ID (LP listExpr RP)?
	| termObjCreation
	;

returnStmt
	: RETURN expr SIMI
	;

continueStmt
	: CONTINUE SIMI
	;

breakStmt
	: BREAK SIMI
	;


// EXPRESSION

expr
	: term0 (LOWER | GREATER | LOWER_E | GREATER_E) term0
	| term0
	; // < > <= >=

term0
	: term1 (EQUALS | NOT_EQUALS) term1
	| term1
	; // == !=

term1
	: term1 (AND | OR) term2
	| term2
	; // && || @left
	
term2
	: term2 (PLUS | MINUS) term3
	| term3
	; // + - (binary) @left

term3
	: term3 (MUL | INT_DIV | FLOAT_DIV | PERCENT) term4
	| term4
	; //  * / \ & @left

term4
	: term4 CONCAT term5
	| term5
	; // ^ (concat string) @left

term5
	: NOT term5
	| term6
	; // ! (not) @right

term6
	: (PLUS | MINUS) term6
	| termIndexExpr
	; // + - (unary) @right

termIndexExpr
	: indexExpr
	| termMemAccess
	; // INDEX expr
	
indexExpr
	: termMemAccess LSB expr RSB
	;

termMemAccess
	: termMemAccess DOT ID (LP listExpr RP)?
	| termObjCreation
	; // Member access @left

termObjCreation
	: NEW ID LP listExpr RP
	| operands
	; // Object Creation @right
	
operands
	: LP expr RP
	| funcCallExpr
	| INT_LIT 
	| FLOAT_LIT 
	| BOOL_LIT
	| STRING_LIT
	| NIL
	| THIS
	| ID
	;

funcCallExpr
	: ID LP listExpr RP
	; 

listExpr
	: expr nextExpr
	|
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
	| FLOAT_LIT 
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

bkoolType
	: PRIMITIVE
	| arrayType
	| ID
	;

// ----------- TOKENS ---------------------------------------------

FLOAT_LIT: DIGIT+ (DECIMAL | EXPONENT | DECIMAL EXPONENT);
fragment DECIMAL: DOT DIGIT*; // ditgit after decimal point is optinal
fragment EXPONENT: [Ee] ('+'|'-')? DIGIT+;

INT_LIT
	: DIGIT+
	;
	
fragment DIGIT: [0-9];

STRING_LIT: '"' STR_CHAR* '"'{ self.text = self.text[1:-1] };
BOOL_LIT: 'true' | 'false';

PRIMITIVE
	: 'int' 
	| 'float' 
	| 'boolean' 
	| 'string'
	| 'void'
	;

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
THIS: 'this';

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
		possible = ['\n', '\r']
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
fragment STR_CHAR: ~[\n\r"\\] | ESC_ACCEPT ;

fragment ESC_ACCEPT: '\\' [btnfr"\\] ;

fragment ESC_ILLEGAL: '\\' ~[btnfr"\\] ;

ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	}
	;
