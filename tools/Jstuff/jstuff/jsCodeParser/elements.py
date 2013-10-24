from utils import *
from xml.sax.saxutils import escape


class Element:
    """
        Some element of the code, which has JsDoc.
    
        @param {string} code Code of an element.
        @param {jsCodeParser.jsDoc.JsDoc} jsDoc JsDoc object of an element.
    
        @attribute {string} code Code of an element.
        @attribute {jsCodeParser.jsDoc.JsDoc} jsDoc JsDoc object of an element.
        @attribute {string} name Name of an element.
    """
    def __init__(self, code, jsDoc, path):
        self.code = code
        self.jsDoc = jsDoc
        self.name = self._defineName()
        self.path = path
        self.description = self.jsDoc.getDescription()

    def _defineName(self):
        name = self.code
        eqPos = name.find('=')
        if eqPos != -1:
            name = name[:eqPos]
        name = name.strip('; ')
        if 'var ' in name:
            name = name.replace('var ', '')
        return name

    def getShortName(self):
        name = self.name
        if 'prototype' in name:
            name = name.split('prototype')[-1]
        elif '.' in name:
            name = name.split('.')[-1]
        name = name.strip('.')
        return name

    def getParentName(self):
        shortName = self.getShortName()
        shortNamePosition = self.name.rfind(shortName)
        name = self.name[:shortNamePosition]
        end = name.find('.prototype')
        if end + 1:
            name = name[:end]
        name = name.strip('.')
        return name

    def getDescription(self):
        return self.description

    def getCode(self):
        return self.code

    def getJsDoc(self):
        return self.jsDoc

    def getName(self):
        return self.name

    def getPath(self):
        return self.path

    def isPublic(self):
        if not (self.isProtected() or self.isPrivate()):
            return True
        else:
            return False

    def isProtected(self):
        name = self.getShortName()
        if name[0] == '_' and name[1] != '_':
            return True
        else:
            return False

    def isPrivate(self):
        name = self.getShortName()
        if name[:2] == '__':
            return True
        else:
            return False

    def getStructure(self):
        return {
            'name': self.name,
            'description': self.description
        }


class Namespace(Element):
    """
        Element, which has JsDoc with '@namespace' tag.
    
        @param {string} code Code of an element.
        @param {jsCodeParser.jsDoc.JsDoc} jsDoc JsDoc object of an element.
    
        @attribute {Array.<jsCodeParser.elements.Namespace>} children
        @attribute {Array.<jsCodeParser.elements.Class>} classes
        @attribute {Array.<jsCodeParser.elements.Interface>} interfaces
        @attribute {Array.<jsCodeParser.elements.Method>} methods
        @attribute {Array.<jsCodeParser.elements.Property>} properties
        @attribute {Array.<jsCodeParser.elements.Typedef>} typedefs
        @attribute {Array.<jsCodeParser.elements.Enumeration>} enums
    """
    def __init__(self, code, jsDoc, path):
        Element.__init__(self, code, jsDoc, path)
        self.children = list()
        self.classes = list()
        self.interfaces = list()
        self.methods = list()
        self.properties = list()
        self.typedefs = list()
        self.enums = list()

    def getChildren(self):
        return self.children

    def getClasses(self):
        return self.classes

    def getInterfaces(self):
        return self.interfaces

    def getMethods(self):
        return self.methods

    def getProperties(self):
        return self.properties

    def getTypedefs(self):
        return self.typedefs

    def getEnums(self):
        return self.enums

    def setChildren(self, children):
        self.children = children

    def setClasses(self, classes):
        self.classes = classes

    def setInterfaces(self, interfaces):
        self.interfaces = interfaces

    def setMethods(self, methods):
        self.methods = methods

    def setProperties(self, properties):
        self.properties = properties

    def setTypedefs(self, typedefs):
        self.typedefs = typedefs

    def setEnums(self, enums):
        self.enums = enums

    def getStructure(self):
        return {
            'name': self.name,
            'description': self.description,
            'methods': [element.getStructure() for element in self.methods
                        if not element.isPrivate()],
            'properties': [element.getStructure()
                           for element in self.properties
                           if not element.isPrivate()],
            'typedefs': [element.getStructure() for element in self.typedefs
                         if not element.isPrivate()],
            'enums': [element.getStructure() for element in self.enums
                      if not element.isPrivate()]
        }


class GlobalNamespace(Namespace):
    """
        Global namespace of the project.

        @param {string} code Empty code.
        @param {jsCodeParser.jsDoc.JsDoc} jsDoc Empty JsDoc.

        @attribute {string} name Name of a project.
        @attribute {string} description Description of a project.
    """
    def __init__(self, code, jsDoc, projectName, projectDescription):
        Namespace.__init__(self, code, jsDoc, '')
        self.name = projectName
        self.description = projectDescription

    def getStructure(self):
        structure = {
            'name': self.name,
            'description': self.description,
        }
        keysMap = {
            'namespaces': self.children,
            'classes': self.classes,
            'interfaces': self.interfaces,
            'methods': self.methods,
            'properties': self.properties,
            'typedefs': self.typedefs,
            'enums': self.enums
        }
        for key in keysMap.keys():
            elements = keysMap[key]
            if elements:
                structure[key] = [element.getStructure()
                                  for element in elements]
        return structure


