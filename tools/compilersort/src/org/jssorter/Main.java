package org.jssorter;

import java.nio.file.FileSystems;
import java.nio.file.Files;

public class Main {

  public static void main(String[] args) {

    JsSorter jss = new JsSorter(args.length > 0 ? args[0] : "./lib/");

    jss.getSortedList().forEach(x -> outputFile(x));

  }

  public static void outputFile(String path) {
    try {
      Files.readAllLines(FileSystems.getDefault().getPath(path)).forEach(System.out::println);
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
