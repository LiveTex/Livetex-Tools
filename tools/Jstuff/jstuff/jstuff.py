#!/usr/bin/python3

from optparse import OptionParser
from collector import Collector
from jsCodeParser.jsCodeParser import parse
from externsGenerator.externsGenerator import generateExterns


collector = Collector()


def main():
    usage = "usage: jstuff [--p path_to_files_set]"
    parser = OptionParser(usage)
    parser.add_option("-p", "--path",
                      action="store",
                      default='./etc/index.d',
                      dest="paths",
                      help="Input path to file with project files.")
    (options, args) = parser.parse_args()
    parse(options.paths)
    generateExterns()


if __name__ == "__main__":
    main()


