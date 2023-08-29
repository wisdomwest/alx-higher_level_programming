#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side
    """
    def __init__(self, size):
        """Initializes a square
        Args:
            size (int): size of a side of square
        Returns: None
        """
        self.__size = size
