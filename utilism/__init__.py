
__version__ = (0, 2)

full_version = '.'.join(map(str, __version__[0:3])) + ''.join(__version__[3:])
release = full_version
short_version = '.'.join(str(x) for x in __version__[0:3])

__all__ = []

# DictObject
from . import dictobject
from dictobject import *
__all__.extend(dictobject.__all__)

# xml2json
from . import xml2json
__all__.append(xml2json)

# resolve
from . import resolve
__all__.append(resolve)
