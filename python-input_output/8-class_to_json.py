#!/usr/bin/python3
"""transfo object python in a dict for make compatibility with JSON"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for JSON serialization of an object."""
    return obj.__dict__
