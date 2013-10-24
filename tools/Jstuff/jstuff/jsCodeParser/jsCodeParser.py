from collector import Collector
from jsCodeParser.config import Config
from jsCodeParser.project import Project
from jsCodeParser.extractors.elementsExtractor import extractElements
from jsCodeParser.extractors.linksExtractor import link


collector = Collector()


def parse(projectNames, configPath):
    """
        Parses code and creates elements structures.
    """
    for name in projectNames:
        projectConfig = Config(name, configPath)
        project = Project(projectConfig)
        extractElements(project)
        collector.addProject(project)
    link()