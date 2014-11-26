package org.jssorter;

import java.util.ArrayList;

public class JsInspector extends JsCommentsBaseListener {

  private String filename;
  private String type;
  private String name;
  private ArrayList<String> ext = new ArrayList<>();
  private ArrayList<String> impl = new ArrayList<>();

  public JsInspector(String f) {
    filename = f;
    type = "other";
    name = "";
  }

  public String getFilename() {
    return filename;
  }

  public String getType() {
    return type;
  }

  public String getName() {
    return name;
  }

  public ArrayList<String> getExtends() {
    return ext;
  }

  public ArrayList<String> getImpl() {
    return impl;
  }

  @Override
  public void enterBody(JsCommentsParser.BodyContext ctx) {
    if (name == "" && ctx.IDENTIFIER() != null) {
      name = ctx.IDENTIFIER().getText();
    }
  }

  @Override
  public void enterMnamespace(JsCommentsParser.MnamespaceContext ctx) {
    type = "namespace";
  }

  @Override
  public void enterMinterface(JsCommentsParser.MinterfaceContext ctx) {
    type = "interface";
  }

  @Override
  public void enterConstructor(JsCommentsParser.ConstructorContext ctx) {
    type = "class";
  }

  @Override
  public void enterMimplements(JsCommentsParser.MimplementsContext ctx) {
    impl.add(ctx.IDENTIFIER().getText());
  }

  @Override
  public void enterMextends(JsCommentsParser.MextendsContext ctx) {
    ext.add(ctx.IDENTIFIER().getText());
  }

}
