thriftr
-------

Pure python apache thrift parser.

For Python 2.7+/3.3+/PyPy

```python
from thriftr import parse

data = open('sample.thrift').read()
parse(data)
```

[example](example)

NOTE: this parser will be merged into [eleme/thriftpy](https://github.com/eleme/thriftpy.git),

```python
from thriftpy import parse

data = open('sample.thrift').read()
parse(data)
```
