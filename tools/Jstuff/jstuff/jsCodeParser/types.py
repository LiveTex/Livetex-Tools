

class Type:
    """
        Type of JsDoc expression.
        
        @param {string} expression.
        
        @attribute {string} expression.
    """
    def __init__(self, expression):
        self.expression = expression

    def getExpression(self):
        return self.expression

    def getNames(self):
        names = list()
        if self.__class__.__name__ == 'TypeName':
            names.append(self)
        if 'getTypes' in dir(self):
            for element in self.getTypes():
                names = names + element.getName()
        return names


class TypeName(Type):
    """
        Name expression.
        Can be default as 'string', 'number', 'boolean', 'Object'.
        Or custom as the name of some element.
        
        @param {string} expression.
        
        @attribute {string} expression.
    """
    def __init__(self, expression):
        Type.__init__(self, expression)

    def isDefault(self):
        expression = self.getName()
        defaults = {'string', 'number', 'boolean', 'Object'}
        if not expression or expression in defaults:
            return True
        else:
            return False

    def getName(self):
        return self.expression.strip('!?.[ ]=')


class TypeApplication(Type):
    """
        Application expression.
        Such as:
            Object.<string>
        or
            Array.<string>
        
        @param {string} expression.
        
        @attribute {jsCodeParser.types.Type} types Types inside an application.
    """
    def __init__(self, expression):
        Type.__init__(self, expression)
        self.types = None

    def getTypes(self):
        return self.types

    def setTypes(self, types):
        self.types = types


class TypeUnion(Type):
    """
        Union expression, which parts are divided by '|'.
        
        @param {string} expression.
        
        @attribute {jsCodeParser.types.Type} types Types inside a union.
    """
    def __init__(self, expression):
        Type.__init__(self, expression)
        self.types = None

    def getTypes(self):
        return self.types

    def setTypes(self, types):
        self.types = types


class TypeRecord(Type):
    """
        Record expression, which describes objects.
        
        @param {string} expression.
        
        @attribute {{key: value}} dictionary.
    """
    def __init__(self, expression):
        Type.__init__(self, expression)
        self.dictionary = None

    def setDictionary(self, dictionary):
        self.dictionary = dictionary


class TypeFunction(Type):
    """
        Function expression.
        Can have parameters, parameters tagged with 'new' or 'this' words
        and result.
        
        @param {string} expression.
        
        @attribute {Array.<jsCodeParser.types.Type>} parameters.
        @attribute {Array.<jsCodeParser.types.Type>} newParameters.
        @attribute {Array.<jsCodeParser.types.Type>} thisParameters.
        @attribute {jsCodeParser.types.Type} result.
    """
    def __init__(self, expression):
        Type.__init__(self, expression)
        self.parameters = None
        self.newParameters = None
        self.thisParameters = None
        self.result = None

    def setParameters(self, parameters):
        self.parameters = parameters

    def setNewParameters(self, newParameters):
        self.newParameters = newParameters

    def setThisParameters(self, thisParameters):
        self.thisParameters = thisParameters

    def setResult(self, result):
        self.result = result
