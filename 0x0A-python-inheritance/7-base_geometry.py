#!/usr/bin/python3
""" module creating a class BaseGeometry """


class BaseGeometry:

    def area(self):
        """raising exception when called """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validating data"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
