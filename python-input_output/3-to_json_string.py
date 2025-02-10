#!/usr/bin/python3
"""Create a function that converts a
    Python object into a JSON-formatted string"""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
