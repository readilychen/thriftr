# coding=utf8
# ref: https://thrift.apache.org/docs/idl

from ply import yacc
from . import ThriftSyntaxError
from .lexer import tokens

dct = {
    'include': [],
    'namespace': [],
    'const': {},
    'typedef': {},
}

def p_error(p):
    raise ThriftSyntaxError(p)


def p_start(p):
    '''start : header definition'''


def p_header(p):
    '''header : header_unit header
              |'''

def p_header_unit(p):
    '''header_unit : include
                   | namespace'''


def p_include(p):
    '''include : INCLUDE LITERAL'''


def p_namespace(p):
    '''namespace : NAMESPACE namespace_scope IDENTIFIER'''


def p_namespace_scope(p):
    '''namespace_scope : '*'
                       | 'cpp'
                       | 'java'
                       | 'py'
                       | 'perl'
                       | 'rb'
                       | 'cocoa'
                       | 'csharp'
                       | 'php'
    '''


def p_definition(p):
    '''definition : const
                  | typedef
                  | enum
                  | struct
                  | union
                  | exception
                  | service
    '''


def p_const(p):
    '''const : CONST field_type IDENTIFIER '=' const_value '''


def p_const_value(p):
    '''const_value : INTCONSTANT
                   | DUBCONSTANT
                   | LITERAL
                   | IDENTIFIER
                   | const_list
                   | const_map'''


def p_const_list(p):
    '''const_list : '[' const_value_sea ']' '''


def p_const_value_seq(p):
    '''const_value_seq : const_value_seq ',' const_value
                       | const_value_seq ','
                       | const_value
                       |'''


def p_const_map(p):
    '''const_map : '{' const_map_seq '}' '''


def p_const_map_items(p):
    '''const_map_seq : const_map_seq ',' const_map_item
                     | const_map_seq ','
                     | const_map_item
                     |'''


def p_const_map_item(p):
    '''const_map_item : '\'' const_value '\'' ':' '\'' const_value '\'' '''


def p_typedef(p):
    '''typedef : TYPEDEF definition_type IDENTIFIER'''


def p_enum(p):
    '''enum : ENUM IDENTIFIER '{' enum_seq '}' '''


def p_enum_seq(p):
    '''enum_seq : enum_seq ',' enum_item
                | enum_seq ','
                | enum_item
                |'''


def p_enum_item(p):
    '''enum_item : IDENTIFIER '=' INTCONSTANT'''


def p_struct(p):
    '''struct : STRUCT IDENTIFIER '{' field_seq '}' '''


def p_union(p):
    '''union : UNION IDENTIFIER '{' field_seq '}' '''


def p_exception(p):
    '''exception : EXCEPTION IDENTIFIER '{' field_seq '}' '''


def p_service(p):
    '''service : SERVICE IDENTIFIER '{' function_seq '}'
               | SERVICE IDENTIFIER EXTENDS IDENTIFIER '{' function_seq '}'
    '''


def p_function(p):
    '''function : ONEWAY function_type IDENTIFIER '(' field_seq ')' throws
                | function_type IDENTIFIER '(' field_seq ')' throws
                | function_type IDENTIFIER '(' field_seq ')'
    '''


def p_throws(p):
    '''throws : THROWS '(' field_seq ')' '''


def p_function_type(p):
    '''function_type : field_type | VOID '''


def p_field_seq(p):
    '''field_seq : field_seq ',' field
                 | field_seq ','
                 | field
                 |'''


def p_field(p):
    '''field : field_id field_req field_type IDENTIFIER'''


def p_field_id(p):
    '''field_id : INTCONSTANT ':' '''


def p_field_req(p):
    '''field_req : REQUIRED
                 | OPTIONAL'''


def p_field_type(p):
    '''field_type : IDENTIFIER
                  | base_type
                  | container_type'''


def p_base_type(p):
    '''base_type : BOOL
                 | BYTE
                 | I16
                 | I32
                 | I64
                 | DOUBLE
                 | STRING
                 | BINARY'''


def p_container_type(p):
    '''container_type : map_type
                      | list_type
                      | set_type'''


def p_map_type(p):
    '''map_type : MAP '<' field_type ',' field_type '>' '''


def p_list_type(p):
    '''list_type : LIST '<' field_type '>' '''


def p_set_type(p):
    '''set_type : SET '<' field_type '>' '''


def p_definition_type(p):
    '''definition_type : base_type
                       | container_type'''


parser = yacc.yacc(debug=0, write_tables=0)
