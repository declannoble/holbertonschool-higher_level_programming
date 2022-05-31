#!/usr/bin.python3
"""
module to append string at end of file
"""


def append_write(filename="", text=""):
    """ function to append string"""
    with open(filename, "s", encoding="utf-8") as f:
        return f.write(text)
