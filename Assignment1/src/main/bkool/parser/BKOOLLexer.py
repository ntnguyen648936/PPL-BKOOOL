# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25")
        buf.write("o\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\5\39\n\3\3\4\3\4\3\4\3\4\3\5\3\5\7\5")
        buf.write("A\n\5\f\5\16\5D\13\5\3\5\5\5G\n\5\3\6\6\6J\n\6\r\6\16")
        buf.write("\6K\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f")
        buf.write("\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22")
        buf.write("\3\22\3\23\6\23g\n\23\r\23\16\23h\3\23\3\23\3\24\3\24")
        buf.write("\3\24\2\2\25\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25\3")
        buf.write("\2\7\3\2\63;\3\2\62;\3\2\62\62\4\2C\\c|\5\2\13\f\17\17")
        buf.write("\"\"\2s\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\3)\3\2\2\2\58\3\2\2\2\7")
        buf.write(":\3\2\2\2\tF\3\2\2\2\13I\3\2\2\2\rM\3\2\2\2\17O\3\2\2")
        buf.write("\2\21Q\3\2\2\2\23S\3\2\2\2\25U\3\2\2\2\27W\3\2\2\2\31")
        buf.write("Y\3\2\2\2\33[\3\2\2\2\35]\3\2\2\2\37_\3\2\2\2!a\3\2\2")
        buf.write("\2#c\3\2\2\2%f\3\2\2\2\'l\3\2\2\2)*\7t\2\2*+\7g\2\2+,")
        buf.write("\7v\2\2,-\7w\2\2-.\7t\2\2./\7p\2\2/\4\3\2\2\2\60\61\7")
        buf.write("k\2\2\61\62\7p\2\2\629\7v\2\2\63\64\7h\2\2\64\65\7n\2")
        buf.write("\2\65\66\7q\2\2\66\67\7c\2\2\679\7v\2\28\60\3\2\2\28\63")
        buf.write("\3\2\2\29\6\3\2\2\2:;\5\t\5\2;<\5\17\b\2<=\5\t\5\2=\b")
        buf.write("\3\2\2\2>B\t\2\2\2?A\t\3\2\2@?\3\2\2\2AD\3\2\2\2B@\3\2")
        buf.write("\2\2BC\3\2\2\2CG\3\2\2\2DB\3\2\2\2EG\t\4\2\2F>\3\2\2\2")
        buf.write("FE\3\2\2\2G\n\3\2\2\2HJ\t\5\2\2IH\3\2\2\2JK\3\2\2\2KI")
        buf.write("\3\2\2\2KL\3\2\2\2L\f\3\2\2\2MN\7.\2\2N\16\3\2\2\2OP\7")
        buf.write("\60\2\2P\20\3\2\2\2QR\7=\2\2R\22\3\2\2\2ST\7*\2\2T\24")
        buf.write("\3\2\2\2UV\7+\2\2V\26\3\2\2\2WX\7}\2\2X\30\3\2\2\2YZ\7")
        buf.write("\177\2\2Z\32\3\2\2\2[\\\7-\2\2\\\34\3\2\2\2]^\7/\2\2^")
        buf.write("\36\3\2\2\2_`\7,\2\2` \3\2\2\2ab\7\61\2\2b\"\3\2\2\2c")
        buf.write("d\7?\2\2d$\3\2\2\2eg\t\6\2\2fe\3\2\2\2gh\3\2\2\2hf\3\2")
        buf.write("\2\2hi\3\2\2\2ij\3\2\2\2jk\b\23\2\2k&\3\2\2\2lm\13\2\2")
        buf.write("\2mn\b\24\3\2n(\3\2\2\2\b\28BFKh\4\b\2\2\3\24\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    TYPE = 2
    FLOATLIT = 3
    INTLIT = 4
    ID = 5
    COMMA = 6
    DOT = 7
    SIMI = 8
    LP = 9
    RP = 10
    LB = 11
    RB = 12
    ADD = 13
    SUB = 14
    MUL = 15
    DIV = 16
    ASSIGN = 17
    WS = 18
    ERROR_CHAR = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'return'", "','", "'.'", "';'", "'('", "')'", "'{'", "'}'", 
            "'+'", "'-'", "'*'", "'/'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "TYPE", "FLOATLIT", "INTLIT", "ID", "COMMA", "DOT", "SIMI", 
            "LP", "RP", "LB", "RB", "ADD", "SUB", "MUL", "DIV", "ASSIGN", 
            "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "TYPE", "FLOATLIT", "INTLIT", "ID", "COMMA", "DOT", 
                  "SIMI", "LP", "RP", "LB", "RB", "ADD", "SUB", "MUL", "DIV", 
                  "ASSIGN", "WS", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[18] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


