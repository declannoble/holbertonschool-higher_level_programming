#!/usr/bin/python3
""" Function that returns True if object is exactly
    an instance of specified class, otherwise False.
"""

def is_same_class(obj, a_class):
    """checks if instance is of a class"""
    return(type(obj) == a_class)
