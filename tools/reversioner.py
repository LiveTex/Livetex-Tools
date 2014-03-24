#!/usr/bin/python


import sys
import json
from collections import OrderedDict
from optparse import OptionParser
from subprocess import Popen, PIPE


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


def checkModule(module, packagePath):
    package = loadPackage(packagePath)
    modules = package['dependencies'].keys()
    if module in modules:
        return True
    return False


def getModulesVersions(module):
    cmd = 'npm --loglevel=silent show ' + module + ' versions'
    versions = Popen(cmd, shell=True, stdout=PIPE).communicate()[0]
    versions = [version.strip(' \'"')
                for version in versions.strip('[] \n').split(',\n')]
    return versions


def getHighestVersion(module):
    versions = [version.split('.') for version in getModulesVersions(module)]
    major = sorted([int(version[0]) for version in versions])[-1]
    minor = sorted([int(version[1]) for version in versions
                    if int(version[0]) == major])[-1]
    patches = [version[2].split('-') for version in versions
               if int(version[0]) == major and int(version[1]) == minor]
    patch = sorted([int(patch[0]) for patch in patches])[-1]
    build = ''
    builds = sorted([int(patchList[1]) for patchList in patches
                     if int(patchList[0]) == patch and len(patchList) > 1])
    if len(builds):
        build = builds[-1]
    version = '.'.join([str(major), str(minor), str(patch)])
    if build:
        version += '-' + str(build)
    return version.strip()


def getLatestVersion(module):
    cmd = 'npm --loglevel=silent show ' + module + ' version'
    version = Popen(cmd, shell=True, stdout=PIPE).communicate()[0]
    return version.strip()


def setHighestVersion(module, packagePath):
    package = loadPackage(packagePath)
    version = getHighestVersion(module)
    dependencies = package['dependencies']
    dependencies.__setitem__(module, version)
    package.__setitem__('dependencies', dependencies)
    writePackage(package, packagePath)


def setLatestVersion(module, packagePath):
    package = loadPackage(packagePath)
    version = getLatestVersion(module)
    dependencies = package['dependencies']
    dependencies.__setitem__(module, version)
    package.__setitem__('dependencies', dependencies)
    writePackage(package, packagePath)


def showDiffVersions(packagePath):
    count = 0
    package = loadPackage(packagePath)
    dependencies = package['dependencies']
    for module, version in dependencies.items():
        version = version.strip()
        latestVersion = getLatestVersion(module)
        highestVersion = getHighestVersion(module)
        if version != latestVersion or \
           version != highestVersion or \
           latestVersion != highestVersion:
            print('----------')
            print('MODULE:\t ' + module)
            print('VERSION: ' + version)
            print('LATEST:\t ' + latestVersion)
            print('HIGHEST: ' + highestVersion)
            count += 1
    if not count:
        print('OK: All modules versions are specified as highest and latest.')


def showModulesList(packagePath):
    package = loadPackage(packagePath)
    print ' '.join(package['dependencies'].keys())


def main():
    usage = """
    usage: reversioner [--H highest] [--L latest]
                       package.json  [module]
    """
    parser = OptionParser(usage)
    parser.add_option("-H", "--highest",
                      action="store",
                      default=False,
                      dest="highest",
                      help="")
    parser.add_option("-L", "--latest",
                      action="store",
                      default=False,
                      dest="latest",
                      help="")
    parser.add_option("-M", "--modules",
                      action="store",
                      default=False,
                      dest="modules",
                      help="")

    (options, args) = parser.parse_args()

    packagePath = args[0]

    if len(args) == 1:
        if options.modules:
            showModulesList(packagePath)
        else:
            showDiffVersions(packagePath)
    elif len(args) == 2:
        module = args[1]
        if checkModule(module, packagePath):
            if options.highest:
                setHighestVersion(module, packagePath)
            elif options.latest:
                setLatestVersion(module, packagePath)
            else:
                print('ERROR: revisioner --help')
                sys.exit(1)
        else:
            print('ERROR: Module ' + module + ' doesn\'t specified '
                                              'in package.json')
            sys.exit(1)
    else:
        print('ERROR: Wrong number of arguments')
        sys.exit(1)


if __name__ == '__main__':
    main()
