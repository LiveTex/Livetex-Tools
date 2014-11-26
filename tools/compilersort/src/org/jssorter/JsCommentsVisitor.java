package org.jssorter;// Generated from /home/dev/IdeaProjects/CompilerSort/JsComments.g4 by ANTLR 4.4.1-dev

import org.antlr.v4.runtime.misc.NotNull;
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link JsCommentsParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 *            operations with no return type.
 */
public interface JsCommentsVisitor<T> extends ParseTreeVisitor<T> {
  /**
   * Visit a parse tree produced by {@link JsCommentsParser#mextends}.
   *
   * @param ctx the parse tree
   * @return the visitor result
   */
  T visitMextends(@NotNull JsCommentsParser.MextendsContext ctx);

  /**
   * Visit a parse tree produced by {@link JsCommentsParser#mnamespace}.
   *
   * @param ctx the parse tree
   * @return the visitor result
   */
  T visitMnamespace(@NotNull JsCommentsParser.MnamespaceContext ctx);

  /**
   * Visit a parse tree produced by {@link JsCommentsParser#minterface}.
   *
   * @param ctx the parse tree
   * @return the visitor result
   */
  T visitMinterface(@NotNull JsCommentsParser.MinterfaceContext ctx);

  /**
   * Visit a parse tree produced by {@link JsCommentsParser#constructor}.
   *
   * @param ctx the parse tree
   * @return the visitor result
   */
  T visitConstructor(@NotNull JsCommentsParser.ConstructorContext ctx);

  /**
   * Visit a parse tree produced by {@link JsCommentsParser#comment}.
   *
   * @param ctx the parse tree
   * @return the visitor result
   */
  T visitComment(@NotNull JsCommentsParser.CommentContext ctx);

  /**
   * Visit a parse tree produced by {@link JsCommentsParser#program}.
   *
   * @param ctx the parse tree
   * @return the visitor result
   */
  T visitProgram(@NotNull JsCommentsParser.ProgramContext ctx);

  /**
   * Visit a parse tree produced by {@link JsCommentsParser#body}.
   *
   * @param ctx the parse tree
   * @return the visitor result
   */
  T visitBody(@NotNull JsCommentsParser.BodyContext ctx);

  /**
   * Visit a parse tree produced by {@link JsCommentsParser#mimplements}.
   *
   * @param ctx the parse tree
   * @return the visitor result
   */
  T visitMimplements(@NotNull JsCommentsParser.MimplementsContext ctx);
}
