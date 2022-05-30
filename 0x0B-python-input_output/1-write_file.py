#!/usr/bin/python3
"""
module to write a string to a text file
and return number of chars written
"""


def write_file(filename="", text=""):
    """ Function to write string to file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
