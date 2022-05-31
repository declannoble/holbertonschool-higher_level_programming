#!/usr/bin/python3
"""
class_to_json module
"""


def class_to_json(obj):
    """ function returns dictionary description for JSON object """
    return(obj.__dict__)
