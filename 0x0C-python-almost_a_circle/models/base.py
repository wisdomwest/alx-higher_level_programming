#!/usr/bin/python3
"""Module contains class Base"""


class Base:
    """This class will be base of all classes"""

    __nb_objects = 0

    def __init__(self, _id=None):
        """Set private attributes id fields"""
        if _id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = _id
