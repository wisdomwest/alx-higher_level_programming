#!/usr/bin/python3
"""Module contains the JSON"""

import json


def to_json_string(my_obj):
    """returns JSON representation of object"""
    return json.dumps(my_obj)
