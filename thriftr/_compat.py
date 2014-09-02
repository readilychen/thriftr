# coding=utf8

import sys

if sys.version_info[0] < 3:
    bytes_ = bytes
else:
    bytes_ = lambda x: bytes(x, 'utf8')
