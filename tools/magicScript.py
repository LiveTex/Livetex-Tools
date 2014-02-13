#!/usr/bin/python

import re
import os
from optparse import OptionParser
from subprocess import Popen, PIPE


def getDFilesPaths(templatePath):
    templateFile = open(templatePath, 'r')
    text = templateFile.read()
    templateFile.close()
    configPath = os.path.dirname(templatePath)
    return [configPath + os.sep + tag + '.d' for tag in getTags(text)]


def getSourceFilesPaths(dFilesPaths, sourcePath):
    paths = list()
    for dFilePath in dFilesPaths:
        dFile = open(dFilePath, 'r')
        paths += [sourcePath + os.sep + path
                  for path in dFile.read().split('\n')
                  if os.path.isfile(path) and os.path.exists(path)]
        dFile.close()
    return paths


################################################################################


def getTags(text):
    tags = [tag.strip('%').lower() for tag in re.findall('(\%\%.+\%\%)', text)]
    return list(set(tags))


def replaceTag(text, tag, content):
    fullTag = '%%' + tag.upper() + '%%'
    while fullTag in text:
        text = text.replace(fullTag, content)
    return text


def replaceGitVersion(text):
    if '%%VERSION%%' in text:
        cmd = ['git', 'describe', '--tag']
        version = Popen(cmd, stdout=PIPE).communicate()[0].strip()
        text = replaceTag(text, '%%VERSION%%', version)
    return text


def replaceTags(text, configPath):
    for tag in getTags(text):
        replacerPath = configPath + os.sep + tag + '.jso'
        replacerFile = open(replacerPath, 'r')
        text = replaceTag(text, tag, replacerFile.read())
        replacerFile.close()
    return text


################################################################################


def glue(dFilePaths, sourcePath, boxPath):
    paths = list()
    text = ''
    for dFilePath in dFilePaths:
        paths = getSourceFilesPaths([dFilePath], sourcePath)
        lint(path, boxPath)
        for path in paths:
            if os.path.exists(path):
                contentFile = open(path, 'r')
                text += contentFile.read()
                text += '\n'
                contentFile.close()
        if text:
            outPath = dFilePath[:dFilePath.rfind('.d')]
            paths.append(outPath)
            outFile = open(outPath, 'w')
            outFile.write(text)
            outFile.close()
    return paths


def extractExterns(filePath, externsFolderPath, boxPath):
    extractorPath = boxPath + os.sep + 'externs-extractor/externsExtractor.py'
    outputPath = externsFolderPath + os.sep + filePath.split(os.path)[-1]
    cmd = extractorPath + ' -i ' + filePath + '-o' + outputPath
    Popen(cmd, shell=True).wait()
    return outputPath




################################################################################


def lint(filesPaths, boxPath):
    compilerPath = boxPath + os.sep + 'gjslint/closure_linter/gjslint.py'
    cmd = compilerPath + \
          ' --strict --custom_jsdoc_tags="namespace, event" ' + \
          ' '.join(filesPaths)
    Popen(cmd, shell=True).wait()


def compile(filePath, boxPath, externsPath=None):
    compilerPath = boxPath + os.sep + 'compiler.jar'
    cmd = 'java -jar ' + compilerPath + ' --warning_level VERBOSE ' \
                                        '--language_in ECMASCRIPT5_STRICT ' \
                                        '--js ' + filePath
    if externsPath:
        cmd = cmd + ' --externs ' + externsPath
    Popen(cmd, shell=True).wait()


################################################################################


def assemble(templatePath, sourcePath, buildFolderPath, boxPath,
             needCompilation=False, needExterns=False,
             externsFolderPath='./externs'):
    replacers = glue(getDFilesPaths(templatePath), sourcePath, boxPath)
        externsPath = None
    if needExterns:
        externsPath = extractExterns(replacer, externsFolderPath,
                                     boxPath)
    compile(replacer, boxPath, externsPath)
    configPath = os.path.dirname(templatePath)
    templateFile = open(templatePath, 'r')
    text = replaceTags(templateFile.read(), configPath)
    templateFile.close()
    outputPath = buildFolderPath + templatePath.split(os.sep)[-1][:-1]
    outputFile = open(outputPath, 'w')
    outputFile.write(text)
    outputFile.close()


################################################################################

def main():
    usage = "usage: magic [-f file -a action -b box -s source -e externs]"
    parser = OptionParser(usage)
    parser.add_option("-f", "--file",
                      action="store",
                      default=os.getcwd() + os.sep + 'etc/build/index.jst',
                      dest="file",
                      help="Path to file to operate.")
    parser.add_option("-a", "--action",
                      action="store",
                      default='assemble',
                      dest="action",
                      help="Action to do.")
    parser.add_option("-b", "--box",
                      action="store",
                      default=os.getcwd() + os.sep +
                              'node_modules/livetex-tools/tools',
                      dest="box",
                      help="Path to tool box.")
    parser.add_option("-s", "--source",
                      action="store",
                      default=os.getcwd() + os.sep +
                              'lib',
                      dest="source",
                      help="Path to sources.")
    parser.add_option("-e", "--externs",
                      action="store",
                      default=os.getcwd() + os.sep +
                              'externs',
                      dest="externs",
                      help="Path to externs.")
    (options, args) = parser.parse_args()

    # sourcesFilesPaths =

    actions = {
        'lint': [options.file], options.box),
        'compile': compile([options.file], )
    }


if __name__ == "__main__":
    main()