class Constructor(Element):
    """
        Constructor of a class or method.

        @param {string} code Code of an element.
        @param {jsCodeParser.jsDoc.JsDoc} jsDoc JsDoc of an element.

        @attribute {Array.<{'name': string,
                            'type': jsCodeParser.types.Type,
                            'description': string }>} parameters.
        @attribute {Array.<jsCodeParser.elements.Element>} attributes
    """
    def __init__(self, code, jsDoc, path):
        Element.__init__(self, code, jsDoc, path)
        self.parameters = self.__defineParameters()
        self.attributes = list()

    def _defineName(self):
        code = self.code
        end = code.find('(')
        start = code[:end].rfind(' ')
        name = code[start: end].strip()
        if name == 'function':
            end = code.find('=')
            name = code[:end].strip()
        if 'var ' in name:
            name.replace('var ', '')
        return name

    def __defineParameters(self):
        records = self.jsDoc.getRecords(tag='@param')
        if records:
            return [{
                'name': record.getName(),
                'type': record.getType(),
                'description': record.getDescription()
            } for record in records]
        return None

    def getParameters(self):
        return self.parameters

    def getAttributes(self):
        return self.attributes

    def getRealization(self):
        return extractTextBetweenTokens(self.code, '{')

    def getSignature(self):
        name = self.name
        parameters = extractTextBetweenTokens(self.code, '(')
        parameters = clearTokens(parameters.replace('\n', ''))
        return name + parameters

    def setParameters(self, parameters):
        self.parameters = parameters

    def setAttributes(self, attributes):
        self.attributes = attributes


class Class(Constructor):
    """
       Element, which has JsDoc with '@constructor' tag.

       @param {string} code Code of an element.
       @param {jsCodeParser.jsDoc.JsDoc} jsDoc JsDoc of an element.

       @attribute {Array.<jsCodeParser.elements.Class>} parents.
       @attribute {Array.<jsCodeParser.elements.Method>} methods.
       @attribute {Array.<jsCodeParser.elements.Interface>} interfaces.
    """
    def __init__(self, code, jsDoc, path):
        Constructor.__init__(self, code, jsDoc, path)
        self.parents = list()
        self.methods = list()
        self.interfaces = list()

    def getParents(self):
        return self.parents

    def getMethods(self):
        return self.methods

    def getInterfaces(self):
        return self.interfaces

    def setParents(self, parents):
        self.parents = parents

    def setMethods(self, methods):
        self.methods = methods

    def setInterfaces(self, interfaces):
        self.interfaces = interfaces

    def getStructure(self):
        parameters = self.parameters
        if parameters:
            parameters = [{
                'name': parameter['name'],
                'type': escape(parameter['type'].getExpression()),
                'description': parameter['description']
            } for parameter in self.parameters]
        return {
            'name': self.name,
            'description': self.description,
            'signature': self.getSignature(),
            'attributes': [element.getStructure()
                           for element in self.getAttributes()
                           if not element.isPrivate()],
            'parameters': parameters,
            'parents': [element.getStructure() for element in self.parents
                        if not element.isPrivate()],
            'methods': [element.getStructure() for element in self.methods
                        if not element.isPrivate()],
            'interfaces': [element.getStructure()
                           for element in self.interfaces
                           if not element.isPrivate()],
        }


class Method(Constructor):
    """
       Element, which represented as function in code.

       @param {string} code Code of an element.
       @param {jsCodeParser.jsDoc.JsDoc} jsDoc JsDoc of an element.

       @attribute {Array.<jsCodeParser.elements.Method>} implementation
            Method which this element implements.
    """
    def __init__(self, code, jsDoc, path):
        Constructor.__init__(self, code, jsDoc, path)
        self.result = self.__defineResult()
        self.abstraction = None

    def __defineResult(self):
        records = self.jsDoc.getRecords(tag='@return')
        if records:
            return [{
                        'type': record.getType(),
                        'description': record.getDescription()
                    } for record in records][0]
        return None

    def _defineName(self):
        code = self.code
        end = code.find('(')
        start = code[:end].rfind(' ')
        name = code[start: end].strip()
        if name == 'function':
            end = code.find('=')
            name = code[:end].strip()
        if 'var ' in name:
            name = name.replace('var ', '')
        return name

    def getResult(self):
        return self.result

    def getAbstract(self):
        return self.abstraction

    def setAbstract(self, abstraction):
        self.parameters = abstraction.getParameters()
        self.result = abstraction.getResult()
        self.description = abstraction.getDescription()
        self.abstraction = abstraction

    def getStructure(self):
        parameters = self.parameters
        if self.parameters:
            parameters = [{
                'name': parameter['name'],
                'type': escape(parameter['type'].getExpression()),
                'description': parameter['description']
            } for parameter in self.parameters]
        result = None
        if self.result:
            result = dict(self.result)
            result['type'] = escape(result['type'].getExpression())

        return {
            'name': self.name,
            'description': self.description,
            'signature': self.getSignature(),
            'attributes': [element.getStructure()
                           for element in self.getAttributes()
                           if not element.isPrivate()],
            'parameters': parameters,
            'result': result
        }


