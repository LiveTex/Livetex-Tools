import json
from utils import *


class Config:
    """
        Configuration of project.

        @param {string} name Name of project.
        @param {string} configPath Path to project's config.

        @param {string} name Name of project.
        @param {{option: value}} config Configuration of a project..
    """
    def __init__(self, name, configPath):
        self.name = name
        file = open(configPath, 'r')
        self.config = self.__defineConfig(json.load(file))

    def __defineConfig(self, config):
        default = config['default']
        projectConfig = config[self.name]
        return mergeDictsItems(projectConfig, default)

    def getName(self):
        return self.name

    def getValueByPath(self, path):
        path = path.lower().split('.')
        value = self.config
        for key in path:
            value = value[key]
        return value

