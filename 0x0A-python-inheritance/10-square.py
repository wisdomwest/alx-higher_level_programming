#!/usr/bin/python3
"""Module contains class BaseGeometry and subclass Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """representation of class square"""
    def __init__(self, size):
        """instant square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"returns area of square"""
        return self.__size ** 2