class Interface(Element):
    """
       Element, which has JsDoc with '@interface' tag.

       @param {string} code Code of an element.
       @param {jsCodeParser.jsDoc.JsDoc} jsDoc JsDoc of an element.

       @attribute {Array.<{'name': string,
                            'type': jsCodeParser.types.Type,
                            'description': string }>} parameters.
       @attribute {Array.<jsCodeParser.elements.Interface>} parents.
       @attribute {Array.<jsCodeParser.elements.Method>} methods.
       @attribute {Array.<jsCodeParser.elements.Class>} users.
    """
    def __init__(self, code, jsDoc, path):
        Element.__init__(self, code, jsDoc, path)
        self.parameters = self.__defineParameters()
        self.parents = list()
        self.methods = list()
        self.users = list()

    def _defineName(self):
        code = self.code
        end = code.find('(')
        start = code[:end].rfind(' ')
        name = code[start: end].strip()
        if name == 'function':
            end = code.find('=')
            name = code[:end].strip()
        if 'var ' in name:
            name.replace('var ', '')
        return name

    def __defineParameters(self):
        records = self.jsDoc.getRecords(tag='@param')
        if records:
            return [{
                'name': record.getName(),
                'type': record.getType(),
                'description': record.getDescription()
            } for record in records]
        else:
            return None

    def getParents(self):
        return self.parents

    def getMethods(self):
        return self.methods

    def getUsers(self):
        return self.users

    def getSignature(self):
        name = self.name
        parameters = extractTextBetweenTokens(self.code, '(')
        return name + parameters

    def setParents(self, parents):
        self.parents = parents

    def setMethods(self, methods):
        self.methods = methods

    def setUsers(self, users):
        self.users = users

    def getStructure(self):
        parameters = self.parameters
        if parameters:
            parameters = [{
                'name': parameter['name'],
                'type': escape(parameter['type'].getExpression()),
                'description': parameter['description']
            } for parameter in self.parameters]
        return {
            'name': self.name,
            'description': self.description,
            'signature': self.getSignature(),
            'parameters': parameters,
            'parents': [element.getStructure() for element in self.parents
                        if not element.isPrivate()],
            'methods': [element.getStructure() for element in self.methods
                        if not element.isPrivate()],
            'users': [element.getName()
                      for element in self.users
                      if not element.isPrivate()],
        }


class Property(Element):
    """
       Element, which has JsDoc with '@type' tag.

       @param {string} code Code of an element.
       @param {jsCodeParser.jsDoc.JsDoc} jsDoc JsDoc of an element.

       @attribute {string} value.
       @attribute {jsCodeParser.types.Type} type.
    """
    def __init__(self, code, jsDoc, path):
        Element.__init__(self, code, jsDoc, path)
        self.value = self.__defineValue()
        self.type = self.__defineType()

    def __defineValue(self):
        eqPos = self.code.find('=')
        return self.code[eqPos + 1:].strip(';\n ')

    def __defineType(self):
        return self.jsDoc.getRecords(tag='@type')[0].getType()

    def getStructure(self):
        return {
            'name': self.name,
            'description': self.description,
            'value': self.value,
            'type': escape(self.type.getExpression())
        }


class Typedef(Element):
    """
       Element, which has JsDoc with '@typedef' tag.

       @param {string} code Code of an element.
       @param {jsCodeParser.jsDoc.JsDoc} jsDoc JsDoc of an element.

       @attribute {jsCodeParser.types.Type} type.
    """
    def __init__(self, code, jsDoc, path):
        Element.__init__(self, code, jsDoc, path)
        self.type = self.jsDoc.getRecords(tag='@typedef')[0].getType()

    def getStructure(self):
        return {
            'name': self.name,
            'description': self.description,
            'type': escape(self.type.getExpression())
        }


class Enumeration(Element):
    """
       Element, which has JsDoc with '@enum' tag.

       @param {string} code Code of an element.
       @param {jsCodeParser.jsDoc.JsDoc} jsDoc JsDoc of an element.

       @attribute {{key: value}} enum.
       @attribute {jsCodeParser.types.Type} type.
    """
    def __init__(self, code, jsDoc, path):
        Element.__init__(self, code, jsDoc, path)
        self.enum = self.__defineEnum()
        self.type = self.jsDoc.getRecords(tag='@enum')[0].getType()

    def __defineEnum(self):
        string = extractTextBetweenTokens(self.code, '{')
        return convertStringToDict(string, ':', ',')

    def getKeys(self):
        return [key for key in self.enum.keys().__iter__()]

    def getValues(self):
        return [value for value in self.enum.values().__iter__()]

    def getStructure(self):
        return {
            'name': self.name,
            'description': self.description,
            'type': escape(self.type.getExpression()),
            'keys': self.getKeys(),
            'values': self.getValues(),
            'number': len(self.getKeys())
        }