# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3<")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\3\2\2\2\5\3\3\2\2\2\2")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'class'", "'final'", "'static'", "'extends'", 
                     "'void'", "'main'", "'new'", "'return'", "'true'", 
                     "'false'", "'for'", "'then'", "'nil'", "'if'", "'downto'", 
                     "'to'", "'break'", "'else'", "'continue'", "'this'", 
                     "','", "';'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "'='", "'+'", "'-'", "'*'", "'/'", "'\\'", "':='", 
                     "'<='", "'>='", "'!='", "'=='", "'<'", "'>'", "'%'", 
                     "'.'", "'&&'", "'!'", "'||'", "'^'" ]

    symbolicNames = [ "<INVALID>", "FLOATLIT", "INTLIT", "STRING_LIT", "TYPE", 
                      "CLASS", "FINAL", "STATIC", "EXTEND", "VOID", "MAIN", 
                      "NEW", "RETURN", "TRUE", "FALSE", "FOR", "THEN", "NIL", 
                      "IF", "DOWNTO", "TO", "BREAK", "ELSE", "CONTINUE", 
                      "THIS", "COMMA", "SIMI", "LP", "RP", "LB", "RB", "LSB", 
                      "RSB", "EQUATION", "ADD", "SUB", "MUL", "INT_DIV", 
                      "FLOAT_DIV", "ASSIGN", "LOWER_E", "GREATER_E", "NOT_EQUALS", 
                      "EQUALS", "LOWER", "GREATER", "PERCENT", "DOT", "AND", 
                      "NOT", "OR", "CONCAT", "ID", "BLOCK_COMMENT", "LINE_COMMENT", 
                      "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    FLOATLIT=1
    INTLIT=2
    STRING_LIT=3
    TYPE=4
    CLASS=5
    FINAL=6
    STATIC=7
    EXTEND=8
    VOID=9
    MAIN=10
    NEW=11
    RETURN=12
    TRUE=13
    FALSE=14
    FOR=15
    THEN=16
    NIL=17
    IF=18
    DOWNTO=19
    TO=20
    BREAK=21
    ELSE=22
    CONTINUE=23
    THIS=24
    COMMA=25
    SIMI=26
    LP=27
    RP=28
    LB=29
    RB=30
    LSB=31
    RSB=32
    EQUATION=33
    ADD=34
    SUB=35
    MUL=36
    INT_DIV=37
    FLOAT_DIV=38
    ASSIGN=39
    LOWER_E=40
    GREATER_E=41
    NOT_EQUALS=42
    EQUALS=43
    LOWER=44
    GREATER=45
    PERCENT=46
    DOT=47
    AND=48
    NOT=49
    OR=50
    CONCAT=51
    ID=52
    BLOCK_COMMENT=53
    LINE_COMMENT=54
    WS=55
    UNCLOSE_STRING=56
    ILLEGAL_ESCAPE=57
    ERROR_CHAR=58

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





