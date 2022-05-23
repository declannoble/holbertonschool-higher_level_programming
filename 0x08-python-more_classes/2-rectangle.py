#!/usr/bin/python3


class Rectangle:
    """ Defining an empty class Rectangle """
    def __init__(self, width=0, height=0):
        """ Initialising rectangle """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter for private instance attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter values for private instance attributes"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for private instance attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for private instance attribute """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of a rectangle """
        return (self.height * self.width)

    def perimeter(self):
        """returns the perimeter of a rectangle """
        return (self.height + self.height + self.width + self.width)
