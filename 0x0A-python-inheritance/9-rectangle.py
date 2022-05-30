#!/usr/bin/python3
""" Module creates a rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initialising data"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of a rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """returns an informal string representation of a rectangle"""
        return (f"[Rectangle] {self.__width}/{self.__height}")
