#!/usr/bin/python

import re
import sys
from optparse import OptionParser
from subprocess import Popen, PIPE


def getTemplateText(templatePath):
    file = open(templatePath, 'r')
    text = file.read()
    file.close()
    return text


def getDFilesList(templateText):
    dFiles = str()
    tags = re.findall('(\%\%.+\%\%)', templateText)
    for tag in tags:
        match = re.search('[a-zA-Z0-9_-]+\.js', tag)
        if match:
            fileName = tag[match.start(): match.end() - 2] + 'd '
            dFiles += fileName
    return dFiles


def getIndent(text, start):
    lineStart = text.rfind('\n', 0, start) + 1
    return start - lineStart


def addIndent(text, indent):
    indentedText = ''
    for line in text.splitlines():
        indentedLine = ' '*indent + line + '\n'
        indentedText += indentedLine
    return indentedText


def interpretAdvanced(templateText):
    templateText = templateText.replace('.js-externs-compile ',
                                        '.js-externs-compile-advanced ')
    templateText = templateText.replace('.js-externs-compile-compressed ',
                                        '.js-externs-compile-advanced ')
    return templateText


def assemble(templateText):
    match = re.search('(\%\%.+\%\%)', templateText)
    while match:
        tag = match.group(0)
        cmd = tag.strip('%')
        insertion = Popen(cmd, shell=True, stdout=PIPE).communicate()[0]
        insertion = addIndent(insertion, getIndent(templateText, match.start()))
        templateText = templateText.replace(tag, insertion)
        match = re.search('(\%\%.+\%\%)', templateText)
    return templateText


def main():
    usage = "usage: templater [--a advanced]"
    parser = OptionParser(usage)
    parser.add_option("-a", "--advanced",
                      action="store",
                      default=False,
                      dest="advanced",
                      help="Whether to interpret commands for advanced "
                           "compilation mode or not")
    parser.add_option("-d", "--dFiles",
                      action="store",
                      default=False,
                      dest="dFiles",
                      help="Whether to get only names of required for template "
                           "d-filed or not")
    (options, args) = parser.parse_args()
    file = open('args.txt', 'w')
    file.write('ARGS: ' + str(args))
    file.close()

    templatePath = args[0]
    templateText = getTemplateText(templatePath)

    if options.advanced:
        templateText = interpretAdvanced(templateText)

    if options.dFiles:
        print getDFilesList(templateText)
    else:
        print assemble(templateText)


if __name__ == "__main__":
    main()