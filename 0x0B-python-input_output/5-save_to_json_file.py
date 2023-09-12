#!/usr/bin/python3
"""Module contains function save_to_json_file"""

import json


def save_to_json_file(my_obj, filename):
    """convert object to text file using JSON representation"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
