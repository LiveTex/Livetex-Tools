import os
from utils import *


class Container:
    """
        A hub of structure, which can contain different types of other hubs like
        aggregator or item and even the same like it is.

        @param {project.Project} project.
        @param {jsCodeParser.elements.Element} element.
        @param {string} path.

        @attribute {project.Project} project.
        @attribute {jsCodeParser.elements.Element} element Element which
                    contains other elements.
        @attribute {string} path Out path.
        @attribute {Array.<(docsGenerator.structure.Container|
                            docsGenerator.structure.Aggregator|
                            docsGenerator.structure.Item)>} components
                    Components of given element.
    """
    def __init__(self, project, element, path):
        self.project = project
        self.element = element
        self.path = path + os.sep + element.getName()
        self.components = self.__defineComponents()

    def __defineComponents(self):
        components = list()

        project = self.project
        element = self.element
        path = self.path

        namespaces = self.element.getChildren()
        classes = self.element.getClasses()
        interfaces = self.element.getInterfaces()

        components.append(Item(project, element, path))

        if isTheOnlyOne([namespaces, classes, interfaces]):
            if namespaces:
                for namespace in namespaces:
                    components.append(Container(project, namespace, path))
            else:
                group = classes or interfaces
                for item in group:
                    components.append(Item(project, item, path))
        else:
            for group in [namespaces, classes, interfaces]:
                if group:
                    components.append(Aggregator(project, group, path))
        return components

    def getPath(self):
        return self.path

    def getItems(self):
        items = list()
        components = self.components
        for component in components:
            if isinstance(component, Item):
                items.append(component)
            else:
                items = items + component.getItems()
        return items


class Aggregator:
    """
        A hub of structure, which can contain only one type of hubs like
        item or container.

        @param {project.Project} project.
        @param {Array.<jsCodeParser.elements.Element>} group Elements
                which form the group.
        @param {string} path Leveled up path.

        @attribute {project.Project} project.
        @attribute {string} group The name of elements group.
        @attribute {string} path Out path.
        @attribute {Array.<(docsGenerator.structure.Container|
                            docsGenerator.structure.Item)>} components
                    Components of given element.
    """
    def __init__(self, project, group, path):
        self.project = project
        self.group = group[0].__class__.__name__
        self.path = self.__definePath(path)
        self.components = self.__defineComponents(project, group, self.path)

    def __definePath(self, path):
        pathsMap = {
            'Namespace': path + os.sep + 'namespaces',
            'Class': path + os.sep + 'classes',
            'Interface': path + os.sep + 'interfaces'
        }
        return pathsMap[self.group]

    def __defineComponents(self, project, group, path):
        items = list()
        for element in group:
            if self.group == 'Namespace':
                items.append(Container(project, element, path))
            else:
                items.append(Item(project, element, path))
        return items

    def getItems(self):
        items = list()
        components = self.components
        for component in components:
            if isinstance(component, Item):
                items.append(component)
            else:
                items = items + component.getItems()
        return items


class Item:
    """
        A hub of structure, which can contain only element's information.

        @param {project.Project} project.
        @param {jsCodeParser.elements.Element} element.
        @param {string} path.

        @attribute {project.Project} project.
        @attribute {jsCodeParser.elements.Element} element.
        @attribute {string} templatePath Path to item's template.
        @attribute {string} path Path of item.
        @attribute {{key: value}} variables Variables for rendering a template.
    """
    def __init__(self, project, element, path):
        self.project = project
        self.element = element
        self.templatePath = self.__defineTemplatePath()
        self.path = self.__definePath(path)
        self.link = self.__defineLink()
        self.variables = self.element.getStructure()

    def __defineTemplatePath(self):
        key = self.element.__class__.__name__
        return self.project.getConfig().getValueByPath('docs.templates.' + key)

    def __definePath(self, path):
        extension = getExtension(self.templatePath)
        path = path + os.sep + self.element.getName() + extension
        return path

    def __defineLink(self):
        config = self.project.getConfig()
        outPath = config.getValueByPath('docs.out')
        path = self.path
        if not config.getValueByPath('docs.hold_extension'):
            path = cutExtension(path)
        path = os.path.relpath(path, outPath)
        linkRoot = self.project.getConfig().getValueByPath('docs.root')
        link = linkRoot + os.sep + path
        return link

    def getPath(self):
        return self.path

    def getLink(self):
        return self.link

    def getTemplatePath(self):
        return self.templatePath

    def getVariables(self):
        return self.variables

    def getProject(self):
        return self.project

    def getElement(self):
        return self.element
