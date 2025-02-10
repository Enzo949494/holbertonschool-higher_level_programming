#!/usr/bin/python3
"""convert string JSON in object python"""

import json


def from_json_string(my_str):
    """Return object (Python data structure) represented by a JSON string."""
    return json.loads(my_str)
