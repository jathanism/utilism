# -*- coding: utf-8 -*-

"""
Resolve v4/v6 hostnames
"""

__author__ = 'Jathan McCollum'
__maintainer__ = 'Jathan McCollum'
__email__ = 'jathan@gmail.com'
__version__ = '0.1'

import socket

__all__ = ('resolve', 'reverse')

def resolve(host):
    """
    Resolve an IPv4 or IPv6 hostname to an address.

    :param host:
        The host to resolve!
    """
    port = None # Hard-code for now
    try:
        info = socket.getaddrinfo(host, port)
    except socket.gaierror:
        return host
    else: 
        # Take the first 5-tuple and use its address
        family, socktype, proto, canonname, sockaddr = info[0]

    addr, port = sockaddr # e.g. ('74.125.239.48', 0)
    return addr

def reverse(addr):
    """
    Resolve an IPv4 or IPv6 address to a hostname.

    :param addr:
        The address to lookup!
    """
    port = 0 # Hard-code for now
    flags = 0 # Just use the default
    try:
        info = socket.getnameinfo((addr, port), flags)
    except socket.gaierror:
        return addr
    else:
        host, port = info

    return host
