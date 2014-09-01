# coding=utf8
# ref: https://thrift.apache.org/docs/idl

from ply import yacc
from . import ThriftSyntaxError, ThriftUnkownType
from .lexer import tokens


dct = {
    'includes': [],
    'namespaces': [],
    'consts': {},
    'typedefs': [],
}


def parse(data):
    for key in dct:
        dct[key] = []
    parser.parse(data)
    return dct


converters = {
    'bool': bool,
    'byte': int,
    'i16': int,
    'i32': int,
    'i64': int,
    'double': float,
    'string': str,
    'binary': str,
}


# cast thrift values to python values
def cast(val, tp):
    if isinstance(tp, str) and tp in converters:
        return converters[tp](val)
    elif isinstance(tp, list):
        if tp[0] == 'list':
            t = tp[1]
            return map(lambda v: cast(v, t), val)
        elif tp[0] == 'map':
            kt = tp[1]
            vt = tp[2]
            d = {}
            for k, v in d.items():
                d[cast(k, kt)] = cast(v, vt)
            return d
    raise ThriftUnkownType(tp)


def p_error(p):
    raise ThriftSyntaxError(p)


def p_start(p):
    '''start : unit start
             | '''
    pass


def p_unit(p):
    '''unit : include
            | const'''


def p_include(p):
    '''include : INCLUDE LITERAL'''
    dct['includes'].append(p[2])


def p_field_type(p):
    '''field_type : base_type
                  | container_type
                  | IDENTIFIER'''
    p[0] = p[1]


def p_base_type(p):
    '''base_type : VOID
                 | BOOL
                 | BYTE
                 | I16
                 | I32
                 | I64
                 | DOUBLE
                 | STRING
                 | BINARY'''
    p[0] = p[1]


def p_container_type(p):
    '''container_type : map_type
                      | list_type
                      | set_type'''
    p[0] = p[1]


def p_map_type(p):
    '''map_type : MAP '<' field_type ',' field_type '>' '''
    p[0] = ['map', p[3], p[5]]


def p_list_type(p):
    '''list_type : LIST '<' field_type '>' '''
    p[0] = ['list', p[3]]


def p_set_type(p):
    '''set_type : SET '<' field_type '>' '''
    p[0] = ['set', p[3]]


def p_const(p):
    '''const : CONST field_type IDENTIFIER '=' const_value'''
    tp = p[2]
    key = p[3]
    val = p[5]
    dct['consts'].append([key, cast(val, tp)])


def p_const_value(p):
    '''const_value : BOOLCONSTANT
                   | INTCONSTANT
                   | DUBCONSTANT
                   | LITERAL
                   | const_list'''
    p[0] = p[1]


def p_const_list(p):
    '''const_list : '[' const_sequence ']' '''
    p[0] = p[2]

def p_const_sequence(p):
    '''const_sequence : const_sequence ',' const_value
                      | const_sequence  ','
                      | const_value
                      |'''
    length = len(p)

    if length == 1:
        p[0] = []
    elif len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 3:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[1] + [p[3]]

def p_typedef(p):
    '''typedef : TYPEDEF definition_type IDENTIFIER'''


def p_definition_type(p):
    '''definition_type : base_type
                       | container_type'''


parser = yacc.yacc(debug=1, write_tables=0)
