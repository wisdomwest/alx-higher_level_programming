#!/usr/bin/python3
"""Module contains clas Student"""


class Student:
    """Representation of class student"""
    def __init__(self, first_name, last_name, age):
        """Initialize student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary representation of class Student """
        return self.__dict__
