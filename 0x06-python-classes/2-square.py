#!/usr/bin/python3
""" Defining a square class with a private instance attribute 'size' """
class Square:
    """instantiating data"""
    def __init__(self, size=0):
        """instantiating data"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                """instantiate with size"""
                self.__size = size
