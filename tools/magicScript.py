#!/usr/bin/python

import re
import os
from optparse import OptionParser


def getDFiles(templatePath):
    templateFile = open(templatePath, 'r')
    text = templateFile.read()
    templateFile.close()
    tags = [tag.strip('%').lower() for tag in re.findall('(\%\%.+\%\%)', text)]
    configPath = os.path.dirname(templatePath)
    return [configPath + os.sep + tag + '.d' for tag in tags]


def getSourceFiles(dFilePath, sourcePath):
    files = list()
    dFile = open(dFilePath, 'r')
    for file in dFile.read().split('\n'):
        path = sourcePath + os.sep + file
        if os.path.isfile(path) and os.path.exists(path):
            files.append(path)
    dFile.close()
    return files

################################################################################


def glue(files):
    text = ''
    for file in files:
        if os.path.exists(file):
            contentFile = open(file, 'r')
            text += contentFile.read()
            text += '\n'
            contentFile.close()
    return text


def compile():
    pass


def lint():
    pass


def assemble():
    pass


def main():
    usage = "usage: magic [-t template]"
    parser = OptionParser(usage)
    parser.add_option("-t", "--template",
                      action="store",
                      default=os.getcwd() + os.sep + 'etc/build/index.jst',
                      dest="template",
                      help="Path to template.")
    (options, args) = parser.parse_args()
    print(getDFiles(options.template))


if __name__ == "__main__":
    main()