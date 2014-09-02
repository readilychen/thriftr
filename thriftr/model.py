# coding=utf8


class Thrift(dict):

    def __init__(self,
                 includes=None,
                 namespaces=None,
                 consts=None,
                 enums=None,
                 typedefs=None,
                 structs=None,
                 unions=None,
                 exceptions=None,
                 services=None):

        if includes is None:
            includes = []
        if namespaces is None:
            namespaces = {}    # {identifier: scope}
        if consts is None:
            consts = {}
        if enums is None:
            enums = []
        if typedefs is None:
            typedefs = []
        if structs is None:
            structs = []
        if unions is None:
            unions = []
        if exceptions is None:
            exceptions = []
        if services is None:
            services = []

        self.includes = self['includes'] = includes
        self.namespaces = self['namespaces'] = namespaces
        self.consts = self['consts'] = consts
        self.enums = self['enums'] = enums
        self.typedefs = self['typedefs'] = typedefs
        self.structs = self['structs'] = structs
        self.unions = self['unions'] = unions
        self.exceptions = self['exceptions'] = exceptions
        self.services = self['services'] = services
