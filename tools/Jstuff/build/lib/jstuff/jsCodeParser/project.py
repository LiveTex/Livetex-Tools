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
    def __init__(self, config):
        self.config = config
        self.globalNamespace = self.__defineGlobal(config)
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
        self.paths = self.__definePaths()

    def __defineGlobal(self, config):
        jsDoc = JsDoc('')
        name = config.getName()
        description = config.getValueByPath('parser.description')
        return GlobalNamespace('', jsDoc, name, description)

    def __definePaths(self):
        config = self.config
        projectPath = config.getValueByPath('parser.path')
        file = open(config.getValueByPath('parser.files'), 'r')
        pathsList = file.read().splitlines()
        paths = [projectPath + os.sep + 'lib' + os.sep + path
                 for path in pathsList if path]
        paths = getFiles(paths)
        return paths

    def getName(self):
        return self.config.getName()

    def getConfig(self):
        return self.config

    def getPaths(self):
        return self.paths

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
