import re
from utils import *
from jsCodeParser.types import *


def __getStartPosition(pos, context):
    """
        Gets the start position of type expression.
        Context can content '!', '?'. '...' or '[' markers before expression.

        @param {number} pos Start position of expression.
        @param {string} context Context in which contains the expression.

        @return {number} Start position.
    """
    tokens = {'!', '?', '.', '['}
    while pos > -1 and context[pos - 1] in tokens:
        pos -= 1
    return pos


def __getEndPosition(pos, context):
    """
        Gets the end position of type expression.
        Context can content '=' or '[' markers before expression.

        @param {number} pos End position of expression.
        @param {string} context Context in which contains the expression.

        @return {number} End position.
    """
    tokens = {'=', ']'}
    while pos < len(context) and context[pos] in tokens:
        pos += 1
    return pos + 1


def __getFullExpression(expression, context):
    """
        Gets full expression with all markers from context.

        @param {string} expression.
        @param {string} context.

        @return {string} Full expression.
    """
    exprStart = context.find(expression)
    exprEnd = exprStart + len(expression)
    start = __getStartPosition(exprStart, context)
    end = __getEndPosition(exprEnd, context)
    return context[start:end]


def __extractParts(expression):
    """
        Extracts type from expression and returns its parts.

        @param {string} expression.

        @return {Array.<jsCodeParser.types.Type>} Types.
    """
    element = extractType(expression)
    if isinstance(element, TypeUnion):
        types = element.getTypes()
    else:
        types = [element]
    return types


def __extractType(expression):
    """
        Chooses extractor for type and get it.

        @param {string} expression.

        @return {jsCodeParser.types.Type} Type.
    """
    context = expression
    expression = expression.strip('?!=.[')
    if re.match('(\.\.\.(\[)?)?(\!|\?)?(Array|Object)\.\<', expression):
        extractor = __extractApplication
    elif expression.find('function(') == 0:
        extractor = __extractFunction
    elif expression.find('{') == 0:
        extractor = __extractRecord
    elif expression.find('(') == 0:
        extractor = __extractUnion
    else:
        extractor = __extractName
    return extractor(expression, context)


def __extractName(expression, context):
    """
        Extracts name expression.

        @param {string} expression.
        @param {string} context.

        @return {jsCodeParser.types.TypeName} Name.
    """
    end = getFirst(expression, ['|', ' '])
    if end == -1:
        end = len(expression)
    expression = expression[:end].strip(',')
    expression = __getFullExpression(expression, context).strip('| ')
    if not expression:
        expression = context
    name = TypeName(expression)
    return name


def __extractApplication(expression, context):
    """
        Extracts application expression and sets types to its structure.

        @param {string} expression.
        @param {string} context.

        @return {jsCodeParser.types.TypeApplication} Application.
    """
    appElements = extractTextBetweenTokens(expression, '<')
    end = expression.find(appElements) + len(appElements)
    expression = __getFullExpression(expression[:end], context)
    element = TypeApplication(expression)
    types = __extractParts(appElements[1:-1])
    element.setTypes(types)
    return element


def __extractUnion(expression, context):
    """
       Extracts union expression and sets types to its structure.

       @param {string} expression.
       @param {string} context.

       @return {jsCodeParser.types.TypeUnion} Union.
    """
    expression = extractTextBetweenTokens(expression, '(')
    types = __extractParts(expression[1:-1])
    expression = __getFullExpression(expression, context)
    element = TypeUnion(expression)
    element.setTypes(types)
    return element


def __extractFunction(expression, context):
    """
        Extracts function expression and sets parameters and result to its
        structure.

        @param {string} expression.
        @param {string} context.

        @return {jsCodeParser.types.TypeFunction} Function.
    """
    parameters = extractTextBetweenTokens(expression, '(')
    end = expression.find(parameters) + len(parameters)
    result = None
    if end < len(expression) and expression[end] == ':':
        valueExpression = expression[end + 1:].strip()
        result = __extractType(valueExpression)
        valueExpression = result.getExpression()
        end = expression.find(valueExpression, end) + len(valueExpression)
    parameters = parameters[1:-1]
    newParameters = None
    thisParameters = None
    if parameters:
        parameters = __extractParts(parameters)
        newParameters = [parameter for parameter in parameters
                         if 'new:' in parameter.getExpression()]
        thisParameters = [parameter for parameter in parameters
                          if 'this:' in parameter.getExpression()]
    else:
        parameters = None
    expression = __getFullExpression(expression[:end], context)
    element = TypeFunction(expression)
    element.setParameters(parameters)
    element.setNewParameters(newParameters)
    element.setThisParameters(thisParameters)
    element.setResult(result)
    return element


def __extractRecord(expression, context):
    """
        Extracts record expression and sets its dictionary representation to
        structure.

        @param {string} expression.
        @param {string} context.

        @return {jsCodeParser.types.TypeRecord} Record.
    """
    expression = extractTextBetweenTokens(expression, '{')
    expression = __getFullExpression(expression, context)
    expression = clearTokens(expression)
    element = TypeRecord(expression)
    dictionary = convertStringToDict(expression, ':', ',')
    for key in dictionary.keys():
        dictionary[key] = extractType(dictionary[key])
    element.setDictionary(dictionary)
    return element


def extractType(expression):
    """
        Extracts the type of given expression.
        Parses expression and returns type or union
        if it contains more than one type.

        @param {string} expression.

        @return {jsCodeParser.types.Type} Type.
    """
    types = []
    exprCopy = expression
    while expression:
        element = __extractType(expression)
        elementExpr = element.getExpression()
        position = expression.find(elementExpr) + len(elementExpr)
        while position < len(expression) and expression[position] == '|':
            position += 1
        if position == 0:
            break
        expression = expression[position:]
        types.append(element)
    if len(types) > 1:
        typeExpression = TypeUnion(exprCopy)
        typeExpression.setTypes(types)
    else:
        typeExpression = types[0]
    return typeExpression