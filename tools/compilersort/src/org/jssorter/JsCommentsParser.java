// Generated from /home/dev/IdeaProjects/CompilerSort/JsComments.g4 by ANTLR 4.4.1-dev
package org.jssorter;

import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;

import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class JsCommentsParser extends Parser {
  static {
    RuntimeMetaData.checkVersion("4.4.1-dev", RuntimeMetaData.VERSION);
  }

  protected static final DFA[] _decisionToDFA;
  protected static final PredictionContextCache _sharedContextCache =
      new PredictionContextCache();
  public static final int
      T__7 = 1, T__6 = 2, T__5 = 3, T__4 = 4, T__3 = 5, T__2 = 6, T__1 = 7, T__0 = 8, IDENTIFIER = 9,
      WHITESPACE = 10, LINE_COMMENT = 11, MULTILINE_COMMENT = 12, FILTER = 13;
  public static final String[] tokenNames = {
      "<INVALID>", "'@implements {'", "'@extends {'", "'*/'", "'@constructor'",
      "'/**'", "'@interface'", "'@namespace'", "'}'", "IDENTIFIER", "WHITESPACE",
      "LINE_COMMENT", "MULTILINE_COMMENT", "FILTER"
  };
  public static final int
      RULE_program = 0, RULE_body = 1, RULE_comment = 2, RULE_mnamespace = 3,
      RULE_minterface = 4, RULE_constructor = 5, RULE_mextends = 6, RULE_mimplements = 7;
  public static final String[] ruleNames = {
      "program", "body", "comment", "mnamespace", "minterface", "constructor",
      "mextends", "mimplements"
  };

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
  public ATN getATN() {
    return _ATN;
  }

  public JsCommentsParser(TokenStream input) {
    super(input);
    _interp = new ParserATNSimulator(this, _ATN, _decisionToDFA, _sharedContextCache);
  }

  public static class ProgramContext extends ParserRuleContext {
    public BodyContext body(int i) {
      return getRuleContext(BodyContext.class, i);
    }

    public List<BodyContext> body() {
      return getRuleContexts(BodyContext.class);
    }

    public ProgramContext(ParserRuleContext parent, int invokingState) {
      super(parent, invokingState);
    }

    @Override
    public int getRuleIndex() {
      return RULE_program;
    }

    @Override
    public void enterRule(ParseTreeListener listener) {
      if (listener instanceof JsCommentsListener) ((JsCommentsListener) listener).enterProgram(this);
    }

    @Override
    public void exitRule(ParseTreeListener listener) {
      if (listener instanceof JsCommentsListener) ((JsCommentsListener) listener).exitProgram(this);
    }
  }

  public final ProgramContext program() throws RecognitionException {
    ProgramContext _localctx = new ProgramContext(_ctx, getState());
    enterRule(_localctx, 0, RULE_program);
    int _la;
    try {
      enterOuterAlt(_localctx, 1);
      {
        setState(17);
        _errHandler.sync(this);
        _la = _input.LA(1);
        do {
          {
            {
              setState(16);
              body();
            }
          }
          setState(19);
          _errHandler.sync(this);
          _la = _input.LA(1);
        } while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__3) | (1L << T__0) | (1L << IDENTIFIER))) != 0));
      }
    } catch (RecognitionException re) {
      _localctx.exception = re;
      _errHandler.reportError(this, re);
      _errHandler.recover(this, re);
    } finally {
      exitRule();
    }
    return _localctx;
  }

  public static class BodyContext extends ParserRuleContext {
    public CommentContext comment() {
      return getRuleContext(CommentContext.class, 0);
    }

    public TerminalNode IDENTIFIER() {
      return getToken(JsCommentsParser.IDENTIFIER, 0);
    }

    public BodyContext(ParserRuleContext parent, int invokingState) {
      super(parent, invokingState);
    }

    @Override
    public int getRuleIndex() {
      return RULE_body;
    }

    @Override
    public void enterRule(ParseTreeListener listener) {
      if (listener instanceof JsCommentsListener) ((JsCommentsListener) listener).enterBody(this);
    }

    @Override
    public void exitRule(ParseTreeListener listener) {
      if (listener instanceof JsCommentsListener) ((JsCommentsListener) listener).exitBody(this);
    }
  }

  public final BodyContext body() throws RecognitionException {
    BodyContext _localctx = new BodyContext(_ctx, getState());
    enterRule(_localctx, 2, RULE_body);
    int _la;
    try {
      setState(26);
      switch (_input.LA(1)) {
        case T__3:
          enterOuterAlt(_localctx, 1);
        {
          setState(21);
          match(T__3);
          setState(22);
          comment();
          setState(23);
          match(T__5);
        }
        break;
        case T__0:
        case IDENTIFIER:
          enterOuterAlt(_localctx, 2);
        {
          setState(25);
          _la = _input.LA(1);
          if (!(_la == T__0 || _la == IDENTIFIER)) {
            _errHandler.recoverInline(this);
          }
          consume();
        }
        break;
        default:
          throw new NoViableAltException(this);
      }
    } catch (RecognitionException re) {
      _localctx.exception = re;
      _errHandler.reportError(this, re);
      _errHandler.recover(this, re);
    } finally {
      exitRule();
    }
    return _localctx;
  }

  public static class CommentContext extends ParserRuleContext {
    public MnamespaceContext mnamespace() {
      return getRuleContext(MnamespaceContext.class, 0);
    }

    public MinterfaceContext minterface() {
      return getRuleContext(MinterfaceContext.class, 0);
    }

    public ConstructorContext constructor() {
      return getRuleContext(ConstructorContext.class, 0);
    }

    public TerminalNode IDENTIFIER(int i) {
      return getToken(JsCommentsParser.IDENTIFIER, i);
    }

    public List<TerminalNode> IDENTIFIER() {
      return getTokens(JsCommentsParser.IDENTIFIER);
    }

    public CommentContext(ParserRuleContext parent, int invokingState) {
      super(parent, invokingState);
    }

    @Override
    public int getRuleIndex() {
      return RULE_comment;
    }

    @Override
    public void enterRule(ParseTreeListener listener) {
      if (listener instanceof JsCommentsListener) ((JsCommentsListener) listener).enterComment(this);
    }

    @Override
    public void exitRule(ParseTreeListener listener) {
      if (listener instanceof JsCommentsListener) ((JsCommentsListener) listener).exitComment(this);
    }
  }

  public final CommentContext comment() throws RecognitionException {
    CommentContext _localctx = new CommentContext(_ctx, getState());
    enterRule(_localctx, 4, RULE_comment);
    int _la;
    try {
      int _alt;
      setState(51);
      switch (getInterpreter().adaptivePredict(_input, 6, _ctx)) {
        case 1:
          enterOuterAlt(_localctx, 1);
        {
          setState(31);
          _errHandler.sync(this);
          _alt = getInterpreter().adaptivePredict(_input, 2, _ctx);
          while (_alt != 1 && _alt != org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER) {
            if (_alt == 1 + 1) {
              {
                {
                  setState(28);
                  _la = _input.LA(1);
                  if (!(_la == T__0 || _la == IDENTIFIER)) {
                    _errHandler.recoverInline(this);
                  }
                  consume();
                }
              }
            }
            setState(33);
            _errHandler.sync(this);
            _alt = getInterpreter().adaptivePredict(_input, 2, _ctx);
          }
          setState(37);
          switch (_input.LA(1)) {
            case T__2: {
              setState(34);
              minterface();
            }
            break;
            case T__7:
            case T__6:
            case T__4: {
              setState(35);
              constructor();
            }
            break;
            case T__1: {
              setState(36);
              mnamespace();
            }
            break;
            default:
              throw new NoViableAltException(this);
          }
          setState(42);
          _errHandler.sync(this);
          _alt = getInterpreter().adaptivePredict(_input, 4, _ctx);
          while (_alt != 1 && _alt != org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER) {
            if (_alt == 1 + 1) {
              {
                {
                  setState(39);
                  _la = _input.LA(1);
                  if (!(_la == T__0 || _la == IDENTIFIER)) {
                    _errHandler.recoverInline(this);
                  }
                  consume();
                }
              }
            }
            setState(44);
            _errHandler.sync(this);
            _alt = getInterpreter().adaptivePredict(_input, 4, _ctx);
          }
        }
        break;
        case 2:
          enterOuterAlt(_localctx, 2);
        {
          setState(48);
          _errHandler.sync(this);
          _alt = getInterpreter().adaptivePredict(_input, 5, _ctx);
          while (_alt != 1 && _alt != org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER) {
            if (_alt == 1 + 1) {
              {
                {
                  setState(45);
                  _la = _input.LA(1);
                  if (!(_la == T__0 || _la == IDENTIFIER)) {
                    _errHandler.recoverInline(this);
                  }
                  consume();
                }
              }
            }
            setState(50);
            _errHandler.sync(this);
            _alt = getInterpreter().adaptivePredict(_input, 5, _ctx);
          }
        }
        break;
      }
    } catch (RecognitionException re) {
      _localctx.exception = re;
      _errHandler.reportError(this, re);
      _errHandler.recover(this, re);
    } finally {
      exitRule();
    }
    return _localctx;
  }

  public static class MnamespaceContext extends ParserRuleContext {
    public MnamespaceContext(ParserRuleContext parent, int invokingState) {
      super(parent, invokingState);
    }

    @Override
    public int getRuleIndex() {
      return RULE_mnamespace;
    }

    @Override
    public void enterRule(ParseTreeListener listener) {
      if (listener instanceof JsCommentsListener) ((JsCommentsListener) listener).enterMnamespace(this);
    }

    @Override
    public void exitRule(ParseTreeListener listener) {
      if (listener instanceof JsCommentsListener) ((JsCommentsListener) listener).exitMnamespace(this);
    }
  }

  public final MnamespaceContext mnamespace() throws RecognitionException {
    MnamespaceContext _localctx = new MnamespaceContext(_ctx, getState());
    enterRule(_localctx, 6, RULE_mnamespace);
    try {
      enterOuterAlt(_localctx, 1);
      {
        setState(53);
        match(T__1);
      }
    } catch (RecognitionException re) {
      _localctx.exception = re;
      _errHandler.reportError(this, re);
      _errHandler.recover(this, re);
    } finally {
      exitRule();
    }
    return _localctx;
  }

  public static class MinterfaceContext extends ParserRuleContext {
    public List<MextendsContext> mextends() {
      return getRuleContexts(MextendsContext.class);
    }

    public MextendsContext mextends(int i) {
      return getRuleContext(MextendsContext.class, i);
    }

    public MinterfaceContext(ParserRuleContext parent, int invokingState) {
      super(parent, invokingState);
    }

    @Override
    public int getRuleIndex() {
      return RULE_minterface;
    }

    @Override
    public void enterRule(ParseTreeListener listener) {
      if (listener instanceof JsCommentsListener) ((JsCommentsListener) listener).enterMinterface(this);
    }

    @Override
    public void exitRule(ParseTreeListener listener) {
      if (listener instanceof JsCommentsListener) ((JsCommentsListener) listener).exitMinterface(this);
    }
  }

  public final MinterfaceContext minterface() throws RecognitionException {
    MinterfaceContext _localctx = new MinterfaceContext(_ctx, getState());
    enterRule(_localctx, 8, RULE_minterface);
    int _la;
    try {
      enterOuterAlt(_localctx, 1);
      {
        setState(55);
        match(T__2);
        setState(59);
        _errHandler.sync(this);
        _la = _input.LA(1);
        while (_la == T__6) {
          {
            {
              setState(56);
              mextends();
            }
          }
          setState(61);
          _errHandler.sync(this);
          _la = _input.LA(1);
        }
      }
    } catch (RecognitionException re) {
      _localctx.exception = re;
      _errHandler.reportError(this, re);
      _errHandler.recover(this, re);
    } finally {
      exitRule();
    }
    return _localctx;
  }

  public static class ConstructorContext extends ParserRuleContext {
    public List<MextendsContext> mextends() {
      return getRuleContexts(MextendsContext.class);
    }

    public MimplementsContext mimplements(int i) {
      return getRuleContext(MimplementsContext.class, i);
    }

    public MextendsContext mextends(int i) {
      return getRuleContext(MextendsContext.class, i);
    }

    public List<MimplementsContext> mimplements() {
      return getRuleContexts(MimplementsContext.class);
    }

    public ConstructorContext(ParserRuleContext parent, int invokingState) {
      super(parent, invokingState);
    }

    @Override
    public int getRuleIndex() {
      return RULE_constructor;
    }

    @Override
    public void enterRule(ParseTreeListener listener) {
      if (listener instanceof JsCommentsListener) ((JsCommentsListener) listener).enterConstructor(this);
    }

    @Override
    public void exitRule(ParseTreeListener listener) {
      if (listener instanceof JsCommentsListener) ((JsCommentsListener) listener).exitConstructor(this);
    }
  }

  public final ConstructorContext constructor() throws RecognitionException {
    ConstructorContext _localctx = new ConstructorContext(_ctx, getState());
    enterRule(_localctx, 10, RULE_constructor);
    int _la;
    try {
      setState(88);
      switch (getInterpreter().adaptivePredict(_input, 12, _ctx)) {
        case 1:
          enterOuterAlt(_localctx, 1);
        {
          setState(62);
          match(T__4);
          setState(66);
          _errHandler.sync(this);
          _la = _input.LA(1);
          while (_la == T__6) {
            {
              {
                setState(63);
                mextends();
              }
            }
            setState(68);
            _errHandler.sync(this);
            _la = _input.LA(1);
          }
          setState(72);
          _errHandler.sync(this);
          _la = _input.LA(1);
          while (_la == T__7) {
            {
              {
                setState(69);
                mimplements();
              }
            }
            setState(74);
            _errHandler.sync(this);
            _la = _input.LA(1);
          }
        }
        break;
        case 2:
          enterOuterAlt(_localctx, 2);
        {
          setState(78);
          _errHandler.sync(this);
          _la = _input.LA(1);
          while (_la == T__6) {
            {
              {
                setState(75);
                mextends();
              }
            }
            setState(80);
            _errHandler.sync(this);
            _la = _input.LA(1);
          }
          setState(84);
          _errHandler.sync(this);
          _la = _input.LA(1);
          while (_la == T__7) {
            {
              {
                setState(81);
                mimplements();
              }
            }
            setState(86);
            _errHandler.sync(this);
            _la = _input.LA(1);
          }
          setState(87);
          match(T__4);
        }
        break;
      }
    } catch (RecognitionException re) {
      _localctx.exception = re;
      _errHandler.reportError(this, re);
      _errHandler.recover(this, re);
    } finally {
      exitRule();
    }
    return _localctx;
  }

  public static class MextendsContext extends ParserRuleContext {
    public TerminalNode IDENTIFIER() {
      return getToken(JsCommentsParser.IDENTIFIER, 0);
    }

    public MextendsContext(ParserRuleContext parent, int invokingState) {
      super(parent, invokingState);
    }

    @Override
    public int getRuleIndex() {
      return RULE_mextends;
    }

    @Override
    public void enterRule(ParseTreeListener listener) {
      if (listener instanceof JsCommentsListener) ((JsCommentsListener) listener).enterMextends(this);
    }

    @Override
    public void exitRule(ParseTreeListener listener) {
      if (listener instanceof JsCommentsListener) ((JsCommentsListener) listener).exitMextends(this);
    }
  }

  public final MextendsContext mextends() throws RecognitionException {
    MextendsContext _localctx = new MextendsContext(_ctx, getState());
    enterRule(_localctx, 12, RULE_mextends);
    try {
      enterOuterAlt(_localctx, 1);
      {
        setState(90);
        match(T__6);
        setState(91);
        match(IDENTIFIER);
        setState(92);
        match(T__0);
      }
    } catch (RecognitionException re) {
      _localctx.exception = re;
      _errHandler.reportError(this, re);
      _errHandler.recover(this, re);
    } finally {
      exitRule();
    }
    return _localctx;
  }

  public static class MimplementsContext extends ParserRuleContext {
    public TerminalNode IDENTIFIER() {
      return getToken(JsCommentsParser.IDENTIFIER, 0);
    }

    public MimplementsContext(ParserRuleContext parent, int invokingState) {
      super(parent, invokingState);
    }

    @Override
    public int getRuleIndex() {
      return RULE_mimplements;
    }

    @Override
    public void enterRule(ParseTreeListener listener) {
      if (listener instanceof JsCommentsListener) ((JsCommentsListener) listener).enterMimplements(this);
    }

    @Override
    public void exitRule(ParseTreeListener listener) {
      if (listener instanceof JsCommentsListener) ((JsCommentsListener) listener).exitMimplements(this);
    }
  }

  public final MimplementsContext mimplements() throws RecognitionException {
    MimplementsContext _localctx = new MimplementsContext(_ctx, getState());
    enterRule(_localctx, 14, RULE_mimplements);
    try {
      enterOuterAlt(_localctx, 1);
      {
        setState(94);
        match(T__7);
        setState(95);
        match(IDENTIFIER);
        setState(96);
        match(T__0);
      }
    } catch (RecognitionException re) {
      _localctx.exception = re;
      _errHandler.reportError(this, re);
      _errHandler.recover(this, re);
    } finally {
      exitRule();
    }
    return _localctx;
  }

  public static final String _serializedATN =
      "\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\17e\4\2\t\2\4\3\t" +
          "\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\3\2\6\2\24\n\2\r\2" +
          "\16\2\25\3\3\3\3\3\3\3\3\3\3\5\3\35\n\3\3\4\7\4 \n\4\f\4\16\4#\13\4\3" +
          "\4\3\4\3\4\5\4(\n\4\3\4\7\4+\n\4\f\4\16\4.\13\4\3\4\7\4\61\n\4\f\4\16" +
          "\4\64\13\4\5\4\66\n\4\3\5\3\5\3\6\3\6\7\6<\n\6\f\6\16\6?\13\6\3\7\3\7" +
          "\7\7C\n\7\f\7\16\7F\13\7\3\7\7\7I\n\7\f\7\16\7L\13\7\3\7\7\7O\n\7\f\7" +
          "\16\7R\13\7\3\7\7\7U\n\7\f\7\16\7X\13\7\3\7\5\7[\n\7\3\b\3\b\3\b\3\b\3" +
          "\t\3\t\3\t\3\t\3\t\5!,\62\2\n\2\4\6\b\n\f\16\20\2\3\3\2\n\13j\2\23\3\2" +
          "\2\2\4\34\3\2\2\2\6\65\3\2\2\2\b\67\3\2\2\2\n9\3\2\2\2\fZ\3\2\2\2\16\\" +
          "\3\2\2\2\20`\3\2\2\2\22\24\5\4\3\2\23\22\3\2\2\2\24\25\3\2\2\2\25\23\3" +
          "\2\2\2\25\26\3\2\2\2\26\3\3\2\2\2\27\30\7\7\2\2\30\31\5\6\4\2\31\32\7" +
          "\5\2\2\32\35\3\2\2\2\33\35\t\2\2\2\34\27\3\2\2\2\34\33\3\2\2\2\35\5\3" +
          "\2\2\2\36 \t\2\2\2\37\36\3\2\2\2 #\3\2\2\2!\"\3\2\2\2!\37\3\2\2\2\"\'" +
          "\3\2\2\2#!\3\2\2\2$(\5\n\6\2%(\5\f\7\2&(\5\b\5\2\'$\3\2\2\2\'%\3\2\2\2" +
          "\'&\3\2\2\2(,\3\2\2\2)+\t\2\2\2*)\3\2\2\2+.\3\2\2\2,-\3\2\2\2,*\3\2\2" +
          "\2-\66\3\2\2\2.,\3\2\2\2/\61\t\2\2\2\60/\3\2\2\2\61\64\3\2\2\2\62\63\3" +
          "\2\2\2\62\60\3\2\2\2\63\66\3\2\2\2\64\62\3\2\2\2\65!\3\2\2\2\65\62\3\2" +
          "\2\2\66\7\3\2\2\2\678\7\t\2\28\t\3\2\2\29=\7\b\2\2:<\5\16\b\2;:\3\2\2" +
          "\2<?\3\2\2\2=;\3\2\2\2=>\3\2\2\2>\13\3\2\2\2?=\3\2\2\2@D\7\6\2\2AC\5\16" +
          "\b\2BA\3\2\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2EJ\3\2\2\2FD\3\2\2\2GI\5\20" +
          "\t\2HG\3\2\2\2IL\3\2\2\2JH\3\2\2\2JK\3\2\2\2K[\3\2\2\2LJ\3\2\2\2MO\5\16" +
          "\b\2NM\3\2\2\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2QV\3\2\2\2RP\3\2\2\2SU\5\20" +
          "\t\2TS\3\2\2\2UX\3\2\2\2VT\3\2\2\2VW\3\2\2\2WY\3\2\2\2XV\3\2\2\2Y[\7\6" +
          "\2\2Z@\3\2\2\2ZP\3\2\2\2[\r\3\2\2\2\\]\7\4\2\2]^\7\13\2\2^_\7\n\2\2_\17" +
          "\3\2\2\2`a\7\3\2\2ab\7\13\2\2bc\7\n\2\2c\21\3\2\2\2\17\25\34!\',\62\65" +
          "=DJPVZ";
  public static final ATN _ATN =
      new ATNDeserializer().deserialize(_serializedATN.toCharArray());

  static {
    _decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
    for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
      _decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
    }
  }
}
