#!/usr/bin/python

import os
import re
from subprocess import Popen, PIPE
from optparse import OptionParser


def getDFiles(path):
    return [path + os.sep + file for file in os.listdir(path)
            if file.split('.')[1] == 'd']


def getSourceFiles(dFile, sourcePath):
    files = list()
    filesList = open(dFile, 'r')
    for file in filesList.read().split('\n'):
        path = sourcePath + os.sep + file
        if os.path.isfile(path) and os.path.exists(path):
            files.append(path)
    filesList.close()
    return files


def glue(files):
    text = ''
    for file in files:
        if os.path.exists(file):
            contentFile = open(file, 'r')
            text += contentFile.read()
            text += '\n'
            contentFile.close()
    return text


def replaceTag(text, tag, content):
    fullTag = '%%' + tag.upper() + '%%'
    while fullTag in text:
        text = text.replace(fullTag, content)
    return text


def replaceTags(text, configPath, sourcePath):
    for fileList in getDFiles(configPath):
        tag = fileList.split('.')[0].split('/')[-1]
        files = getSourceFiles(fileList, sourcePath)
        text = replaceTag(text, tag, glue(files))
    return text


def replaceGitVersion(text):
    if '%%VERSION%%' in text:
        cmd = ['git', 'describe', '--tag']
        version = Popen(cmd, stdout=PIPE).communicate()[0].strip()
        text = text.replace('%%VERSION%%', version)
    return text


def createContentFiles(templatePath, configPath, sourcePath):
    text = open(templatePath, 'r').read()
    tags = [tag.strip('%').lower() for tag in re.findall('(\%\%.+\%\%)', text)]
    for tag in tags:
        jsoFilePath = configPath + os.sep + tag + '.jso'
        dFilePath = configPath + os.sep + tag + '.d'
        text = glue(getSourceFiles(dFilePath, sourcePath))
        jsoFile = open(jsoFilePath, 'w')
        jsoFile.write(text)
        jsoFile.close()


def main():
    usage = "usage: templater [-o output " \
            "-s path_to_sources -c path path_to_config]"
    parser = OptionParser(usage)
    parser.add_option("-o", "--output",
                      action="store",
                      default=os.getcwd() + os.sep + 'bin',
                      dest="outPath",
                      help="Input path to settings for templater.")
    parser.add_option("-c", "--config",
                      action="store",
                      default=os.getcwd() + os.sep + 'etc/build',
                      dest="configPath",
                      help="Input path to settings for templater.")
    parser.add_option("-s", "--source",
                      action="store",
                      default=os.getcwd() + os.sep + 'lib',
                      dest="sourcePath",
                      help="Input path to settings for templater.")
    parser.add_option("-l", "--list",
                      action="store",
                      default=None,
                      dest="list",
                      help="Input path to settings for templater.")

    (options, args) = parser.parse_args()

    templatePath = args[0]
    configPath = options.configPath
    sourcePath = options.sourcePath

    if options.list:
        createContentFiles(templatePath, configPath, sourcePath)
    else:
        template = open(templatePath, 'r')
        text = template.read()
        template.close()
        text = replaceTags(text, configPath, sourcePath)
        text = replaceGitVersion(text)
        if os.path.isdir(options.outPath):
            outPath = options.outPath + os.sep + \
                      templatePath.split('/')[-1].split('.')[0] + '.js'
        else:
            outPath = options.outPath
        file = open(outPath, 'w')
        file.write(text)
        file.close()


if __name__ == "__main__":
    main()
