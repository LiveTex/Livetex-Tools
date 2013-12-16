#!/usr/bin/python2

import os
from optparse import OptionParser
from extractors.elementsExtractor import extractElements


def getPaths(path):
    paths = list()
    pathsListFile = open(path, 'r')
    pathsList = pathsListFile.read().splitlines()
    for path in pathsList:
        if path:
            paths.append('./lib/' + path)
    return paths


def main():
    usage = "usage: jstuff [--p path_to_files_set]"
    parser = OptionParser(usage)
    parser.add_option("-i", "--input",
                      action="store",
                      default='./etc/index.d',
                      dest="input",
                      help="Input path to file with project files.")
    parser.add_option("-o", "--out",
                      action="store",
                      default='./externs/index.js',
                      dest="output",
                      help="Input path to externs file.")
    (options, args) = parser.parse_args()
    paths = getPaths(options.input)
    out = options.output
    externs = ''
    if os.path.exists(out):
        os.remove(out)
    file = open(out, 'w')
    for path in paths:
        elements = extractElements(path)
        for element in elements:
            if not element.isPrivate():
                externs += element.getExterns()
                externs += '\n\n'
        externs += '\n'
    file.write(externs)
    file.close()

if __name__ == "__main__":
    main()


