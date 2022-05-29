#!/usr/bin/python3
"""
Function that returns available attributes and methods of an object

"""

def lookup(obj):
    """return a list of attributes """
    return(dir(obj))
