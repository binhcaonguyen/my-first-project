# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


#MSSV 1610228
from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2>")
        buf.write("\u0268\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%")
        buf.write("\3%\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+")
        buf.write("\3+\7+\u0185\n+\f+\16+\u0188\13+\3+\3+\3+\3+\3+\3,\3,")
        buf.write("\7,\u0191\n,\f,\16,\u0194\13,\3,\3,\3,\3,\3-\3-\3-\3-")
        buf.write("\7-\u019e\n-\f-\16-\u01a1\13-\3-\3-\3.\3.\3/\3/\3\60\3")
        buf.write("\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\7\64\u01b3")
        buf.write("\n\64\f\64\16\64\u01b6\13\64\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\58\u01c2\n8\38\38\38\58\u01c7\n")
        buf.write("8\39\59\u01ca\n9\39\39\39\39\39\59\u01d1\n9\3:\3:\5:\u01d5")
        buf.write("\n:\3:\3:\3:\5:\u01da\n:\3:\5:\u01dd\n:\3;\3;\3<\6<\u01e2")
        buf.write("\n<\r<\16<\u01e3\3=\3=\3>\3>\5>\u01ea\n>\3?\3?\7?\u01ee")
        buf.write("\n?\f?\16?\u01f1\13?\3@\3@\5@\u01f5\n@\3@\3@\3@\3A\6A")
        buf.write("\u01fb\nA\rA\16A\u01fc\3B\3B\5B\u0201\nB\3C\3C\3C\3D\3")
        buf.write("D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3L\3M\3")
        buf.write("M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\3S\3T\3T\3U\3U\3V\3")
        buf.write("V\3W\3W\3X\3X\3Y\3Y\3Z\3Z\3[\3[\3\\\3\\\3]\3]\3^\6^\u023b")
        buf.write("\n^\r^\16^\u023c\3^\3^\3_\3_\7_\u0243\n_\f_\16_\u0246")
        buf.write("\13_\3_\3_\3_\3_\7_\u024c\n_\f_\16_\u024f\13_\3_\3_\5")
        buf.write("_\u0253\n_\3`\3`\7`\u0257\n`\f`\16`\u025a\13`\3`\3`\3")
        buf.write("`\3`\3`\3`\5`\u0262\n`\3`\3`\3a\3a\3a\4\u0186\u0192\2")
        buf.write("b\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\2-\2/\27\61")
        buf.write("\30\63\31\65\32\67\339\34;\35=\36?\37A C!E\"G#I$K%M&O")
        buf.write("\'Q(S)U*W+Y,[-]._/a\60c\61e\62g\63i\64k\65m\66o\67q\2")
        buf.write("s\2u\2w\2y\2{8}9\177:\u0081\2\u0083\2\u0085\2\u0087\2")
        buf.write("\u0089\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095")
        buf.write("\2\u0097\2\u0099\2\u009b\2\u009d\2\u009f\2\u00a1\2\u00a3")
        buf.write("\2\u00a5\2\u00a7\2\u00a9\2\u00ab\2\u00ad\2\u00af\2\u00b1")
        buf.write("\2\u00b3\2\u00b5\2\u00b7\2\u00b9\2\u00bb;\u00bd<\u00bf")
        buf.write("=\u00c1>\3\2\'\4\2\f\f\17\17\3\2\"\"\4\2--//\3\2\62;\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\7\2\n\f\16\17$$))^^\n\2$$))^")
        buf.write("^ddhhppttvv\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4")
        buf.write("\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNn")
        buf.write("n\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2")
        buf.write("UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4")
        buf.write("\2\\\\||\5\2\13\f\16\17\"\"\t\2$$))^^ddhhttvv\3\2$$\2")
        buf.write("\u025c\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2")
        buf.write("a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2")
        buf.write("\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2{\3\2\2\2\2}\3\2\2")
        buf.write("\2\2\177\3\2\2\2\2\u00bb\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf")
        buf.write("\3\2\2\2\2\u00c1\3\2\2\2\3\u00c3\3\2\2\2\5\u00c9\3\2\2")
        buf.write("\2\7\u00d2\3\2\2\2\t\u00d6\3\2\2\2\13\u00d9\3\2\2\2\r")
        buf.write("\u00e0\3\2\2\2\17\u00e3\3\2\2\2\21\u00e6\3\2\2\2\23\u00eb")
        buf.write("\3\2\2\2\25\u00f0\3\2\2\2\27\u00f7\3\2\2\2\31\u00fd\3")
        buf.write("\2\2\2\33\u0102\3\2\2\2\35\u0108\3\2\2\2\37\u010c\3\2")
        buf.write("\2\2!\u0115\3\2\2\2#\u011f\3\2\2\2%\u0123\3\2\2\2\'\u0129")
        buf.write("\3\2\2\2)\u012c\3\2\2\2+\u0131\3\2\2\2-\u0136\3\2\2\2")
        buf.write("/\u013c\3\2\2\2\61\u0144\3\2\2\2\63\u014c\3\2\2\2\65\u0153")
        buf.write("\3\2\2\2\67\u0157\3\2\2\29\u015b\3\2\2\2;\u015e\3\2\2")
        buf.write("\2=\u0162\3\2\2\2?\u0166\3\2\2\2A\u0168\3\2\2\2C\u016a")
        buf.write("\3\2\2\2E\u016c\3\2\2\2G\u016e\3\2\2\2I\u0171\3\2\2\2")
        buf.write("K\u0173\3\2\2\2M\u0175\3\2\2\2O\u0177\3\2\2\2Q\u017a\3")
        buf.write("\2\2\2S\u017d\3\2\2\2U\u0180\3\2\2\2W\u018e\3\2\2\2Y\u0199")
        buf.write("\3\2\2\2[\u01a4\3\2\2\2]\u01a6\3\2\2\2_\u01a8\3\2\2\2")
        buf.write("a\u01aa\3\2\2\2c\u01ac\3\2\2\2e\u01ae\3\2\2\2g\u01b0\3")
        buf.write("\2\2\2i\u01b9\3\2\2\2k\u01bb\3\2\2\2m\u01bd\3\2\2\2o\u01c6")
        buf.write("\3\2\2\2q\u01d0\3\2\2\2s\u01dc\3\2\2\2u\u01de\3\2\2\2")
        buf.write("w\u01e1\3\2\2\2y\u01e5\3\2\2\2{\u01e9\3\2\2\2}\u01eb\3")
        buf.write("\2\2\2\177\u01f2\3\2\2\2\u0081\u01fa\3\2\2\2\u0083\u0200")
        buf.write("\3\2\2\2\u0085\u0202\3\2\2\2\u0087\u0205\3\2\2\2\u0089")
        buf.write("\u0207\3\2\2\2\u008b\u0209\3\2\2\2\u008d\u020b\3\2\2\2")
        buf.write("\u008f\u020d\3\2\2\2\u0091\u020f\3\2\2\2\u0093\u0211\3")
        buf.write("\2\2\2\u0095\u0213\3\2\2\2\u0097\u0215\3\2\2\2\u0099\u0217")
        buf.write("\3\2\2\2\u009b\u0219\3\2\2\2\u009d\u021b\3\2\2\2\u009f")
        buf.write("\u021d\3\2\2\2\u00a1\u021f\3\2\2\2\u00a3\u0221\3\2\2\2")
        buf.write("\u00a5\u0223\3\2\2\2\u00a7\u0225\3\2\2\2\u00a9\u0227\3")
        buf.write("\2\2\2\u00ab\u0229\3\2\2\2\u00ad\u022b\3\2\2\2\u00af\u022d")
        buf.write("\3\2\2\2\u00b1\u022f\3\2\2\2\u00b3\u0231\3\2\2\2\u00b5")
        buf.write("\u0233\3\2\2\2\u00b7\u0235\3\2\2\2\u00b9\u0237\3\2\2\2")
        buf.write("\u00bb\u023a\3\2\2\2\u00bd\u0252\3\2\2\2\u00bf\u0254\3")
        buf.write("\2\2\2\u00c1\u0265\3\2\2\2\u00c3\u00c4\5\u0089E\2\u00c4")
        buf.write("\u00c5\5\u00a9U\2\u00c5\u00c6\5\u008fH\2\u00c6\u00c7\5")
        buf.write("\u0087D\2\u00c7\u00c8\5\u009bN\2\u00c8\4\3\2\2\2\u00c9")
        buf.write("\u00ca\5\u008bF\2\u00ca\u00cb\5\u00a3R\2\u00cb\u00cc\5")
        buf.write("\u00a1Q\2\u00cc\u00cd\5\u00adW\2\u00cd\u00ce\5\u0097L")
        buf.write("\2\u00ce\u00cf\5\u00a1Q\2\u00cf\u00d0\5\u00afX\2\u00d0")
        buf.write("\u00d1\5\u008fH\2\u00d1\6\3\2\2\2\u00d2\u00d3\5\u0091")
        buf.write("I\2\u00d3\u00d4\5\u00a3R\2\u00d4\u00d5\5\u00a9U\2\u00d5")
        buf.write("\b\3\2\2\2\u00d6\u00d7\5\u00adW\2\u00d7\u00d8\5\u00a3")
        buf.write("R\2\u00d8\n\3\2\2\2\u00d9\u00da\5\u008dG\2\u00da\u00db")
        buf.write("\5\u00a3R\2\u00db\u00dc\5\u00b3Z\2\u00dc\u00dd\5\u00a1")
        buf.write("Q\2\u00dd\u00de\5\u00adW\2\u00de\u00df\5\u00a3R\2\u00df")
        buf.write("\f\3\2\2\2\u00e0\u00e1\5\u008dG\2\u00e1\u00e2\5\u00a3")
        buf.write("R\2\u00e2\16\3\2\2\2\u00e3\u00e4\5\u0097L\2\u00e4\u00e5")
        buf.write("\5\u0091I\2\u00e5\20\3\2\2\2\u00e6\u00e7\5\u00adW\2\u00e7")
        buf.write("\u00e8\5\u0095K\2\u00e8\u00e9\5\u008fH\2\u00e9\u00ea\5")
        buf.write("\u00a1Q\2\u00ea\22\3\2\2\2\u00eb\u00ec\5\u008fH\2\u00ec")
        buf.write("\u00ed\5\u009dO\2\u00ed\u00ee\5\u00abV\2\u00ee\u00ef\5")
        buf.write("\u008fH\2\u00ef\24\3\2\2\2\u00f0\u00f1\5\u00a9U\2\u00f1")
        buf.write("\u00f2\5\u008fH\2\u00f2\u00f3\5\u00adW\2\u00f3\u00f4\5")
        buf.write("\u00afX\2\u00f4\u00f5\5\u00a9U\2\u00f5\u00f6\5\u00a1Q")
        buf.write("\2\u00f6\26\3\2\2\2\u00f7\u00f8\5\u00b3Z\2\u00f8\u00f9")
        buf.write("\5\u0095K\2\u00f9\u00fa\5\u0097L\2\u00fa\u00fb\5\u009d")
        buf.write("O\2\u00fb\u00fc\5\u008fH\2\u00fc\30\3\2\2\2\u00fd\u00fe")
        buf.write("\5\u00b3Z\2\u00fe\u00ff\5\u0097L\2\u00ff\u0100\5\u00ad")
        buf.write("W\2\u0100\u0101\5\u0095K\2\u0101\32\3\2\2\2\u0102\u0103")
        buf.write("\5\u0089E\2\u0103\u0104\5\u008fH\2\u0104\u0105\5\u0093")
        buf.write("J\2\u0105\u0106\5\u0097L\2\u0106\u0107\5\u00a1Q\2\u0107")
        buf.write("\34\3\2\2\2\u0108\u0109\5\u008fH\2\u0109\u010a\5\u00a1")
        buf.write("Q\2\u010a\u010b\5\u008dG\2\u010b\36\3\2\2\2\u010c\u010d")
        buf.write("\5\u0091I\2\u010d\u010e\5\u00afX\2\u010e\u010f\5\u00a1")
        buf.write("Q\2\u010f\u0110\5\u008bF\2\u0110\u0111\5\u00adW\2\u0111")
        buf.write("\u0112\5\u0097L\2\u0112\u0113\5\u00a3R\2\u0113\u0114\5")
        buf.write("\u00a1Q\2\u0114 \3\2\2\2\u0115\u0116\5\u00a5S\2\u0116")
        buf.write("\u0117\5\u00a9U\2\u0117\u0118\5\u00a3R\2\u0118\u0119\5")
        buf.write("\u008bF\2\u0119\u011a\5\u008fH\2\u011a\u011b\5\u008dG")
        buf.write("\2\u011b\u011c\5\u00afX\2\u011c\u011d\5\u00a9U\2\u011d")
        buf.write("\u011e\5\u008fH\2\u011e\"\3\2\2\2\u011f\u0120\5\u00b1")
        buf.write("Y\2\u0120\u0121\5\u0087D\2\u0121\u0122\5\u00a9U\2\u0122")
        buf.write("$\3\2\2\2\u0123\u0124\5\u0087D\2\u0124\u0125\5\u00a9U")
        buf.write("\2\u0125\u0126\5\u00a9U\2\u0126\u0127\5\u0087D\2\u0127")
        buf.write("\u0128\5\u00b7\\\2\u0128&\3\2\2\2\u0129\u012a\5\u00a3")
        buf.write("R\2\u012a\u012b\5\u0091I\2\u012b(\3\2\2\2\u012c\u012d")
        buf.write("\5\u00a9U\2\u012d\u012e\5\u008fH\2\u012e\u012f\5\u0087")
        buf.write("D\2\u012f\u0130\5\u009dO\2\u0130*\3\2\2\2\u0131\u0132")
        buf.write("\5\u00adW\2\u0132\u0133\5\u00a9U\2\u0133\u0134\5\u00af")
        buf.write("X\2\u0134\u0135\5\u008fH\2\u0135,\3\2\2\2\u0136\u0137")
        buf.write("\5\u0091I\2\u0137\u0138\5\u0087D\2\u0138\u0139\5\u009d")
        buf.write("O\2\u0139\u013a\5\u00abV\2\u013a\u013b\5\u008fH\2\u013b")
        buf.write(".\3\2\2\2\u013c\u013d\5\u0089E\2\u013d\u013e\5\u00a3R")
        buf.write("\2\u013e\u013f\5\u00a3R\2\u013f\u0140\5\u009dO\2\u0140")
        buf.write("\u0141\5\u008fH\2\u0141\u0142\5\u0087D\2\u0142\u0143\5")
        buf.write("\u00a1Q\2\u0143\60\3\2\2\2\u0144\u0145\5\u0097L\2\u0145")
        buf.write("\u0146\5\u00a1Q\2\u0146\u0147\5\u00adW\2\u0147\u0148\5")
        buf.write("\u008fH\2\u0148\u0149\5\u0093J\2\u0149\u014a\5\u008fH")
        buf.write("\2\u014a\u014b\5\u00a9U\2\u014b\62\3\2\2\2\u014c\u014d")
        buf.write("\5\u00abV\2\u014d\u014e\5\u00adW\2\u014e\u014f\5\u00a9")
        buf.write("U\2\u014f\u0150\5\u0097L\2\u0150\u0151\5\u00a1Q\2\u0151")
        buf.write("\u0152\5\u0093J\2\u0152\64\3\2\2\2\u0153\u0154\5\u00a1")
        buf.write("Q\2\u0154\u0155\5\u00a3R\2\u0155\u0156\5\u00adW\2\u0156")
        buf.write("\66\3\2\2\2\u0157\u0158\5\u0087D\2\u0158\u0159\5\u00a1")
        buf.write("Q\2\u0159\u015a\5\u008dG\2\u015a8\3\2\2\2\u015b\u015c")
        buf.write("\5\u00a3R\2\u015c\u015d\5\u00a9U\2\u015d:\3\2\2\2\u015e")
        buf.write("\u015f\5\u008dG\2\u015f\u0160\5\u0097L\2\u0160\u0161\5")
        buf.write("\u00b1Y\2\u0161<\3\2\2\2\u0162\u0163\5\u009fP\2\u0163")
        buf.write("\u0164\5\u00a3R\2\u0164\u0165\5\u008dG\2\u0165>\3\2\2")
        buf.write("\2\u0166\u0167\7-\2\2\u0167@\3\2\2\2\u0168\u0169\7/\2")
        buf.write("\2\u0169B\3\2\2\2\u016a\u016b\7,\2\2\u016bD\3\2\2\2\u016c")
        buf.write("\u016d\7\61\2\2\u016dF\3\2\2\2\u016e\u016f\7>\2\2\u016f")
        buf.write("\u0170\7@\2\2\u0170H\3\2\2\2\u0171\u0172\7?\2\2\u0172")
        buf.write("J\3\2\2\2\u0173\u0174\7>\2\2\u0174L\3\2\2\2\u0175\u0176")
        buf.write("\7@\2\2\u0176N\3\2\2\2\u0177\u0178\7>\2\2\u0178\u0179")
        buf.write("\7?\2\2\u0179P\3\2\2\2\u017a\u017b\7@\2\2\u017b\u017c")
        buf.write("\7?\2\2\u017cR\3\2\2\2\u017d\u017e\7<\2\2\u017e\u017f")
        buf.write("\7?\2\2\u017fT\3\2\2\2\u0180\u0181\7*\2\2\u0181\u0182")
        buf.write("\7,\2\2\u0182\u0186\3\2\2\2\u0183\u0185\13\2\2\2\u0184")
        buf.write("\u0183\3\2\2\2\u0185\u0188\3\2\2\2\u0186\u0187\3\2\2\2")
        buf.write("\u0186\u0184\3\2\2\2\u0187\u0189\3\2\2\2\u0188\u0186\3")
        buf.write("\2\2\2\u0189\u018a\7,\2\2\u018a\u018b\7+\2\2\u018b\u018c")
        buf.write("\3\2\2\2\u018c\u018d\b+\2\2\u018dV\3\2\2\2\u018e\u0192")
        buf.write("\7}\2\2\u018f\u0191\13\2\2\2\u0190\u018f\3\2\2\2\u0191")
        buf.write("\u0194\3\2\2\2\u0192\u0193\3\2\2\2\u0192\u0190\3\2\2\2")
        buf.write("\u0193\u0195\3\2\2\2\u0194\u0192\3\2\2\2\u0195\u0196\7")
        buf.write("\177\2\2\u0196\u0197\3\2\2\2\u0197\u0198\b,\2\2\u0198")
        buf.write("X\3\2\2\2\u0199\u019a\7\61\2\2\u019a\u019b\7\61\2\2\u019b")
        buf.write("\u019f\3\2\2\2\u019c\u019e\n\2\2\2\u019d\u019c\3\2\2\2")
        buf.write("\u019e\u01a1\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3")
        buf.write("\2\2\2\u01a0\u01a2\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2\u01a3")
        buf.write("\b-\2\2\u01a3Z\3\2\2\2\u01a4\u01a5\7*\2\2\u01a5\\\3\2")
        buf.write("\2\2\u01a6\u01a7\7+\2\2\u01a7^\3\2\2\2\u01a8\u01a9\7]")
        buf.write("\2\2\u01a9`\3\2\2\2\u01aa\u01ab\7_\2\2\u01abb\3\2\2\2")
        buf.write("\u01ac\u01ad\7<\2\2\u01add\3\2\2\2\u01ae\u01af\7=\2\2")
        buf.write("\u01aff\3\2\2\2\u01b0\u01b4\7\60\2\2\u01b1\u01b3\t\3\2")
        buf.write("\2\u01b2\u01b1\3\2\2\2\u01b3\u01b6\3\2\2\2\u01b4\u01b2")
        buf.write("\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b7\3\2\2\2\u01b6")
        buf.write("\u01b4\3\2\2\2\u01b7\u01b8\7\60\2\2\u01b8h\3\2\2\2\u01b9")
        buf.write("\u01ba\7.\2\2\u01baj\3\2\2\2\u01bb\u01bc\7$\2\2\u01bc")
        buf.write("l\3\2\2\2\u01bd\u01be\5w<\2\u01ben\3\2\2\2\u01bf\u01c1")
        buf.write("\5q9\2\u01c0\u01c2\5s:\2\u01c1\u01c0\3\2\2\2\u01c1\u01c2")
        buf.write("\3\2\2\2\u01c2\u01c7\3\2\2\2\u01c3\u01c4\5w<\2\u01c4\u01c5")
        buf.write("\5s:\2\u01c5\u01c7\3\2\2\2\u01c6\u01bf\3\2\2\2\u01c6\u01c3")
        buf.write("\3\2\2\2\u01c7p\3\2\2\2\u01c8\u01ca\5w<\2\u01c9\u01c8")
        buf.write("\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb")
        buf.write("\u01cc\7\60\2\2\u01cc\u01d1\5w<\2\u01cd\u01ce\5w<\2\u01ce")
        buf.write("\u01cf\7\60\2\2\u01cf\u01d1\3\2\2\2\u01d0\u01c9\3\2\2")
        buf.write("\2\u01d0\u01cd\3\2\2\2\u01d1r\3\2\2\2\u01d2\u01d4\7g\2")
        buf.write("\2\u01d3\u01d5\5u;\2\u01d4\u01d3\3\2\2\2\u01d4\u01d5\3")
        buf.write("\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01dd\5w<\2\u01d7\u01d9")
        buf.write("\7G\2\2\u01d8\u01da\5u;\2\u01d9\u01d8\3\2\2\2\u01d9\u01da")
        buf.write("\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01dd\5w<\2\u01dc\u01d2")
        buf.write("\3\2\2\2\u01dc\u01d7\3\2\2\2\u01ddt\3\2\2\2\u01de\u01df")
        buf.write("\t\4\2\2\u01dfv\3\2\2\2\u01e0\u01e2\5y=\2\u01e1\u01e0")
        buf.write("\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e3")
        buf.write("\u01e4\3\2\2\2\u01e4x\3\2\2\2\u01e5\u01e6\t\5\2\2\u01e6")
        buf.write("z\3\2\2\2\u01e7\u01ea\5+\26\2\u01e8\u01ea\5-\27\2\u01e9")
        buf.write("\u01e7\3\2\2\2\u01e9\u01e8\3\2\2\2\u01ea|\3\2\2\2\u01eb")
        buf.write("\u01ef\t\6\2\2\u01ec\u01ee\t\7\2\2\u01ed\u01ec\3\2\2\2")
        buf.write("\u01ee\u01f1\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0\3")
        buf.write("\2\2\2\u01f0~\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f2\u01f4")
        buf.write("\5k\66\2\u01f3\u01f5\5\u0081A\2\u01f4\u01f3\3\2\2\2\u01f4")
        buf.write("\u01f5\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f7\5k\66\2")
        buf.write("\u01f7\u01f8\b@\3\2\u01f8\u0080\3\2\2\2\u01f9\u01fb\5")
        buf.write("\u0083B\2\u01fa\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc")
        buf.write("\u01fa\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u0082\3\2\2\2")
        buf.write("\u01fe\u0201\n\b\2\2\u01ff\u0201\5\u0085C\2\u0200\u01fe")
        buf.write("\3\2\2\2\u0200\u01ff\3\2\2\2\u0201\u0084\3\2\2\2\u0202")
        buf.write("\u0203\7^\2\2\u0203\u0204\t\t\2\2\u0204\u0086\3\2\2\2")
        buf.write("\u0205\u0206\t\n\2\2\u0206\u0088\3\2\2\2\u0207\u0208\t")
        buf.write("\13\2\2\u0208\u008a\3\2\2\2\u0209\u020a\t\f\2\2\u020a")
        buf.write("\u008c\3\2\2\2\u020b\u020c\t\r\2\2\u020c\u008e\3\2\2\2")
        buf.write("\u020d\u020e\t\16\2\2\u020e\u0090\3\2\2\2\u020f\u0210")
        buf.write("\t\17\2\2\u0210\u0092\3\2\2\2\u0211\u0212\t\20\2\2\u0212")
        buf.write("\u0094\3\2\2\2\u0213\u0214\t\21\2\2\u0214\u0096\3\2\2")
        buf.write("\2\u0215\u0216\t\22\2\2\u0216\u0098\3\2\2\2\u0217\u0218")
        buf.write("\t\23\2\2\u0218\u009a\3\2\2\2\u0219\u021a\t\24\2\2\u021a")
        buf.write("\u009c\3\2\2\2\u021b\u021c\t\25\2\2\u021c\u009e\3\2\2")
        buf.write("\2\u021d\u021e\t\26\2\2\u021e\u00a0\3\2\2\2\u021f\u0220")
        buf.write("\t\27\2\2\u0220\u00a2\3\2\2\2\u0221\u0222\t\30\2\2\u0222")
        buf.write("\u00a4\3\2\2\2\u0223\u0224\t\31\2\2\u0224\u00a6\3\2\2")
        buf.write("\2\u0225\u0226\t\32\2\2\u0226\u00a8\3\2\2\2\u0227\u0228")
        buf.write("\t\33\2\2\u0228\u00aa\3\2\2\2\u0229\u022a\t\34\2\2\u022a")
        buf.write("\u00ac\3\2\2\2\u022b\u022c\t\35\2\2\u022c\u00ae\3\2\2")
        buf.write("\2\u022d\u022e\t\36\2\2\u022e\u00b0\3\2\2\2\u022f\u0230")
        buf.write("\t\37\2\2\u0230\u00b2\3\2\2\2\u0231\u0232\t \2\2\u0232")
        buf.write("\u00b4\3\2\2\2\u0233\u0234\t!\2\2\u0234\u00b6\3\2\2\2")
        buf.write("\u0235\u0236\t\"\2\2\u0236\u00b8\3\2\2\2\u0237\u0238\t")
        buf.write("#\2\2\u0238\u00ba\3\2\2\2\u0239\u023b\t$\2\2\u023a\u0239")
        buf.write("\3\2\2\2\u023b\u023c\3\2\2\2\u023c\u023a\3\2\2\2\u023c")
        buf.write("\u023d\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u023f\b^\2\2")
        buf.write("\u023f\u00bc\3\2\2\2\u0240\u0244\7$\2\2\u0241\u0243\5")
        buf.write("\u0083B\2\u0242\u0241\3\2\2\2\u0243\u0246\3\2\2\2\u0244")
        buf.write("\u0242\3\2\2\2\u0244\u0245\3\2\2\2\u0245\u0247\3\2\2\2")
        buf.write("\u0246\u0244\3\2\2\2\u0247\u0248\7\f\2\2\u0248\u0253\b")
        buf.write("_\4\2\u0249\u024d\7$\2\2\u024a\u024c\5\u0083B\2\u024b")
        buf.write("\u024a\3\2\2\2\u024c\u024f\3\2\2\2\u024d\u024b\3\2\2\2")
        buf.write("\u024d\u024e\3\2\2\2\u024e\u0250\3\2\2\2\u024f\u024d\3")
        buf.write("\2\2\2\u0250\u0251\7\2\2\3\u0251\u0253\b_\5\2\u0252\u0240")
        buf.write("\3\2\2\2\u0252\u0249\3\2\2\2\u0253\u00be\3\2\2\2\u0254")
        buf.write("\u0258\7$\2\2\u0255\u0257\5\u0083B\2\u0256\u0255\3\2\2")
        buf.write("\2\u0257\u025a\3\2\2\2\u0258\u0256\3\2\2\2\u0258\u0259")
        buf.write("\3\2\2\2\u0259\u0261\3\2\2\2\u025a\u0258\3\2\2\2\u025b")
        buf.write("\u025c\7^\2\2\u025c\u0262\n%\2\2\u025d\u0262\n&\2\2\u025e")
        buf.write("\u0262\7)\2\2\u025f\u0260\7^\2\2\u0260\u0262\7\2\2\3\u0261")
        buf.write("\u025b\3\2\2\2\u0261\u025d\3\2\2\2\u0261\u025e\3\2\2\2")
        buf.write("\u0261\u025f\3\2\2\2\u0262\u0263\3\2\2\2\u0263\u0264\b")
        buf.write("`\6\2\u0264\u00c0\3\2\2\2\u0265\u0266\13\2\2\2\u0266\u0267")
        buf.write("\ba\7\2\u0267\u00c2\3\2\2\2\32\2\u0186\u0192\u019f\u01b4")
        buf.write("\u01c1\u01c6\u01c9\u01d0\u01d4\u01d9\u01dc\u01e3\u01e9")
        buf.write("\u01ef\u01f4\u01fc\u0200\u023c\u0244\u024d\u0252\u0258")
        buf.write("\u0261\b\b\2\2\3@\2\3_\3\3_\4\3`\5\3a\6")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BREAK = 1
    CONTINUE = 2
    FOR = 3
    TO = 4
    DOWNTO = 5
    DO = 6
    IF = 7
    THEN = 8
    ELSE = 9
    RETURN = 10
    WHILE = 11
    WITH = 12
    BEGIN = 13
    END = 14
    FUNCTION = 15
    PROCEDURE = 16
    VAR = 17
    ARRAY = 18
    OF = 19
    REAL = 20
    BOOLEAN = 21
    INTEGER = 22
    STRING = 23
    NOT = 24
    AND = 25
    OR = 26
    DIV = 27
    MOD = 28
    ADDOP = 29
    SUBOP = 30
    MULOP = 31
    DIVOP = 32
    NOT_EQUAL = 33
    EQUAL = 34
    LESS = 35
    GREATER = 36
    LESS_OR_EQUAL = 37
    GREATER_OR_EQUAL = 38
    ASSIGN = 39
    TRADITIONAL_BLOCK_COMMENT = 40
    BLOCK_COMMENT = 41
    LINE_COMMENT = 42
    LB = 43
    RB = 44
    LQ = 45
    RQ = 46
    COLON = 47
    SEMI = 48
    DOUBLE_DOT = 49
    COMMA = 50
    QUOTES = 51
    INTLIT = 52
    FLOATLIT = 53
    BOOLLIT = 54
    IDENTIFIER = 55
    STRINGLIT = 56
    WS = 57
    UNCLOSE_STRING = 58
    ILLEGAL_ESCAPE = 59
    ERROR_CHAR = 60

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'<>'", "'='", "'<'", "'>'", "'<='", 
            "'>='", "':='", "'('", "')'", "'['", "']'", "':'", "';'", "','", 
            "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", 
            "ELSE", "RETURN", "WHILE", "WITH", "BEGIN", "END", "FUNCTION", 
            "PROCEDURE", "VAR", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
            "STRING", "NOT", "AND", "OR", "DIV", "MOD", "ADDOP", "SUBOP", 
            "MULOP", "DIVOP", "NOT_EQUAL", "EQUAL", "LESS", "GREATER", "LESS_OR_EQUAL", 
            "GREATER_OR_EQUAL", "ASSIGN", "TRADITIONAL_BLOCK_COMMENT", "BLOCK_COMMENT", 
            "LINE_COMMENT", "LB", "RB", "LQ", "RQ", "COLON", "SEMI", "DOUBLE_DOT", 
            "COMMA", "QUOTES", "INTLIT", "FLOATLIT", "BOOLLIT", "IDENTIFIER", 
            "STRINGLIT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", 
                  "THEN", "ELSE", "RETURN", "WHILE", "WITH", "BEGIN", "END", 
                  "FUNCTION", "PROCEDURE", "VAR", "ARRAY", "OF", "REAL", 
                  "TRUE", "FALSE", "BOOLEAN", "INTEGER", "STRING", "NOT", 
                  "AND", "OR", "DIV", "MOD", "ADDOP", "SUBOP", "MULOP", 
                  "DIVOP", "NOT_EQUAL", "EQUAL", "LESS", "GREATER", "LESS_OR_EQUAL", 
                  "GREATER_OR_EQUAL", "ASSIGN", "TRADITIONAL_BLOCK_COMMENT", 
                  "BLOCK_COMMENT", "LINE_COMMENT", "LB", "RB", "LQ", "RQ", 
                  "COLON", "SEMI", "DOUBLE_DOT", "COMMA", "QUOTES", "INTLIT", 
                  "FLOATLIT", "FRACTIONAL_CONSTANT", "EXPONENT_PART", "SIGN", 
                  "DIGIT_SEQUENCE", "DIGIT", "BOOLLIT", "IDENTIFIER", "STRINGLIT", 
                  "STRING_CHARACTERS", "STRING_CHARACTER", "ESCAPE_SEQUENCE", 
                  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                  "W", "X", "Y", "Z", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[62] = self.STRINGLIT_action 
            actions[93] = self.UNCLOSE_STRING_action 
            actions[94] = self.ILLEGAL_ESCAPE_action 
            actions[95] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

             self.text = self.text[1:-1]
             
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise UncloseString(self.text[1:-1])
     

        if actionIndex == 2:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     


