package org.jssorter;

import static java.nio.file.Files.newInputStream;

import org.antlr.v4.runtime.ANTLRInputStream;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.ParseTreeWalker;

import java.io.InputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.HashMap;

public class JsSorter {

  private String libpath;
  private Boolean isAlreadySorted;
  private ArrayList<String> sorted = new ArrayList<>();
  private HashMap<String, Boolean> isSorted = new HashMap<>();
  private ArrayList<String> inter = new ArrayList<>();
  private ArrayList<String> classes = new ArrayList<>();
  private ArrayList<String> other = new ArrayList<>();
  private HashMap<String, ArrayList<String>> interGraph = new HashMap<>();
  private HashMap<String, ArrayList<String>> classGraph = new HashMap<>();
  private HashMap<String, String> nameToPath = new HashMap<>();

  public JsSorter(String libpath) {
    this.libpath = libpath;
    isAlreadySorted = false;
  }

  /**
   * Returns list of file paths sorted in the right order.
   *
   * @return list of strings
   */
  public ArrayList<String> getSortedList() {
    if (!isAlreadySorted) {
      makeSortedList();
      isAlreadySorted = true;
    }
    return sorted;
  }

  private void makeSortedList() {
    try {
      Files.walk(Paths.get(libpath)).forEach(filePath -> {
        if (Files.isRegularFile(filePath)) {
          inspectFile(filePath);
        }
      });
    } catch (IOException e) {
      e.printStackTrace();
    }

    sorted.addAll(other);

    for (final String key : interGraph.keySet()) {
      if (!isSorted.get(key)) {
        sortInterfaces(key);
      }
    }
    inter.forEach(x -> sorted.add(nameToPath.get(x)));

    for (final String key : classGraph.keySet()) {
      if (!isSorted.get(key)) {
        sortClasses(key);
      }
    }
    classes.forEach(x -> sorted.add(nameToPath.get(x)));

  }

  private void sortInterfaces(String node) {
    if (isSorted.get(node)) {
      return;
    }
    for (final String key : interGraph.get(node)) {
      sortInterfaces(key);
    }
    isSorted.put(node, true);
    inter.add(0, node);
  }

  private void sortClasses(String node) {
    if (isSorted.get(node)) {
      return;
    }
    for (final String key : classGraph.get(node)) {
      sortClasses(key);
    }
    isSorted.put(node, true);
    classes.add(0, node);
  }

  private void inspectFile(Path path) {
    ANTLRInputStream input = null;

    try (InputStream in = newInputStream(path, StandardOpenOption.READ)) {
      input = new ANTLRInputStream(in);
    } catch (IOException e) {
      e.printStackTrace();
    }

    JsCommentsLexer lexer = new JsCommentsLexer(input);

    CommonTokenStream tokens = new CommonTokenStream(lexer);

    JsCommentsParser parser = new JsCommentsParser(tokens);
    ParseTree tree = parser.program();

    ParseTreeWalker walker = new ParseTreeWalker();

    JsInspector tc = new JsInspector(path.getFileName().toString());
    walker.walk(tc, tree);

    switch (tc.getType()) {
      case "namespace":
        sorted.add(path.toString());
        break;
      case "interface":
        if (!interGraph.containsKey(tc.getName())) {
          interGraph.put(tc.getName(), new ArrayList<>());
        }
        if (!tc.getExtends().isEmpty()) {
          for (final String s : tc.getExtends()) {
            if (!interGraph.containsKey(s)) {
              interGraph.put(s, new ArrayList<>());
            }
            interGraph.get(s).add(tc.getName());
          }
        }
        isSorted.put(tc.getName(), false);
        nameToPath.put(tc.getName(), path.toString());
        break;
      case "class":
        if (!classGraph.containsKey(tc.getName())) {
          classGraph.put(tc.getName(), new ArrayList<>());
        }
        if (!tc.getImpl().isEmpty()) {
          for (final String s : tc.getExtends()) {
            if (!classGraph.containsKey(s)) {
              classGraph.put(s, new ArrayList<>());
            }
            classGraph.get(s).add(tc.getName());
          }
        }
        isSorted.put(tc.getName(), false);
        nameToPath.put(tc.getName(), path.toString());
        break;
      default:
        other.add(path.toString());
        break;
    }
  }
}
