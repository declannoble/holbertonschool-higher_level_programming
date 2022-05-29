#!/usr/bin/python3
"""function returns true if object is instance of, or if object
is an instance of a class inherited from, the speicified class.
otherwise false
"""


def is_kind_of_class(obj, a_class):
    """returns true or false based on if object
    is an instance of a class that it's been inherited from
    """
    return(isinstance(obj, a_class))
