#!/usr/bin/python3
"""Module contains function append_write"""


def append_write(filename="", text=""):
    """returns number of characters"""
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
