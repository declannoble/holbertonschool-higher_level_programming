#!/usr/bin/python3
"""
Module to return inverted operators
"""


class MyInt(int):
    """
    class which returns inverted operators
    """
    def __eq__(self, other):
        """
        Return the inverse of ==
        """
        return self.real != other

    def __ne__(self, other):
        """
        Return the inverse of !=
        """
        return self.real == other
