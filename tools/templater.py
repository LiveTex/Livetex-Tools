#!/usr/bin/python

import re
import sys
from subprocess import Popen, PIPE


def getIndent(text, start):
    lineStart = text.rfind('\n', 0, start) + 1
    return start - lineStart


def addIndent(text, indent):
    indentedText = ''
    for line in text.splitlines():
        indentedLine = ' '*indent + line + '\n'
        indentedText += indentedLine
    return indentedText


file = open(sys.argv[1], 'r')
text = file.read()
file.close()

match = re.search('(\%\%.+\%\%)', text)

while match:
    tag = match.group(0)
    cmd = tag.strip('%')
    insertion = Popen(cmd, shell=True, stdout=PIPE).communicate()[0]
    insertion = addIndent(insertion, getIndent(text, match.start()))
    text = text.replace(tag, insertion)
    match = re.search('(\%\%.+\%\%)', text)

print text
