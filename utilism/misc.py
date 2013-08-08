# -*- coding: utf-8 -*_

"""
Miscellaneous utilities.
"""

__author__ = 'Jathan McCollum'
__maintainer__ = 'Jathan McCollum'
__email__ = 'jathan@gmail.com'
__version__ = '0.1'

import os

# Used by dprint()
DEBUG = os.getenv('DEBUG', False)

__all__ = ('dprint',)

def dprint(*args, **kwargs):
    """
    Pretty-print the passed in values if global ``DEBUG`` is set.

    You may also set the DEBUG environment variable prior to importing this
    function or module.
    """
    if DEBUG:
        for a in args:
            print a
        for k,v in kwargs.iteritems():
            print '%s = %s' % (k.upper(), v)
        if args and kwargs:
            print

if __name__ == '__main__':
    DEBUG = 1
    dprint('\nTest 1', bacon='delicious', numbers=range(1,11))
    dprint('Hello, World!')
    dprint('\nTest 2', foo='bar', data={'a':1, 'b':2})
    DEBUG = 0
    dprint("You won't see this!")
    dprint("Or this.")
