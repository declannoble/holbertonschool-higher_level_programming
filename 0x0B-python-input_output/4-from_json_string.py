#!/usr/bin/python3
"""
module to return object represented
by a JSON string
"""


import json


def from_json_string(my_str):
    """
    function to return object
    from JSON string
    """
    return json.loads(my_str)
