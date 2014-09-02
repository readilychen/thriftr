# coding=utf8

"""
thriftr
~~~~~~~

The pure python parser for apache thrift.

Author: hit9 <wangchao@ele.me>
License: MIT.

    >>> from thriftr import parse
    >>> thrift = parse(open('sample.thrift').read())

Parsing results:

  thrift:

    {
      'includes': [],
      'namespaces': [],
      'consts', {'k', 'v'},
      ''
    }

"""

__version__ = '0.0.1'


class ThriftSyntaxError(Exception):
    pass


class ThriftUnkownType(ThriftSyntaxError):
    pass


from .parser import parse
