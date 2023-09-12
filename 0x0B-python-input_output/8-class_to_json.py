#!/usr/bin/python3
"""
Module contains class_to_json function
"""


def class_to_json(obj):
    """returns dictionary description JSON serialization of object"""
    return obj.__dict__
