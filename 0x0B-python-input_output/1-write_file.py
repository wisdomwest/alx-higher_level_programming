#!/usr/bin/python3
"""Module contains function wrtie_file"""


def write_file(filename="", text=""):
    """returns number chars written"""
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
