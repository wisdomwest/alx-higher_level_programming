#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Rep a square
    Attributes:
        __size (int): size of a side of square
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of a side of square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """computes the area
        Returns:
            The area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """get __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """set__size
        Args:
            value (int): size of a side of square
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

    def my_print(self):
        """prints the square #
        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
