

class Collector:
    """
        Singleton class for collecting projects with their elements.

        @attribute {{name: project}} _collection The collection of projects.
    """

    _collection = {}

    def __init__(self):
        self.__dict__ = self._collection

    def addProject(self, project):
        if project.getElements():
            name = project.getName()
            self._collection.__setitem__(name, project)

    def getProject(self, projectName):
        return self._collection[projectName]

    def getProjects(self):
        return self._collection.values()

    def getElement(self, name, project=None, group=None):
        for element in self.getElements(project, group):
            if element.getName() == name:
                return element
        return None

    def getElements(self, projectName=None, group=None):
        elements = list()
        if projectName:
            projects = [self.getProject(projectName)]
        else:
            projects = self.getProjects()
        for project in projects:
            for element in project.getElements(group):
                elements.append(element)
        return elements

    def selectElements(self, filterFunction, elements,
                       parameters=None):
        filtered = [element for element in elements
                    if filterFunction(element, parameters)]
        return filtered

