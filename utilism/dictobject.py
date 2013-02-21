# -*- coding: utf-8 -*_

"""
A dictionary-like object to represent items as attributes, but still behaves
like a dict in every way.
"""

__author__ = 'Jathan McCollum'
__maintainer__ = 'Jathan McCollum'
__email__ = 'jathan@gmail.com'
__version__ = '0.2'

import collections 

__all__ = ('DictObject',)

class DictObject(collections.MutableMapping, dict):
    """
    Recursively represent a dict and any nested dicts as objects while also
    still behaving like a dict.

    Source: http://stackoverflow.com/a/6573827/194311

    It inherits from dict so that isinstance checks will identify it as a dict.

    :param obj:
        A dictionary-like object

    :param recursive:
        Whether to recursively convert inner dicts. (Default: True)

    :param unicode_keys:
        Whether to allow dictionary keys to be Unicode. (Default: False)
    """
    def __init__(self, obj, recursive=True, unicode_keys=False):
        if not unicode_keys:
            try:
                obj = self.__class__._kwdict(obj)
            except AttributeError:
                raise TypeError("'obj' must be a dictionary-like object!")

        # Recursively turn everything into an object
        if recursive:
            attrs = self._recursive_object(obj)
        # Or just the top-level items
        else:
            attrs = self._simple_object(obj, unicode_keys=unicode_keys)

        # And update our attributes
        self.__dict__.update(attrs)

    @classmethod
    def _simple_object(cls, obj, unicode_keys=False):
        """
        Convert the top-level dicts into non-recursive objects and return the
        dict of objects.

        :param obj:
            A dictionary-like object

        :param unicode_keys:
            Whether to allow dictionary keys to be Unicode. (Default: False)
        """
        if not isinstance(obj, dict):
            return obj

        n = {}
        for k, v in obj.iteritems():
            if isinstance(v, dict):
                n[k] = cls(v, recursive=False, unicode_keys=unicode_keys)
            else:
                n[k] = v
        return n

    @classmethod
    def _recursive_object(cls, obj):
        """
        Recursively convert all dicts and nested dicts, lists, or tuples into a
        object and return the resultant object.

        A list or tuple of dicts will be returned as a list of objects.

        Anything not a dict, or list/tuple of dicts will be returned as-is.

        :param obj:
            A dictionary-like object
        """
        # Convert a nested dicts into Structs and iterate nested lists/tuples
        # to convert into list of Structs
        if isinstance(obj, dict):
            n = {}
            for ikey, ival in obj.iteritems():
                if isinstance(ival, dict):
                    n[ikey] = cls(ival)
                elif isinstance(ival, (list, tuple)):
                    n[ikey] = [cls(item) for item in ival]
                else:
                    n[ikey] = ival
            return n

        # Convert a list/tuple of dicts into a list of Structs
        elif isinstance(obj, (list, tuple)):
            L = []
            for item in obj:
                L.append(cls(item))
            return L

        # Or return object as-is
        else:
            return obj

    @classmethod
    def _kwdict(cls, kwargs):
        """
        Make sure dictionary keyword are not in Unicode.

        This should be fixed in newer Python versions, see:
            http://bugs.python.org/issue4978.

        :param kwargs:
            A dictionary-like object
        """
        return dict((key.encode('utf-8'), value) for key, value in
                    kwargs.iteritems())

    def __repr__(self):
        return '{%s}' % str(', '.join('%s: %s' % (repr(k), repr(v)) for
            (k, v) in self.__dict__.iteritems()))

    # collections.MutableMapping requires these to be defined to dictate the
    # dictionary-like behavior. 

    def __getitem__(self, val):
        return self.__dict__[val]

    def __setitem__(self, key, val):
        self.__dict__[key] = val

    def __delitem__(self, key):
        del self.__dict__[key]

    def __len__(self):
        return len(self.__dict__)

    def __iter__(self):
        return iter(self.__dict__)

if __name__ == '__main__':
    data = {
        u'task': {
            u'id': u'b2833808-d9ee-4dfa-8b0c-1e4dec45a041',
            u'result': {'name': 'foo', 'value': 'bar'}
        }
    }

    d = DictObject(data)
    print '    id:', d.task.id
    print 'result:', d.task.result.value
