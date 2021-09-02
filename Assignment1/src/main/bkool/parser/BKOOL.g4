grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : decl+ EOF ;

decl: vardecl | funcdecl;

vardecl: TYPE listVardecl SIMI;

funcdecl: TYPE ID LP funcDeclParams RP body;

funcDeclParams: TYPE listVardecl listFuncDeclParams | ;

listFuncDeclParams: SIMI TYPE listVardecl listFuncDeclParams |;
listVardecl: ID COMMA listVardecl | ID;


TYPE: 'int' | 'float';
FINAL: 'final';
STATIC: 'static';

FLOATLIT: INTLIT DOT INTLIT;
INTLIT: [1-9][0-9]* | [0];

body: LB listStmt retStmt RB;

listStmt: stmt listStmt | ;
funcCall: ID LP funcCallParams RP; 

expr: expr DIV term | expr MUL term | term;
term: factor ADD term | factor SUB factor | factor;
factor: LP expr RP | INTLIT | FLOATLIT | funcCall | ID;

assignment: ID ASSIGN expr SIMI;

funcCallStmt: funcCall SIMI; 

retStmt: 'return' expr SIMI;

funcCallParams: expr listFuncCallParams | ;
listFuncCallParams: COMMA expr listFuncCallParams | ;


stmt: vardecl | assignment | funcCallStmt;

ID: [a-zA-Z]+;

COMMA: ',';
DOT: '.';
SIMI: ';';
LP: '(';
RP: ')';
LB: '{';
RB: '}';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
ASSIGN: '=';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: . {raise ErrorToken(self.text)};
//UNCLOSE_STRING: .;
//ILLEGAL_ESCAPE: .;