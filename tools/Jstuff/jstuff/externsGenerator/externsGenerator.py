import os
from utils import *
from collector import Collector
from jsCodeParser.elements import *


collector = Collector()


def __filterByFile(element, parameters):
    """
        Filter for 'absolute' elements.

        @param {jsCodeParser.elements.Element} element
        @param {Array.<string>} parameters Parameters for this filter -
            [fileName]

        @return {boolean} True if file includes element.
                          False if it doesn't.
    """

    path = parameters[0]
    if element.getPath() == path:
        return True
    return False


def __getElementsOfFile(project, file):
    """
        Returns the list of elements, which the file contains.

        @param {project.Project} project
        @param {string} file
        @return {Array.<jsCodeParser.elements.Element>}
    """
    elements = collector.getElements(project.getName())
    elementsOfFile =collector.selectElements(__filterByFile, elements, [file])
    return elementsOfFile


def __getElementExtern(element, indent=0):
    """
        Returns externs of the element.

        @param {jsCodeParser.elements.Element} element
        @return {string}
    """
    jsDoc = element.getJsDoc().getText()
    if isinstance(element, Constructor):
        code = element.getCode()
        parameters = extractTextBetweenTokens(code, '(')
        realizationStart = code.find(parameters) + len(parameters)
        realizationStart = code.find('{', realizationStart)
        definition = code[:realizationStart]
        realization = '{'
        attributes = element.getAttributes()
        if attributes:
            for attribute in attributes:
                realization += '\n'
                attributeExtern = __getElementExtern(attribute, 2)
                realization += attributeExtern
        realization += '};\n'
        extern = jsDoc + '\n' + ' ' * indent + definition + realization
    else:
        code = element.getCode()
        extern = jsDoc + '\n' + code + '\n'
    extern = addIntend(extern, indent)
    return extern


def __getFileExterns(project, file):
    """
        Returns externs of the file.

        @param {project.Project} project
        @param {string} file
        @return {string}
    """
    externs = '\n\n'
    elements = __getElementsOfFile(project, file)
    for element in elements:
        externs += __getElementExtern(element)
        externs += '\n\n'
    return externs


def __getProjectExterns(project):
    """
        Returns externs of the project.

        @param {project.Project} project
        @return {string}
    """
    externs = ''
    paths = project.getPaths()
    for path in paths:
        fileExterns = __getFileExterns(project, path)
        externs += fileExterns
        externs += '\n'
    return externs


def generateExterns():
    """
        Generates externs.
    """
    for project in collector.getProjects():
        out = './externs/index.js'
        if os.path.exists(out):
            os.remove(out)
        file = open(out, 'w')
        externs = __getProjectExterns(project)
        file.write(externs)
        file.close()
