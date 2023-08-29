#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Rep a square
    Attributes:
        __size (int): size of a side of square
    """
    def __init__(self, size=0):
        """initialize square
        Args:
            size (int): size of a side of square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """computes the square's area
        Returns:
            The area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """get  __size
        Returns:
            The size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """set __size
        Args:
            value (int): the size of a size of square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
