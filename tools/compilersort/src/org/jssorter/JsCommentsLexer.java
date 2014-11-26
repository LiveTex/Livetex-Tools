package org.jssorter;// Generated from /home/dev/IdeaProjects/CompilerSort/JsComments.g4 by ANTLR 4.4.1-dev

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class JsCommentsLexer extends Lexer {
  static {
    RuntimeMetaData.checkVersion("4.4.1-dev", RuntimeMetaData.VERSION);
  }

  protected static final DFA[] _decisionToDFA;
  protected static final PredictionContextCache _sharedContextCache =
      new PredictionContextCache();
  public static final int
      T__7 = 1, T__6 = 2, T__5 = 3, T__4 = 4, T__3 = 5, T__2 = 6, T__1 = 7, T__0 = 8, IDENTIFIER = 9,
      WHITESPACE = 10, LINE_COMMENT = 11, FILTER = 12;
  public static String[] modeNames = {
      "DEFAULT_MODE"
  };

  public static final String[] tokenNames = {
      "'\\u0000'", "'\\u0001'", "'\\u0002'", "'\\u0003'", "'\\u0004'", "'\\u0005'",
      "'\\u0006'", "'\\u0007'", "'\b'", "'\t'", "'\n'", "'\\u000B'", "'\f'"
  };
  public static final String[] ruleNames = {
      "T__7", "T__6", "T__5", "T__4", "T__3", "T__2", "T__1", "T__0", "IDENTIFIER",
      "WHITESPACE", "LINE_COMMENT", "FILTER"
  };


  public JsCommentsLexer(CharStream input) {
    super(input);
    _interp = new LexerATNSimulator(this, _ATN, _decisionToDFA, _sharedContextCache);
  }

  @Override
  public String getGrammarFileName() {
    return "JsComments.g4";
  }

  @Override
  public String[] getTokenNames() {
    return tokenNames;
  }

  @Override
  public String[] getRuleNames() {
    return ruleNames;
  }

  @Override
  public String getSerializedATN() {
    return _serializedATN;
  }

  @Override
  public String[] getModeNames() {
    return modeNames;
  }

  @Override
  public ATN getATN() {
    return _ATN;
  }

  public static final String _serializedATN =
      "\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\16}\b\1\4\2\t\2\4" +
          "\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t" +
          "\13\4\f\t\f\4\r\t\r\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3" +
          "\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5" +
          "\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3" +
          "\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b" +
          "\3\b\3\b\3\t\3\t\3\n\3\n\7\nc\n\n\f\n\16\nf\13\n\3\13\6\13i\n\13\r\13" +
          "\16\13j\3\13\3\13\3\f\3\f\3\f\3\f\7\fs\n\f\f\f\16\fv\13\f\3\f\3\f\3\r" +
          "\3\r\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r" +
          "\31\16\3\2\6\5\2C\\aac|\7\2\60\60\62;C\\aac|\5\2\13\f\17\17\"\"\4\2\f" +
          "\f\17\17\177\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2" +
          "\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2" +
          "\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5)\3\2\2\2\7\64\3\2\2\2\t\67\3\2" +
          "\2\2\13D\3\2\2\2\rH\3\2\2\2\17S\3\2\2\2\21^\3\2\2\2\23`\3\2\2\2\25h\3" +
          "\2\2\2\27n\3\2\2\2\31y\3\2\2\2\33\34\7B\2\2\34\35\7k\2\2\35\36\7o\2\2" +
          "\36\37\7r\2\2\37 \7n\2\2 !\7g\2\2!\"\7o\2\2\"#\7g\2\2#$\7p\2\2$%\7v\2" +
          "\2%&\7u\2\2&\'\7\"\2\2\'(\7}\2\2(\4\3\2\2\2)*\7B\2\2*+\7g\2\2+,\7z\2\2" +
          ",-\7v\2\2-.\7g\2\2./\7p\2\2/\60\7f\2\2\60\61\7u\2\2\61\62\7\"\2\2\62\63" +
          "\7}\2\2\63\6\3\2\2\2\64\65\7,\2\2\65\66\7\61\2\2\66\b\3\2\2\2\678\7B\2" +
          "\289\7e\2\29:\7q\2\2:;\7p\2\2;<\7u\2\2<=\7v\2\2=>\7t\2\2>?\7w\2\2?@\7" +
          "e\2\2@A\7v\2\2AB\7q\2\2BC\7t\2\2C\n\3\2\2\2DE\7\61\2\2EF\7,\2\2FG\7,\2" +
          "\2G\f\3\2\2\2HI\7B\2\2IJ\7k\2\2JK\7p\2\2KL\7v\2\2LM\7g\2\2MN\7t\2\2NO" +
          "\7h\2\2OP\7c\2\2PQ\7e\2\2QR\7g\2\2R\16\3\2\2\2ST\7B\2\2TU\7p\2\2UV\7c" +
          "\2\2VW\7o\2\2WX\7g\2\2XY\7u\2\2YZ\7r\2\2Z[\7c\2\2[\\\7e\2\2\\]\7g\2\2" +
          "]\20\3\2\2\2^_\7\177\2\2_\22\3\2\2\2`d\t\2\2\2ac\t\3\2\2ba\3\2\2\2cf\3" +
          "\2\2\2db\3\2\2\2de\3\2\2\2e\24\3\2\2\2fd\3\2\2\2gi\t\4\2\2hg\3\2\2\2i" +
          "j\3\2\2\2jh\3\2\2\2jk\3\2\2\2kl\3\2\2\2lm\b\13\2\2m\26\3\2\2\2no\7\61" +
          "\2\2op\7\61\2\2pt\3\2\2\2qs\n\5\2\2rq\3\2\2\2sv\3\2\2\2tr\3\2\2\2tu\3" +
          "\2\2\2uw\3\2\2\2vt\3\2\2\2wx\b\f\2\2x\30\3\2\2\2yz\13\2\2\2z{\3\2\2\2" +
          "{|\b\r\2\2|\32\3\2\2\2\6\2djt\3\b\2\2";
  public static final ATN _ATN =
      new ATNDeserializer().deserialize(_serializedATN.toCharArray());

  static {
    _decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
    for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
      _decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
    }
  }
}
