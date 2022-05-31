#!/usr/bin/python3
"""
class Student module
"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        function to retrieve dict
        representation of Student instance
        """
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        else:
            newdict = {}
            for x in attrs:
                if type(x) is not str:
                    return self.__dict__
                if x in self.__dict__:
                    newdict[x] = self.__dict__[x]
            return newdict
