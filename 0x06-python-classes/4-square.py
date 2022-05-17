#!/usr/bin/python3
class Square:
    """Represents a Square"""

    def __init__(self, size=0):
        """ Initialises data"""
        self.__size = size

    @property
    def size(self):
        """ gets size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets size."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the current square area."""
        return self.__size ** 2
