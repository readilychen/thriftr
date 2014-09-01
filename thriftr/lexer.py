# coding=utf8

import sys
from ply import lex

from . import ThriftSyntaxError


literals = ':;,=*{}()<>[]'

tokens = (
    # literal constants
    'BOOLCONSTANT',
    'INTCONSTANT',
    'DUBCONSTANT',
    'LITERAL',
    # identifier
    'IDENTIFIER',
    'ST_IDENTIFIER',
    # keywords
    'NAMESPACE',
    'INCLUDE',
    'VOID',
    'BOOL',
    'BYTE',
    'I16',
    'I32',
    'I64',
    'DOUBLE',
    'STRING',
    'BINARY',
    'MAP',
    'LIST',
    'SET',
    'ONEWAY',
    'TYPEDEF',
    'STRUCT',
    'UNION',
    'EXCEPTION',
    'EXTENDS',
    'THROWS',
    'SERVICE',
    'ENUM',
    'CONST',
    'REQUIRED',
    'OPTIONAL',
    'REFERENCE',
)

t_ignore = ' \t\r'   # whitespace

# comments
t_ignore_SILLYCOMM = r'\/\*\**\*\/'
t_ignore_MULTICOMM = r'\/\*[^*]\/*([^*/]|[^*]\/|\*[^/])*\**\*\/'
t_ignore_COMMENT = r'\/\/[^\n]*'
t_ignore_DOCTEXT = r'\/\*\*([^*/]|[^*]\/|\*[^/])*\**\*\/'
t_ignore_UNIXCOMMENT = r'\#[^\n]*'

# keywords
current_module = sys.modules[__name__]


def t_error(t):
    raise ThriftSyntaxError('Illegal characher %r at line %d' %
                            (t.value[0], t.lineno))


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_BOOLCONSTANT(t):
    r'true|false'
    t.value = t.value == 'true'
    return t


def t_DUBCONSTANT(t):
    r'-?\d+\.\d*(e-?\d+)?'
    t.value = float(t.value)
    return t


def t_HEXCONSTANT(t):
    r'0x[0-9A-Fa-f]+'
    t.value = int(t.value, 16)
    t.type = 'INTCONSTANT'
    return t


def t_INTCONSTANT(t):
    r'[+-]?[0-9]+'
    t.value = int(t.value)
    return t


def t_LITERAL(t):
    r'(\"([^\\\n]|(\\.))*?\")|\'([^\\\n]|(\\.))*?\''
    s = t.value[1:-1]
    maps = {
        't': '\t',
        'r': '\r',
        'n': '\n',
        '\\': '\\',
        '\'': '\'',
        '"': '\"'
    }
    i = 0
    length = len(s)
    val = ''
    while i < length:
        if s[i] == '\\':
            i += 1
            if s[i] in maps:
                val += maps[s[i]]
            else:
                msg = 'Unexcepted escaping characher: %s' % s[i]
                raise ThriftSyntaxError(msg)
        else:
            val += s[i]

        i += 1

    t.value = val
    return t


def t_NAMESPACE(t):
    r'namespace'
    return t


def t_INCLUDE(t):
    r'include'
    return t


def t_VOID(t):
    r'void'
    return t


def t_BOOL(t):
    r'bool'
    return t


def t_BYTE(t):
    r'byte'
    return t


def t_I16(t):
    r'i16'
    return t


def t_I32(t):
    r'i32'
    return t


def t_I64(t):
    r'i64'
    return t


def t_DOUBLE(t):
    r'double'
    return t


def t_STRING(t):
    r'string'
    return t


def t_BINARY(t):
    r'binary'
    return t


def t_MAP(t):
    r'map'
    return t


def t_LIST(t):
    r'list'
    return t


def t_SET(t):
    r'set'
    return t


def t_ONEWAY(t):
    r'oneway'
    return t


def t_TYPEDEF(t):
    r'typedef'
    return t


def t_STRUCT(t):
    r'struct'
    return t


def t_UNION(t):
    r'union'
    return t


def t_EXCEPTION(t):
    r'exception'
    return t


def t_EXTENDS(t):
    r'extends'
    return t


def t_THROWS(t):
    r'throws'
    return t


def t_SERVICE(t):
    r'service'
    return t


def t_ENUM(t):
    r'enum'
    return t


def t_CONST(t):
    r'const'
    return t


def t_REQUIRED(t):
    r'required'
    return t


def t_OPTIONAL(t):
    r'optional'
    return t


def t_REFERENCE(t):
    r'&'
    return t


def t_IDENTIFIER(t):
    r'[a-zA-Z_](\.[a-zA-Z_0-9]|[a-zA-Z_0-9])*'
    return t


def t_ST_IDENTIFIER(t):
    r'[a-zA-Z-](\.[a-zA-Z_0-9-]|[a-zA-Z_0-9-])*'
    return t


lexer = lex.lex()
