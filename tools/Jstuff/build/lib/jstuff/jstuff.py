#!/usr/bin/python3

from optparse import OptionParser
from collector import Collector
from utils import *
from jsCodeParser.jsCodeParser import parse
from docsGenerator.docsGenerator import generateDocs
from externsGenerator.externsGenerator import generateExterns


collector = Collector()


def main():
    usage = "usage: jstuff [--c path_to_config] [--r result] projects"
    parser = OptionParser(usage)
    parser.add_option("-c", "--config",
                      action='store',
                      default='/etc/jstuff/config.json',
                      dest='config',
                      help='Input path to config.json file with settings '
                           'for your projects.')
    parser.add_option("-r", "--result",
                      action="store",
                      default='docs',
                      dest="result",
                      help="Input docs if you want to generate documentation.")
    (options, args) = parser.parse_args()
    configPath = options.config
    projectsNames = args
    if not projectsNames:
        projectsNames = getProjectsNames(configPath)
    result = options.result

    actionsMap = {
        'docs': generateDocs,
        'externs': generateExterns
    }

    if result in actionsMap.keys():
        action = actionsMap[result]
        parse(projectsNames, configPath)
        action()
    else:
        print('WARN: wrong required result!')


if __name__ == "__main__":
    main()


