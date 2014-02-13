#!/usr/bin/python

# IDEAS FOR TOMORROW
#   get rid of jso
#   compiler can glue
#   LTX_IS_API in template  ??
#   externs like console


import re
import os
from optparse import OptionParser
from subprocess import Popen, PIPE


################################################################################

################################################################################


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
                  if os.path.isfile(sourcePath + os.sep + path) and
                     os.path.exists(sourcePath + os.sep + path)]
        dFile.close()
    return paths


################################################################################


def getTags(text):
    tags = [tag.strip('%').lower() for tag in re.findall('(\%\%.+\%\%)', text)
            if tag != '%%GIT-VERSION%%']
    return list(set(tags))


def replaceTag(text, tag, content):
    fullTag = '%%' + tag.upper() + '%%'
    while fullTag in text:
        text = text.replace(fullTag, content)
    return text


def replaceGitVersion(text):
    if '%%GIT-VERSION%%' in text:
        cmd = ['git', 'describe', '--tag']
        version = Popen(cmd, stdout=PIPE).communicate()[0].strip()
        text = replaceTag(text, '%%GIT-VERSION%%', version)
    return text


def replaceTags(text, configPath):
    for tag in getTags(text):
        replacerPath = configPath + os.sep + tag + '.jso'
        replacerFile = open(replacerPath, 'r')
        text = replaceTag(text, tag, replacerFile.read())
        replacerFile.close()
    return text


################################################################################


def prepareForAssembling(replacers, boxPath, externsFolderPath,
                         needCompilation, excludedFiles):
    if needCompilation:
        for replacer in [replacer for replacer in replacers
                         if replacer.split('.')[0] not in excludedFiles]:
            compile(replacer, boxPath, externsFolderPath)


################################################################################

################################################################################

def glue(dFilePaths, sourcePath, boxPath, lintExcludedFiles=[]):
    paths = list()
    for dFilePath in dFilePaths:
        text = ''
        sourceFilesPaths = getSourceFilesPaths([dFilePath], sourcePath)
        if os.path.basename(dFilePath).split('.')[0] not in lintExcludedFiles:
            lint(sourceFilesPaths, boxPath)
        for path in sourceFilesPaths:
            if os.path.exists(path):
                contentFile = open(path, 'r')
                text += contentFile.read()
                text += '\n'
                contentFile.close()
        if text:
            outPath = dFilePath[:dFilePath.rfind('.d')] + '.jso'
            paths.append(outPath)
            outFile = open(outPath, 'w')
            outFile.write(text)
            outFile.close()
    return paths


def extractExterns(filePath, externsFolderPath, boxPath):
    extractorPath = boxPath + os.sep + 'externs-extractor/externsExtractor.py'
    outputPath = externsFolderPath + os.sep + \
                 os.path.basename(filePath).split('.')[0] + '.js'
    cmd = extractorPath + ' -i ' + filePath + ' -o ' + outputPath
    print cmd
    Popen(cmd, shell=True).wait()
    return outputPath


################################################################################

################################################################################


def lint(filesPaths, boxPath):
    compilerPath = boxPath + os.sep + 'gjslint/closure_linter/gjslint.py'
    cmd = compilerPath + \
          ' --strict --custom_jsdoc_tags="namespace, event" ' + \
          ' '.join(filesPaths)
    Popen(cmd, shell=True).wait()


def compile(filePath, boxPath, externsFolderPath=None):
    compilerPath = boxPath + os.sep + 'compiler.jar'
    cmd = 'java -jar ' + \
          compilerPath + ' --warning_level VERBOSE ' \
                         '--language_in ECMASCRIPT5_STRICT ' \
                         '--compilation_level ADVANCED_OPTIMIZATIONS ' \
                         '--js ' + filePath
    if externsFolderPath:
        externsPath = extractExterns(filePath, externsFolderPath, boxPath)
        cmd = cmd + ' --externs ' + externsPath
    Popen(cmd, shell=True).wait()


################################################################################


def assemble(templatePath, sourcePath, buildFolderPath,
             boxPath, needCompilation=False, externsFolderPath='',
             compileExcludedFiles=[], lintExcludedFiles=[]):
    replacers = glue(getDFilesPaths(templatePath), sourcePath, boxPath,
                     lintExcludedFiles)
    # print(replacers, boxPath, needCompilation, externsFolderPath,
    #       compileExcludedFiles)
    prepareForAssembling(replacers, boxPath, needCompilation, externsFolderPath,
                         compileExcludedFiles)
    configPath = os.path.dirname(templatePath)
    templateFile = open(templatePath, 'r')
    text = replaceTags(templateFile.read(), configPath)
    templateFile.close()
    outputPath = buildFolderPath + os.sep + os.path.basename(templatePath)[:-1]
    outputFile = open(outputPath, 'w')
    outputFile.write(text)
    outputFile.close()


################################################################################

################################################################################


def main():
    usage = "usage: toolbox -f file -a action " \
            "-s source -b build -t toolbox " \
            "-e externs " \
            "-l lint-excluded -c compile-excluded]"
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
    parser.add_option("-s", "--source",
                      action="store",
                      default=os.getcwd() + os.sep + 'lib',
                      dest="source",
                      help="Path to sources.")
    parser.add_option("-t", "--toolbox",
                      action="store",
                      default=os.getcwd() + os.sep +
                              'node_modules/livetex-tools/tools',
                      dest="toolbox",
                      help="Path to tool box.")
    parser.add_option("-b", "--build",
                      action="store",
                      default=os.getcwd() + os.sep + 'bin',
                      dest="build",
                      help="Path to built files.")
    parser.add_option("-e", "--externs",
                      action="store",
                      default=os.getcwd() + os.sep + 'externs',
                      dest="externs",
                      help="Path to externs.")
    parser.add_option("-l", "--lint-excluded",
                      action="append",
                      default=[],
                      dest="lintExcluded",
                      help="Tags of files excluded for compilation.")
    parser.add_option("-c", "--compile-excluded",
                      action="append",
                      default=[],
                      dest="compileExcluded",
                      help="Tags of files excluded for checkup with lint.")
    (options, args) = parser.parse_args()

    if options.action == 'lint':
        lint([options.file], options.toolbox)

    if options.action == 'compile':
        compile(options.file, options.toolbox, options.externs)

    if options.action == 'assemble':
        assemble(options.file, options.source, options.build, options.toolbox,
                 lintExcludedFiles=options.lintExcluded)

    if options.action == 'compile-assemble':
        assemble(options.file, options.source, options.build, options.toolbox,
                 needCompilation=True,
                 compileExcludedFiles=options.compileExcluded,
                 lintExcludedFiles=options.lintExcluded)

    if options.action == 'ext-compile-assemble':
        assemble(options.file, options.source, options.build, options.toolbox,
                 needCompilation=True,
                 externsFolderPath=options.externs,
                 compileExcludedFiles=options.compileExcluded,
                 lintExcludedFiles=options.lintExcluded)


if __name__ == "__main__":
    main()