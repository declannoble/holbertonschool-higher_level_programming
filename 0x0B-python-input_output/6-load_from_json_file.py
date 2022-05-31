#!/usr/bin/python3
"""
load_from_json module
"""


import json

def load_from_json_file(filename):
    """
    function that creates object
    from a JSON file
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
