#!/usr/bin/python3
"""Module contains json from_json_string"""

import json


def from_json_string(my_str):
    """returns object represented by JSON"""
    return json.loads(my_str)
