from collector import Collector
from jsCodeParser.project import Project
from jsCodeParser.extractors.elementsExtractor import extractElements
from jsCodeParser.extractors.linksExtractor import link


collector = Collector()


def parse(pathsFile):
    """
        Parses code and creates elements structures.
    """
    project = Project(pathsFile)
    extractElements(project)
    collector.addProject(project)
    link()