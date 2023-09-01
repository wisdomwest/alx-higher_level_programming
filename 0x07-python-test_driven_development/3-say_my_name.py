#!/usr/bin/python3
"""
The 3-say_my_name module has one function, say_my_name.
"""

def say_my_name(first_name, last_name=""):
    """Prints "My name is" first name and optional last name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
