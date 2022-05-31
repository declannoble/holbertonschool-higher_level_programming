#!/usr/bin/python3
"""
module to read a text file and print to stdout
"""


def read_file(filename=""):
    """function that reads and prints files"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
