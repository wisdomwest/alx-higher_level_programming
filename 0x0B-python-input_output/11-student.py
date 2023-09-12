#!/usr/bin/python3
"""Module contains clas Student"""


class Student:
    """Representation of class student"""
    def __init__(self, first_name, last_name, age):
        """Initialize student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation of class Student """
        if attrs is None:
            return self.__dict__
        new = {}
        for i in attrs:
            try:
                new[i] = self.__dict__[i]
            except FileNotFoundError:
                pass
        return new

    def reload_from_json(self, json):
        """replaces attributes of Student """
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
