package org.jssorter;// Generated from /home/dev/IdeaProjects/CompilerSort/JsComments.g4 by ANTLR 4.4.1-dev

import org.antlr.v4.runtime.misc.NotNull;
import org.antlr.v4.runtime.tree.AbstractParseTreeVisitor;

/**
 * This class provides an empty implementation of {@link JsSorter.JsSorter.JsCommentsVisitor},
 * which can be extended to create a visitor which only needs to handle a subset
 * of the available methods.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 *            operations with no return type.
 */
public class JsCommentsBaseVisitor<T> extends AbstractParseTreeVisitor<T> implements JsCommentsVisitor<T> {
  /**
   * {@inheritDoc}
   * <p>
   * <p>The default implementation returns the result of calling
   * {@link #visitChildren} on {@code ctx}.</p>
   */
  @Override
  public T visitMextends(@NotNull JsCommentsParser.MextendsContext ctx) {
    return visitChildren(ctx);
  }

  /**
   * {@inheritDoc}
   * <p>
   * <p>The default implementation returns the result of calling
   * {@link #visitChildren} on {@code ctx}.</p>
   */
  @Override
  public T visitMnamespace(@NotNull JsCommentsParser.MnamespaceContext ctx) {
    return visitChildren(ctx);
  }

  /**
   * {@inheritDoc}
   * <p>
   * <p>The default implementation returns the result of calling
   * {@link #visitChildren} on {@code ctx}.</p>
   */
  @Override
  public T visitMinterface(@NotNull JsCommentsParser.MinterfaceContext ctx) {
    return visitChildren(ctx);
  }

  /**
   * {@inheritDoc}
   * <p>
   * <p>The default implementation returns the result of calling
   * {@link #visitChildren} on {@code ctx}.</p>
   */
  @Override
  public T visitConstructor(@NotNull JsCommentsParser.ConstructorContext ctx) {
    return visitChildren(ctx);
  }

  /**
   * {@inheritDoc}
   * <p>
   * <p>The default implementation returns the result of calling
   * {@link #visitChildren} on {@code ctx}.</p>
   */
  @Override
  public T visitComment(@NotNull JsCommentsParser.CommentContext ctx) {
    return visitChildren(ctx);
  }

  /**
   * {@inheritDoc}
   * <p>
   * <p>The default implementation returns the result of calling
   * {@link #visitChildren} on {@code ctx}.</p>
   */
  @Override
  public T visitProgram(@NotNull JsCommentsParser.ProgramContext ctx) {
    return visitChildren(ctx);
  }

  /**
   * {@inheritDoc}
   * <p>
   * <p>The default implementation returns the result of calling
   * {@link #visitChildren} on {@code ctx}.</p>
   */
  @Override
  public T visitBody(@NotNull JsCommentsParser.BodyContext ctx) {
    return visitChildren(ctx);
  }

  /**
   * {@inheritDoc}
   * <p>
   * <p>The default implementation returns the result of calling
   * {@link #visitChildren} on {@code ctx}.</p>
   */
  @Override
  public T visitMimplements(@NotNull JsCommentsParser.MimplementsContext ctx) {
    return visitChildren(ctx);
  }
}
