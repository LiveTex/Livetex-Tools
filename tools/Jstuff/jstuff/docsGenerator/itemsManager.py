import os
import shutil
import jinja2
from utils import *


class ItemsManager:
    """
        Entity, which manages items:
        creates, links and deletes them.
        
        @param {*} templateEnv.
        
        @attribute {*} templateEnv Environment for template.
        @attribute {Array.<docsGenerator.structure.Item>} items.
        @attribute {{name: path}} links.
    """
    def __init__(self, templateEnv=None):
        if not templateEnv:
            templateEnv = jinja2.Environment(
                loader=jinja2.FileSystemLoader(searchpath="/")) 
        self.templateEnv = templateEnv
        self.items = list()
        self.links = dict()

    def __createFile(self, path):
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        if os.path.exists(path):
            self.delete(path)
        open(path, 'w').close()

    def __addLink(self, name, path):
        if name not in self.links.keys():
            self.links[name] = path

    def __addLinkByItem(self, item):
        element = item.getElement()
        name = element.getName()
        link = item.getLink()

        self.__addLink(name, link)
        if element.__class__.__name__ == 'Namespace':
            components = [element for element in element.getMethods()
                          if not element.isPrivate()] + \
                [element for element in element.getProperties()
                 if not element.isPrivate()] + \
                [element for element in element.getTypedefs()
                 if not element.isPrivate()] + \
                [element for element in element.getEnums()
                 if not element.isPrivate()]
            for component in components:
                name = component.getName()
                self.__addLink(name, link)

    def delete(self, path):
        if os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
            elif os.path.isfile(path):
                os.remove(path)

    def create(self, item):
        path = item.getPath()
        self.__createFile(path)
        templatePath = item.getTemplatePath()
        template = self.templateEnv.get_template(templatePath)
        variables = item.getVariables()
        outText = template.render(variables)
        outText = outText.replace('.prototype.', '#')
        file = open(path, 'w')
        file.write(outText)
        file.close()
        self.items.append(item)
        self.__addLinkByItem(item)

    def getItems(self):
        return self.items

    def getLinks(self):
        return self.links

    def fillWithLinks(self):
        for item in self.items:
            file = open(item.getPath(), 'r')
            text = file.read()
            file.close()
            for name in revertOrder(self.links.keys()):
                if name in text and name != item.getElement().getName():
                    start = text.find(name)
                    while start < len(text) and start != -1:
                        end = start + len(name)
                        if not isInLink(text, start, end) and \
                                not isInTag(text, start, end) and \
                                isWhole(text, start, end):
                            path = self.links[name]
                            link = '<a href="' + path + '">' + name + '</a>'
                            text = text[:start] + link + text[end:]
                            start = text.find(name, start + len(link))
                        else:
                            start = text.find(name, end)

            file = open(item.path, 'w')
            file.write(text)
