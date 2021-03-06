#!/usr/bin/python3
"""
Defines an empty rectangle class
"""


class Rectangle:
    """ Defining an empty class Rectangle """
    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returning the rectangle with the largest area """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __init__(self, width=0, height=0):
        """ Initialising rectangle """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __del__(self):
        """ rectangle being deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
        return (self.__height * self.__width)

    def perimeter(self):
        """returns the perimeter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__height + self.__width + self.__width)

    def __str__(self):
        """ prints a # representation of a rectangle """

        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            if i < self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """ returns a string representation of the rectangle """
        return(f"Rectangle({self.__width},{self.__height})")
