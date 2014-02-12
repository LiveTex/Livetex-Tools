#!/usr/bin/python

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


def getExternsFromFile(path):
    externs = ''
    for element in extractElements(path):
        if not (element.isPrivate() or element.isTest()):
            externs += element.getExterns()
            externs += '\n\n'
    externs += '\n'
    return externs


def getExternsFromFiles(settingsFilePath):
    externs = ''
    for path in getPaths(settingsFilePath):
        externs += getExternsFromFile(path)
    return externs


def main():
    usage = "usage: jstuff [--p path_to_files_set]"
    parser = OptionParser(usage)
    parser.add_option("-i", "--input",
                      action="store",
                      default=None,
                      dest="input",
                      help="Input path to file to get externs.")
    parser.add_option("-o", "--output",
                      action="store",
                      default='./externs/index.js',
                      dest="output",
                      help="Input path to externs file.")
    parser.add_option("-s", "--settings",
                      action="store",
                      default='./etc/build/content.d',
                      dest="settings",
                      help="Input path to file with project files.")
    (options, args) = parser.parse_args()

    input = options.input
    output = open(options.output, 'w')

    externs = ''

    if not input:
        externs += getExternsFromFiles(options.settings)
    else:
        externs += getExternsFromFile(input)

    output.write(externs)
    output.close()


if __name__ == "__main__":
    main()


