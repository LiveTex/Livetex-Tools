#!/usr/bin/python


import os
import json
import sys
from collections import OrderedDict
from optparse import OptionParser
from subprocess import Popen, PIPE, check_call


################################################################################


def loadPackage(packagePath):
    file = open(packagePath, 'r')
    package = json.load(file, object_pairs_hook=OrderedDict)
    file.close()
    return package


def writePackage(content, packagePath):
    content = json.dumps(content, indent=2)
    file = open(packagePath, 'w')
    file.write(content)
    file.close()


################################################################################


def getBranch():
    branch = str(Popen('git branch', shell=True, stdout=PIPE).communicate()[0])
    return [line.strip('* ') for line in branch.splitlines()
              if '*' in line][0]


def gitTag(version):
    cmd = "git tag -a v" + version + " -m 'v" + version + "'"
    Popen(cmd, shell=True).wait()


def gitCommit(project, version):
    issue = raw_input("""
    issue:  """)
    status = raw_input("""
    status: """)
    message = '#' + issue + ' ' + status + ' Build ' + project + '@' + version
    cmd = 'git commit -am "' + message + '"'
    message = Popen(cmd, shell=True, stdout=PIPE).communicate()[0]
    print("""
    """ + str(message))


def gitPush(param):
    cmd = 'git push --quiet origin ' + param
    Popen(cmd, shell=True).wait()


def commitChanges(packagePath):
    package = loadPackage(packagePath)
    sys.stdin = open('/dev/tty')
    gitCommit(package['name'], package['version'])
    gitPush(getBranch())


def commitTag(version):
    gitTag(version)
    gitPush('--tags')


################################################################################


def getVersion(packagePath):
    package = loadPackage(packagePath)
    return package['version']


def getVersionFields(version):
    return [int(field) for field in version.split('.')]


################################################################################


def incrementVersion(field, packagePath):
    version = getVersion(packagePath)
    field = field.upper()
    fields = getVersionFields(version)
    if field == 'MAJOR':
        fields[0] += 1
    if field == 'MINOR':
        fields[1] += 1
    if field == 'PATCH':
        fields[2] += 1
    return '.'.join([str(f) for f in fields])


def writeVersion(version, packagePath):
    package = loadPackage(packagePath)
    package['version'] = version
    writePackage(package, packagePath)


def setVersion(packagePath):
    version = raw_input("""

    Package version:            """ + getVersion(packagePath) + """

    Increment version field:    major/minor/patch
    Set version:                <version>

    """)
    if version in ['major', 'minor', 'patch']:
        version = incrementVersion(version, packagePath)
    writeVersion(version, packagePath)
    print("""
    New version:                """ + version)
    commitChanges(packagePath)
    commitTag(version)


################################################################################
################################################################################


def main():
    usage = """
        usage: reversioner package.json
    """
    parser = OptionParser(usage)
    (options, args) = parser.parse_args()

    if len(args) == 0:
        raise Exception(usage)
    else:
        setVersion(args[0])


if __name__ == '__main__':
    main()
