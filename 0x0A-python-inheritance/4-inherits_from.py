#!/usr/bin/python3
"""inherits_from module """


def inherits_from(obj, a_class):
    """returns True or False based on inheritance"""
    if issubclass(obj, a_class) is True and type(obj) != a_class:
        return True

    else:
        return False
