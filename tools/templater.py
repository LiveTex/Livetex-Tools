#!/usr/bin/python

import os
from subprocess import Popen, PIPE
from optparse import OptionParser


def defineFilesLists(path):
    return [path + os.sep + file for file in os.listdir(path)
            if file.split('.')[1] == 'd']


def getFiles(dFiles, sourcePath):
    files = list()
    filesList = open(dFiles, 'r')
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
    (options, args) = parser.parse_args()
    templatePath = args[0]
    templateName = templatePath.split('/')[-1].split('.')[0]
    outPath = options.outPath + os.sep + templateName + '.js'
    configPath = options.configPath
    sourcePath = options.sourcePath

    text = open(templatePath, 'r').read()

    fileLists = defineFilesLists(configPath)

    for fileList in fileLists:
        tag = fileList.split('.')[0].split('/')[-1]
        files = getFiles(fileList, sourcePath)
        text = replaceTag(text, tag, glue(files))

    if '%%VERSION%%' in text:
        cmd = ['git', 'describe', '--tag']
        version = Popen(cmd, stdout=PIPE).communicate()[0].strip()
        text = text.replace('%%VERSION%%', version)

    file = open(outPath, 'w')
    file.write(text)


if __name__ == "__main__":
    main()
