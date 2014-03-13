#!/usr/bin/python


import json
import subprocess


def getVersions(module):
    cmd = 'npm show ' + module + ' versions'
    versions = subprocess.Popen(cmd,
                                shell=True,
                                stdout=subprocess.PIPE).communicate()[0]
    versions = [version.strip(' \'"')
                for version in versions.strip('[] \n').split(',\n')]
    return versions


def getHighestVersion(module):
    versions = [version.split('.') for version in getVersions(module)]
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
        version += '-' + build
    return version.strip()


def getLatestVersion(module):
    cmd = 'npm show ' + module + ' version'
    version = subprocess.Popen(cmd,
                               shell=True,
                               stdout=subprocess.PIPE).communicate()[0]
    return version.strip()


def showVersions(packagePath):
    file = open(packagePath, 'r')
    package = json.load(file)
    file.close()
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

showVersions('./package.json')
