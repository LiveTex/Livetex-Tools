package org.jssorter;// Generated from /home/dev/IdeaProjects/CompilerSort/JsComments.g4 by ANTLR 4.4.1-dev

import org.antlr.v4.runtime.misc.NotNull;
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link JsCommentsParser}.
 */
public interface JsCommentsListener extends ParseTreeListener {
  /**
   * Enter a parse tree produced by {@link JsCommentsParser#mextends}.
   *
   * @param ctx the parse tree
   */
  void enterMextends(@NotNull JsCommentsParser.MextendsContext ctx);

  /**
   * Exit a parse tree produced by {@link JsCommentsParser#mextends}.
   *
   * @param ctx the parse tree
   */
  void exitMextends(@NotNull JsCommentsParser.MextendsContext ctx);

  /**
   * Enter a parse tree produced by {@link JsCommentsParser#mnamespace}.
   *
   * @param ctx the parse tree
   */
  void enterMnamespace(@NotNull JsCommentsParser.MnamespaceContext ctx);

  /**
   * Exit a parse tree produced by {@link JsCommentsParser#mnamespace}.
   *
   * @param ctx the parse tree
   */
  void exitMnamespace(@NotNull JsCommentsParser.MnamespaceContext ctx);

  /**
   * Enter a parse tree produced by {@link JsCommentsParser#minterface}.
   *
   * @param ctx the parse tree
   */
  void enterMinterface(@NotNull JsCommentsParser.MinterfaceContext ctx);

  /**
   * Exit a parse tree produced by {@link JsCommentsParser#minterface}.
   *
   * @param ctx the parse tree
   */
  void exitMinterface(@NotNull JsCommentsParser.MinterfaceContext ctx);

  /**
   * Enter a parse tree produced by {@link JsCommentsParser#constructor}.
   *
   * @param ctx the parse tree
   */
  void enterConstructor(@NotNull JsCommentsParser.ConstructorContext ctx);

  /**
   * Exit a parse tree produced by {@link JsCommentsParser#constructor}.
   *
   * @param ctx the parse tree
   */
  void exitConstructor(@NotNull JsCommentsParser.ConstructorContext ctx);

  /**
   * Enter a parse tree produced by {@link JsCommentsParser#comment}.
   *
   * @param ctx the parse tree
   */
  void enterComment(@NotNull JsCommentsParser.CommentContext ctx);

  /**
   * Exit a parse tree produced by {@link JsCommentsParser#comment}.
   *
   * @param ctx the parse tree
   */
  void exitComment(@NotNull JsCommentsParser.CommentContext ctx);

  /**
   * Enter a parse tree produced by {@link JsCommentsParser#program}.
   *
   * @param ctx the parse tree
   */
  void enterProgram(@NotNull JsCommentsParser.ProgramContext ctx);

  /**
   * Exit a parse tree produced by {@link JsCommentsParser#program}.
   *
   * @param ctx the parse tree
   */
  void exitProgram(@NotNull JsCommentsParser.ProgramContext ctx);

  /**
   * Enter a parse tree produced by {@link JsCommentsParser#body}.
   *
   * @param ctx the parse tree
   */
  void enterBody(@NotNull JsCommentsParser.BodyContext ctx);

  /**
   * Exit a parse tree produced by {@link JsCommentsParser#body}.
   *
   * @param ctx the parse tree
   */
  void exitBody(@NotNull JsCommentsParser.BodyContext ctx);

  /**
   * Enter a parse tree produced by {@link JsCommentsParser#mimplements}.
   *
   * @param ctx the parse tree
   */
  void enterMimplements(@NotNull JsCommentsParser.MimplementsContext ctx);

  /**
   * Exit a parse tree produced by {@link JsCommentsParser#mimplements}.
   *
   * @param ctx the parse tree
   */
  void exitMimplements(@NotNull JsCommentsParser.MimplementsContext ctx);
}
