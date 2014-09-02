# coding=utf8

from ._compat import *


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


class BaseType(str):
    pass


class BoolType(BaseType):

    cast = bool

    def __new__(self):
        return str.__new__(self, 'bool')


class ByteType(BaseType):

    cast = int

    def __new__(self):
        return str.__new__(self, 'byte')


class I16Type(BaseType):

    cast = int

    def __new__(self):
        return str.__new__(self, 'i16')


class I32Type(BaseType):

    cast = int

    def __new__(self):
        return str.__new__(self, 'i32')


class I64Type(BaseType):

    cast = int

    def __new__(self):
        return str.__new__(self, 'i64')


class DoubleType(BaseType):

    cast = float

    def __new__(self):
        return str.__new__(self, 'double')


class StringType(BaseType):

    cast = str

    def __new__(self):
        return str.__new__(self, 'string')


class BinaryType(BaseType):

    cast = bytes_

    def __new__(self):
        return str.__new__(self, 'binary')


class ContainerType(list):
    pass


class ListType(ContainerType):   # ['list', val_type]

    def cast(self, data):
        return map(self[1].cast, data)


class MapType(ContainerType):  # ['map', k_type, v_type]

    def cast(self, data):
        dct = {}
        keys = data.keys();

        for key in keys:
            dct[self[1].cast(key)] = self[2].cast(data[key])
        return dct


class SetType(ContainerType):  # ['set', v_type]
    pass


BASE_TYPE_MAPS = {
    'bool': BoolType,
    'byte': ByteType,
    'i16': I16Type,
    'i32': I32Type,
    'i64': I64Type,
    'double': DoubleType,
    'string': StringType,
    'binary': BinaryType
}
