from jsCodeParser.elements import GlobalNamespace
from jsCodeParser.jsDoc import JsDoc
from utils import *


class Project:
    """
        Project configured with config.json file.

        @param {config.Config} config Configuration of a project.

        @attribute {config.Config} config Configuration of a project.
        @attribute {jsCodeParser.} globalNamespace Global scope of project.
        @attribute {{group: Array.<jsCodeParser.elements.Element>}} elements
                    Elements of project.
    """
    def __init__(self, pathsFile):
        self.pathsFile = pathsFile
        self.globalNamespace = GlobalNamespace('', JsDoc(''), '', '')
        self.elements = {
            'all': [],
            'Namespace': [],
            'Class': [],
            'Method': [],
            'Interface': [],
            'Property': [],
            'Typedef': [],
            'Enumeration': [],
        }

    def getName(self):
        return ''

    def getPaths(self):
        file = open(self.pathsFile, 'r')
        pathsList = file.read().splitlines()
        paths = ['lib' + os.sep + path
                 for path in pathsList if path]
        paths = getFiles(paths)
        return paths

    def getGlobal(self):
        return self.globalNamespace
    
    def getElements(self, group=None):
        if group:
            return self.elements[group]
        return self.elements['all']

    def addElement(self, element):
        self.elements['all'].append(element)
        key = element.__class__.__name__
        self.elements[key].append(element)
