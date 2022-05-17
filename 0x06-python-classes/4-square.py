#!/usr/bin/python3
"""Represents a Square.
    Private instance attribute: size
    Instantiation with optional size
    Public instance method: area"""


class Square:
    """ Represents a class"""
    def __init__(self, size=0):
        """ Initialise the data."""
        self.__size = size

    @property
    def size(self):
        """ Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the current square area."""
        return self.__size ** 2
