#!/usr/bin/python3
"""module contains is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """True if  instance or inherited from a_class, else False"""
    return (isinstance(obj, a_class))
