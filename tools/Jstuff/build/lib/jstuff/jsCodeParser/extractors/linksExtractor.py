from collector import Collector


collector = Collector()


def __filterAbsolute(element, parameters):
    """
        Filter for 'absolute' elements.

        @param {jsCodeParser.elements.Element} element.
        @param {Array.<string>} parameters Parameters for this filter -
            [projectName]

        @return {boolean} True if an element don't have parents.
                          False if an element has parents.
    """
    project = parameters[0]
    if 'getParents' in dir(element):
        if not element.getParents() and not element.getParentName():
            return True
    if 'getChildren' in dir(element):
        group = element.__class__.__name__
        isAbsolute = True
        for kinElement in collector.getElements(project, group=group):
            if element in kinElement.getChildren():
                isAbsolute = False
                break
        if isAbsolute:
            return True
    return False


def __filterGroup(element, parameters):
    """
        Filter element by group.

        @param {jsCodeParser.elements.Element} element.
        @param {Array.<*>} parameters Parameters for this filter - [group]

        @return {boolean} True if an element belongs to group.
                          False if not.
    """
    group = parameters[0]
    if element.__class__.__name__ == group:
        return True
    return False


def __filterInheritDocs(element, parameters):
    """
        Filter elements which have 'inheritDoc' in JsDoc.

        @param {jsCodeParser.elements.Element} element.
        @param {Array.<*>} parameters Parameters for this filter - None.

        @return {boolean} True if element has 'inheritDoc' in JsDoc.
                          False if not.
    """
    if element.getJsDoc().isInheritDoc():
        return True
    return False


def __getLinksByTag(element, tag):
    """
        Picks up records which have a certain tag and returns elements
        which are mentioned in type.

        @param {jsCodeParser.elements.Element} element.
        @param {string} type.

        @return {Array.<jsCodeParser.elements.Element>} Links.
    """
    links = list()
    records = element.getJsDoc().getRecords(tag=tag)
    linksNames = [record.getType().getName() for record in records]
    group = element.__class__.__name__
    if tag == '@implements':
        group = 'Interface'
    for linkElement in [collector.getElement(linkName, group=group)
                        for linkName in linksNames]:
        if linkElement:
            links.append(linkElement)
    return links


def __getLinksByName(element, group):
    """
        Picks up elements of certain group and returns elements
        which parent names are equals to the name of given element.

        @param {jsCodeParser.elements.Element} element.
        @param {string} group.

        @return {Array.<jsCodeParser.elements.Element>} Links.
    """
    links = list()
    for linkElement in collector.getElements(group=group):
        if element.getName() == linkElement.getParentName():
            links.append(linkElement)
    return links


def __getUsers(element):
    """
        Returns users of interface.

        @param {jsCodeParser.elements.Element} element.

        @return {Array.<jsCodeParser.elements.Element>} Users.
    """
    users = list()
    for user in collector.getElements(group='Class'):
        if element in __getLinksByTag(user, '@implements'):
            users.append(user)
    return users


def __getInheritanceChain(element):
    """
        Returns the list of elements from which the given element inherits.

        @param {jsCodeParser.elements.Element} element.

        @return {Array.<jsCodeParser.elements.Element>} Chain.
    """
    chain = list()
    parents = [collector.getElement(record.getType().getExpression())
               for record in element.getJsDoc().getRecords('@extends')] + \
              [collector.getElement(record.getType().getExpression())
               for record in element.getJsDoc().getRecords('@implements')]
    for parent in parents:
        if parent:
            chain.append(parent)
            parentChain = __getInheritanceChain(parent)
            if parentChain:
                chain = chain + parentChain
    return chain


def __findAbstract(method, owner):
    """
        Finds an abstract method, which a certain method implements.

        @param {jsCodeParser.elements.Method} method.
        @param {jsCodeParser.elements.Class} owner.

        @return {(jsCodeParser.elements.Method|None)} Implementation.
    """
    methodName = method.getShortName()
    chain = __getInheritanceChain(owner)
    for parent in chain:
        for parentMethod in parent.getMethods():
            if methodName == parentMethod.getShortName() \
                    and not parentMethod.getJsDoc().isInheritDoc():
                return parentMethod
    return None


def __linkClass(element):
    """
        Links class with its parents, methods and interfaces.

        @param {jsCodeParser.elements.Element} element.
    """
    parents = __getLinksByTag(element, '@extends')
    methods = __getLinksByName(element, 'Method')
    interfaces = __getLinksByTag(element, '@implements')
    element.setParents(parents)
    element.setMethods(methods)
    element.setInterfaces(interfaces)


def __linkInterface(element):
    """
        Links interface with its parents, methods and users.

        @param {jsCodeParser.elements.Element} element.
    """
    parents = __getLinksByTag(element, '@extends')
    methods = __getLinksByName(element, 'Method')
    users = __getUsers(element)
    element.setParents(parents)
    element.setMethods(methods)
    element.setUsers(users)


def __linkNamespace(element):
    """
        Links namespace with elements which belongs to it.

        @param {jsCodeParser.elements.Element} element.
    """
    settersMap = {
        'Namespace': element.setChildren,
        'Class': element.setClasses,
        'Interface': element.setInterfaces,
        'Method': element.setMethods,
        'Property': element.setProperties,
        'Typedef': element.setTypedefs,
        'Enumeration': element.setEnums
    }
    for key in settersMap.keys():
        elements = __getLinksByName(element, group=key)
        setter = settersMap[key]
        setter(elements)


def __linkMethods():
    """
        Check each method whether it has 'inheritDocs' in JsDocs or not,
        finds abstract method with documentation and links them.

        @param {jsCodeParser.elements.Element} element.
    """
    methods = collector.selectElements(
        __filterInheritDocs, collector.getElements(group='Method'))
    for method in methods:
        owner = collector.getElement(method.getParentName())
        abstraction = __findAbstract(method, owner)
        if abstraction:
            method.setAbstract(abstraction)


def __linkGlobalNamespaces():
    """
        Finds 'absolute' elements of project and
        fills its global namespace with them.
    """
    for project in collector.getProjects():
        projectName = project.getName()
        globalNamespace = project.getGlobal()
        absoluteElements = collector.selectElements(
            __filterAbsolute,
            elements=collector.getElements(projectName),
            parameters=[projectName])

        settersMap = {
            'Namespace': globalNamespace.setChildren,
            'Class': globalNamespace.setClasses,
            'Interface': globalNamespace.setInterfaces,
            'Method': globalNamespace.setMethods,
            'Property': globalNamespace.setProperties,
            'Typedef': globalNamespace.setTypedefs,
            'Enumeration': globalNamespace.setEnums
        }
        for key in settersMap.keys():
            elements = collector.selectElements(__filterGroup,
                                                elements=absoluteElements,
                                                parameters=[key])
            setter = settersMap[key]
            setter(elements)


def link():
    """
        Finds links of elements in collector.
    """
    for namespace in collector.getElements(group='Namespace'):
        __linkNamespace(namespace)
    for classItem in collector.getElements(group='Class'):
        __linkClass(classItem)
    for interface in collector.getElements(group='Interface'):
        __linkInterface(interface)
    __linkMethods()
    __linkGlobalNamespaces()


