#!/usr/bin/python3
"""
This is file to add intergers.
The 0-add_integer module has one fumction add_integer(a, b).
"""

def add_integer(a, b):
    """Return the addition of a and b."""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    
    a = int(a)
    b = int(b)
    
    return a + b
