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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01bc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\6\2\u0085")
        buf.write("\n\2\r\2\16\2\u0086\3\2\3\2\3\2\3\2\3\2\5\2\u008e\n\2")
        buf.write("\3\3\3\3\7\3\u0092\n\3\f\3\16\3\u0095\13\3\3\4\3\4\5\4")
        buf.write("\u0099\n\4\3\4\6\4\u009c\n\4\r\4\16\4\u009d\3\5\6\5\u00a1")
        buf.write("\n\5\r\5\16\5\u00a2\3\6\3\6\3\7\3\7\7\7\u00a9\n\7\f\7")
        buf.write("\16\7\u00ac\13\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\5\b\u00c5\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3")
        buf.write("$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3+\3")
        buf.write(",\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\67\3\67\38\38\78\u0174\n8\f8\168\u0177\138\39")
        buf.write("\39\39\39\79\u017d\n9\f9\169\u0180\139\39\39\39\39\39")
        buf.write("\3:\3:\7:\u0189\n:\f:\16:\u018c\13:\3:\5:\u018f\n:\3:")
        buf.write("\3:\3;\6;\u0194\n;\r;\16;\u0195\3;\3;\3<\3<\7<\u019c\n")
        buf.write("<\f<\16<\u019f\13<\3<\3<\3=\3=\7=\u01a5\n=\f=\16=\u01a8")
        buf.write("\13=\3=\3=\3=\3>\3>\5>\u01af\n>\3?\3?\5?\u01b3\n?\3@\3")
        buf.write("@\3@\5@\u01b8\n@\3A\3A\3A\3\u017e\2B\3\3\5\2\7\2\t\4\13")
        buf.write("\2\r\5\17\6\21\7\23\b\25\t\27\n\31\13\33\f\35\r\37\16")
        buf.write("!\17#\20%\21\'\22)\23+\24-\25/\26\61\27\63\30\65\31\67")
        buf.write("\329\33;\34=\35?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-")
        buf.write("_.a/c\60e\61g\62i\63k\64m\65o\66q\67s8u9w:y;{\2}\2\177")
        buf.write("\2\u0081<\3\2\16\4\2GGgg\4\2--//\3\2\62;\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\4\2\f\f\17\17\4\3\f\f\17\17\5\2\13\f\16")
        buf.write("\17\"\"\6\2\n\f\16\17$$^^\n\2$$))^^ddhhppttvv\t\2$$^^")
        buf.write("ddhhppttvv\3\2^^\2\u01c8\2\3\3\2\2\2\2\t\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2\u0081\3\2\2\2")
        buf.write("\3\u0084\3\2\2\2\5\u008f\3\2\2\2\7\u0096\3\2\2\2\t\u00a0")
        buf.write("\3\2\2\2\13\u00a4\3\2\2\2\r\u00a6\3\2\2\2\17\u00c4\3\2")
        buf.write("\2\2\21\u00c6\3\2\2\2\23\u00cc\3\2\2\2\25\u00d2\3\2\2")
        buf.write("\2\27\u00d9\3\2\2\2\31\u00e1\3\2\2\2\33\u00e6\3\2\2\2")
        buf.write("\35\u00eb\3\2\2\2\37\u00ef\3\2\2\2!\u00f6\3\2\2\2#\u00fb")
        buf.write("\3\2\2\2%\u0101\3\2\2\2\'\u0105\3\2\2\2)\u010a\3\2\2\2")
        buf.write("+\u010e\3\2\2\2-\u0111\3\2\2\2/\u0118\3\2\2\2\61\u011b")
        buf.write("\3\2\2\2\63\u0121\3\2\2\2\65\u0126\3\2\2\2\67\u012f\3")
        buf.write("\2\2\29\u0134\3\2\2\2;\u0136\3\2\2\2=\u0138\3\2\2\2?\u013a")
        buf.write("\3\2\2\2A\u013c\3\2\2\2C\u013e\3\2\2\2E\u0140\3\2\2\2")
        buf.write("G\u0142\3\2\2\2I\u0144\3\2\2\2K\u0146\3\2\2\2M\u0148\3")
        buf.write("\2\2\2O\u014a\3\2\2\2Q\u014c\3\2\2\2S\u014e\3\2\2\2U\u0150")
        buf.write("\3\2\2\2W\u0153\3\2\2\2Y\u0156\3\2\2\2[\u0159\3\2\2\2")
        buf.write("]\u015c\3\2\2\2_\u015f\3\2\2\2a\u0161\3\2\2\2c\u0163\3")
        buf.write("\2\2\2e\u0165\3\2\2\2g\u0167\3\2\2\2i\u016a\3\2\2\2k\u016c")
        buf.write("\3\2\2\2m\u016f\3\2\2\2o\u0171\3\2\2\2q\u0178\3\2\2\2")
        buf.write("s\u0186\3\2\2\2u\u0193\3\2\2\2w\u0199\3\2\2\2y\u01a2\3")
        buf.write("\2\2\2{\u01ae\3\2\2\2}\u01b0\3\2\2\2\177\u01b4\3\2\2\2")
        buf.write("\u0081\u01b9\3\2\2\2\u0083\u0085\5\13\6\2\u0084\u0083")
        buf.write("\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0084\3\2\2\2\u0086")
        buf.write("\u0087\3\2\2\2\u0087\u008d\3\2\2\2\u0088\u008e\5\5\3\2")
        buf.write("\u0089\u008e\5\7\4\2\u008a\u008b\5\5\3\2\u008b\u008c\5")
        buf.write("\7\4\2\u008c\u008e\3\2\2\2\u008d\u0088\3\2\2\2\u008d\u0089")
        buf.write("\3\2\2\2\u008d\u008a\3\2\2\2\u008e\4\3\2\2\2\u008f\u0093")
        buf.write("\5e\63\2\u0090\u0092\5\13\6\2\u0091\u0090\3\2\2\2\u0092")
        buf.write("\u0095\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2")
        buf.write("\u0094\6\3\2\2\2\u0095\u0093\3\2\2\2\u0096\u0098\t\2\2")
        buf.write("\2\u0097\u0099\t\3\2\2\u0098\u0097\3\2\2\2\u0098\u0099")
        buf.write("\3\2\2\2\u0099\u009b\3\2\2\2\u009a\u009c\5\13\6\2\u009b")
        buf.write("\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009b\3\2\2\2")
        buf.write("\u009d\u009e\3\2\2\2\u009e\b\3\2\2\2\u009f\u00a1\5\13")
        buf.write("\6\2\u00a0\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a0")
        buf.write("\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\n\3\2\2\2\u00a4\u00a5")
        buf.write("\t\4\2\2\u00a5\f\3\2\2\2\u00a6\u00aa\7$\2\2\u00a7\u00a9")
        buf.write("\5{>\2\u00a8\u00a7\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa\u00a8")
        buf.write("\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ad\3\2\2\2\u00ac")
        buf.write("\u00aa\3\2\2\2\u00ad\u00ae\7$\2\2\u00ae\16\3\2\2\2\u00af")
        buf.write("\u00b0\7k\2\2\u00b0\u00b1\7p\2\2\u00b1\u00c5\7v\2\2\u00b2")
        buf.write("\u00b3\7h\2\2\u00b3\u00b4\7n\2\2\u00b4\u00b5\7q\2\2\u00b5")
        buf.write("\u00b6\7c\2\2\u00b6\u00c5\7v\2\2\u00b7\u00b8\7d\2\2\u00b8")
        buf.write("\u00b9\7q\2\2\u00b9\u00ba\7q\2\2\u00ba\u00bb\7n\2\2\u00bb")
        buf.write("\u00bc\7g\2\2\u00bc\u00bd\7c\2\2\u00bd\u00c5\7p\2\2\u00be")
        buf.write("\u00bf\7u\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1\7t\2\2\u00c1")
        buf.write("\u00c2\7k\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c5\7i\2\2\u00c4")
        buf.write("\u00af\3\2\2\2\u00c4\u00b2\3\2\2\2\u00c4\u00b7\3\2\2\2")
        buf.write("\u00c4\u00be\3\2\2\2\u00c5\20\3\2\2\2\u00c6\u00c7\7e\2")
        buf.write("\2\u00c7\u00c8\7n\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca\7")
        buf.write("u\2\2\u00ca\u00cb\7u\2\2\u00cb\22\3\2\2\2\u00cc\u00cd")
        buf.write("\7h\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf\7p\2\2\u00cf\u00d0")
        buf.write("\7c\2\2\u00d0\u00d1\7n\2\2\u00d1\24\3\2\2\2\u00d2\u00d3")
        buf.write("\7u\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5\7c\2\2\u00d5\u00d6")
        buf.write("\7v\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8\7e\2\2\u00d8\26")
        buf.write("\3\2\2\2\u00d9\u00da\7g\2\2\u00da\u00db\7z\2\2\u00db\u00dc")
        buf.write("\7v\2\2\u00dc\u00dd\7g\2\2\u00dd\u00de\7p\2\2\u00de\u00df")
        buf.write("\7f\2\2\u00df\u00e0\7u\2\2\u00e0\30\3\2\2\2\u00e1\u00e2")
        buf.write("\7x\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7k\2\2\u00e4\u00e5")
        buf.write("\7f\2\2\u00e5\32\3\2\2\2\u00e6\u00e7\7o\2\2\u00e7\u00e8")
        buf.write("\7c\2\2\u00e8\u00e9\7k\2\2\u00e9\u00ea\7p\2\2\u00ea\34")
        buf.write("\3\2\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed\7g\2\2\u00ed\u00ee")
        buf.write("\7y\2\2\u00ee\36\3\2\2\2\u00ef\u00f0\7t\2\2\u00f0\u00f1")
        buf.write("\7g\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3\7w\2\2\u00f3\u00f4")
        buf.write("\7t\2\2\u00f4\u00f5\7p\2\2\u00f5 \3\2\2\2\u00f6\u00f7")
        buf.write("\7v\2\2\u00f7\u00f8\7t\2\2\u00f8\u00f9\7w\2\2\u00f9\u00fa")
        buf.write("\7g\2\2\u00fa\"\3\2\2\2\u00fb\u00fc\7h\2\2\u00fc\u00fd")
        buf.write("\7c\2\2\u00fd\u00fe\7n\2\2\u00fe\u00ff\7u\2\2\u00ff\u0100")
        buf.write("\7g\2\2\u0100$\3\2\2\2\u0101\u0102\7h\2\2\u0102\u0103")
        buf.write("\7q\2\2\u0103\u0104\7t\2\2\u0104&\3\2\2\2\u0105\u0106")
        buf.write("\7v\2\2\u0106\u0107\7j\2\2\u0107\u0108\7g\2\2\u0108\u0109")
        buf.write("\7p\2\2\u0109(\3\2\2\2\u010a\u010b\7p\2\2\u010b\u010c")
        buf.write("\7k\2\2\u010c\u010d\7n\2\2\u010d*\3\2\2\2\u010e\u010f")
        buf.write("\7k\2\2\u010f\u0110\7h\2\2\u0110,\3\2\2\2\u0111\u0112")
        buf.write("\7f\2\2\u0112\u0113\7q\2\2\u0113\u0114\7y\2\2\u0114\u0115")
        buf.write("\7p\2\2\u0115\u0116\7v\2\2\u0116\u0117\7q\2\2\u0117.\3")
        buf.write("\2\2\2\u0118\u0119\7v\2\2\u0119\u011a\7q\2\2\u011a\60")
        buf.write("\3\2\2\2\u011b\u011c\7d\2\2\u011c\u011d\7t\2\2\u011d\u011e")
        buf.write("\7g\2\2\u011e\u011f\7c\2\2\u011f\u0120\7m\2\2\u0120\62")
        buf.write("\3\2\2\2\u0121\u0122\7g\2\2\u0122\u0123\7n\2\2\u0123\u0124")
        buf.write("\7u\2\2\u0124\u0125\7g\2\2\u0125\64\3\2\2\2\u0126\u0127")
        buf.write("\7e\2\2\u0127\u0128\7q\2\2\u0128\u0129\7p\2\2\u0129\u012a")
        buf.write("\7v\2\2\u012a\u012b\7k\2\2\u012b\u012c\7p\2\2\u012c\u012d")
        buf.write("\7w\2\2\u012d\u012e\7g\2\2\u012e\66\3\2\2\2\u012f\u0130")
        buf.write("\7v\2\2\u0130\u0131\7j\2\2\u0131\u0132\7k\2\2\u0132\u0133")
        buf.write("\7u\2\2\u01338\3\2\2\2\u0134\u0135\7.\2\2\u0135:\3\2\2")
        buf.write("\2\u0136\u0137\7=\2\2\u0137<\3\2\2\2\u0138\u0139\7*\2")
        buf.write("\2\u0139>\3\2\2\2\u013a\u013b\7+\2\2\u013b@\3\2\2\2\u013c")
        buf.write("\u013d\7}\2\2\u013dB\3\2\2\2\u013e\u013f\7\177\2\2\u013f")
        buf.write("D\3\2\2\2\u0140\u0141\7]\2\2\u0141F\3\2\2\2\u0142\u0143")
        buf.write("\7_\2\2\u0143H\3\2\2\2\u0144\u0145\7?\2\2\u0145J\3\2\2")
        buf.write("\2\u0146\u0147\7-\2\2\u0147L\3\2\2\2\u0148\u0149\7/\2")
        buf.write("\2\u0149N\3\2\2\2\u014a\u014b\7,\2\2\u014bP\3\2\2\2\u014c")
        buf.write("\u014d\7\61\2\2\u014dR\3\2\2\2\u014e\u014f\7^\2\2\u014f")
        buf.write("T\3\2\2\2\u0150\u0151\7<\2\2\u0151\u0152\7?\2\2\u0152")
        buf.write("V\3\2\2\2\u0153\u0154\7>\2\2\u0154\u0155\7?\2\2\u0155")
        buf.write("X\3\2\2\2\u0156\u0157\7@\2\2\u0157\u0158\7?\2\2\u0158")
        buf.write("Z\3\2\2\2\u0159\u015a\7#\2\2\u015a\u015b\7?\2\2\u015b")
        buf.write("\\\3\2\2\2\u015c\u015d\7?\2\2\u015d\u015e\7?\2\2\u015e")
        buf.write("^\3\2\2\2\u015f\u0160\7>\2\2\u0160`\3\2\2\2\u0161\u0162")
        buf.write("\7@\2\2\u0162b\3\2\2\2\u0163\u0164\7\'\2\2\u0164d\3\2")
        buf.write("\2\2\u0165\u0166\7\60\2\2\u0166f\3\2\2\2\u0167\u0168\7")
        buf.write("(\2\2\u0168\u0169\7(\2\2\u0169h\3\2\2\2\u016a\u016b\7")
        buf.write("#\2\2\u016bj\3\2\2\2\u016c\u016d\7~\2\2\u016d\u016e\7")
        buf.write("~\2\2\u016el\3\2\2\2\u016f\u0170\7`\2\2\u0170n\3\2\2\2")
        buf.write("\u0171\u0175\t\5\2\2\u0172\u0174\t\6\2\2\u0173\u0172\3")
        buf.write("\2\2\2\u0174\u0177\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176")
        buf.write("\3\2\2\2\u0176p\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u0179")
        buf.write("\7\61\2\2\u0179\u017a\7,\2\2\u017a\u017e\3\2\2\2\u017b")
        buf.write("\u017d\13\2\2\2\u017c\u017b\3\2\2\2\u017d\u0180\3\2\2")
        buf.write("\2\u017e\u017f\3\2\2\2\u017e\u017c\3\2\2\2\u017f\u0181")
        buf.write("\3\2\2\2\u0180\u017e\3\2\2\2\u0181\u0182\7,\2\2\u0182")
        buf.write("\u0183\7\61\2\2\u0183\u0184\3\2\2\2\u0184\u0185\b9\2\2")
        buf.write("\u0185r\3\2\2\2\u0186\u018a\7%\2\2\u0187\u0189\n\7\2\2")
        buf.write("\u0188\u0187\3\2\2\2\u0189\u018c\3\2\2\2\u018a\u0188\3")
        buf.write("\2\2\2\u018a\u018b\3\2\2\2\u018b\u018e\3\2\2\2\u018c\u018a")
        buf.write("\3\2\2\2\u018d\u018f\t\b\2\2\u018e\u018d\3\2\2\2\u018f")
        buf.write("\u0190\3\2\2\2\u0190\u0191\b:\2\2\u0191t\3\2\2\2\u0192")
        buf.write("\u0194\t\t\2\2\u0193\u0192\3\2\2\2\u0194\u0195\3\2\2\2")
        buf.write("\u0195\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0197\3")
        buf.write("\2\2\2\u0197\u0198\b;\2\2\u0198v\3\2\2\2\u0199\u019d\7")
        buf.write("$\2\2\u019a\u019c\5{>\2\u019b\u019a\3\2\2\2\u019c\u019f")
        buf.write("\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019e")
        buf.write("\u01a0\3\2\2\2\u019f\u019d\3\2\2\2\u01a0\u01a1\b<\3\2")
        buf.write("\u01a1x\3\2\2\2\u01a2\u01a6\7$\2\2\u01a3\u01a5\5{>\2\u01a4")
        buf.write("\u01a3\3\2\2\2\u01a5\u01a8\3\2\2\2\u01a6\u01a4\3\2\2\2")
        buf.write("\u01a6\u01a7\3\2\2\2\u01a7\u01a9\3\2\2\2\u01a8\u01a6\3")
        buf.write("\2\2\2\u01a9\u01aa\5\177@\2\u01aa\u01ab\b=\4\2\u01abz")
        buf.write("\3\2\2\2\u01ac\u01af\n\n\2\2\u01ad\u01af\5}?\2\u01ae\u01ac")
        buf.write("\3\2\2\2\u01ae\u01ad\3\2\2\2\u01af|\3\2\2\2\u01b0\u01b2")
        buf.write("\7^\2\2\u01b1\u01b3\t\13\2\2\u01b2\u01b1\3\2\2\2\u01b3")
        buf.write("~\3\2\2\2\u01b4\u01b7\7^\2\2\u01b5\u01b8\n\f\2\2\u01b6")
        buf.write("\u01b8\n\r\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b6\3\2\2\2")
        buf.write("\u01b8\u0080\3\2\2\2\u01b9\u01ba\13\2\2\2\u01ba\u01bb")
        buf.write("\bA\5\2\u01bb\u0082\3\2\2\2\25\2\u0086\u008d\u0093\u0098")
        buf.write("\u009d\u00a2\u00aa\u00c4\u0175\u017e\u018a\u018e\u0195")
        buf.write("\u019d\u01a6\u01ae\u01b2\u01b7\6\b\2\2\3<\2\3=\3\3A\4")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    FLOATLIT = 1
    INTLIT = 2
    STRING_LIT = 3
    TYPE = 4
    CLASS = 5
    FINAL = 6
    STATIC = 7
    EXTEND = 8
    VOID = 9
    MAIN = 10
    NEW = 11
    RETURN = 12
    TRUE = 13
    FALSE = 14
    FOR = 15
    THEN = 16
    NIL = 17
    IF = 18
    DOWNTO = 19
    TO = 20
    BREAK = 21
    ELSE = 22
    CONTINUE = 23
    THIS = 24
    COMMA = 25
    SIMI = 26
    LP = 27
    RP = 28
    LB = 29
    RB = 30
    LSB = 31
    RSB = 32
    EQUATION = 33
    ADD = 34
    SUB = 35
    MUL = 36
    INT_DIV = 37
    FLOAT_DIV = 38
    ASSIGN = 39
    LOWER_E = 40
    GREATER_E = 41
    NOT_EQUALS = 42
    EQUALS = 43
    LOWER = 44
    GREATER = 45
    PERCENT = 46
    DOT = 47
    AND = 48
    NOT = 49
    OR = 50
    CONCAT = 51
    ID = 52
    BLOCK_COMMENT = 53
    LINE_COMMENT = 54
    WS = 55
    UNCLOSE_STRING = 56
    ILLEGAL_ESCAPE = 57
    ERROR_CHAR = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'class'", "'final'", "'static'", "'extends'", "'void'", "'main'", 
            "'new'", "'return'", "'true'", "'false'", "'for'", "'then'", 
            "'nil'", "'if'", "'downto'", "'to'", "'break'", "'else'", "'continue'", 
            "'this'", "','", "';'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "'='", "'+'", "'-'", "'*'", "'/'", "'\\'", "':='", "'<='", "'>='", 
            "'!='", "'=='", "'<'", "'>'", "'%'", "'.'", "'&&'", "'!'", "'||'", 
            "'^'" ]

    symbolicNames = [ "<INVALID>",
            "FLOATLIT", "INTLIT", "STRING_LIT", "TYPE", "CLASS", "FINAL", 
            "STATIC", "EXTEND", "VOID", "MAIN", "NEW", "RETURN", "TRUE", 
            "FALSE", "FOR", "THEN", "NIL", "IF", "DOWNTO", "TO", "BREAK", 
            "ELSE", "CONTINUE", "THIS", "COMMA", "SIMI", "LP", "RP", "LB", 
            "RB", "LSB", "RSB", "EQUATION", "ADD", "SUB", "MUL", "INT_DIV", 
            "FLOAT_DIV", "ASSIGN", "LOWER_E", "GREATER_E", "NOT_EQUALS", 
            "EQUALS", "LOWER", "GREATER", "PERCENT", "DOT", "AND", "NOT", 
            "OR", "CONCAT", "ID", "BLOCK_COMMENT", "LINE_COMMENT", "WS", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "FLOATLIT", "DECIMAL", "EXPONENT", "INTLIT", "DIGIT", 
                  "STRING_LIT", "TYPE", "CLASS", "FINAL", "STATIC", "EXTEND", 
                  "VOID", "MAIN", "NEW", "RETURN", "TRUE", "FALSE", "FOR", 
                  "THEN", "NIL", "IF", "DOWNTO", "TO", "BREAK", "ELSE", 
                  "CONTINUE", "THIS", "COMMA", "SIMI", "LP", "RP", "LB", 
                  "RB", "LSB", "RSB", "EQUATION", "ADD", "SUB", "MUL", "INT_DIV", 
                  "FLOAT_DIV", "ASSIGN", "LOWER_E", "GREATER_E", "NOT_EQUALS", 
                  "EQUALS", "LOWER", "GREATER", "PERCENT", "DOT", "AND", 
                  "NOT", "OR", "CONCAT", "ID", "BLOCK_COMMENT", "LINE_COMMENT", 
                  "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "STR_CHAR", 
                  "ESC_SEQ", "ESC_ILLEGAL", "ERROR_CHAR" ]

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
            actions[58] = self.UNCLOSE_STRING_action 
            actions[59] = self.ILLEGAL_ESCAPE_action 
            actions[63] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		y = str(self.text)
            		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
            		if y[-1] in possible:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		raise ErrorToken(self.text)
            	
     


