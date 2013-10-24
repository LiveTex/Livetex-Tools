import os
import shutil
from collector import Collector
from docsGenerator.structure import Container
from docsGenerator.itemsManager import ItemsManager


collector = Collector()


def generateDocs():
    """
        Generates documentation.
    """
    itemsManager = ItemsManager()
    for project in collector.getProjects():
        element = project.getGlobal()
        path = project.getConfig().getValueByPath('docs.out')
        projectPath = path + os.sep + project.getName()
        if os.path.exists(projectPath):
            shutil.rmtree(projectPath)
        projectContainer = Container(project, element, path)
        for item in projectContainer.getItems():
            itemsManager.create(item)
    itemsManager.fillWithLinks()

