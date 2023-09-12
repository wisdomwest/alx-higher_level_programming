#!/usr/bin/python3
"""Module contains function that create Object from JSON file"""

import json


def load_from_json_file(filename):
    """create object from JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
