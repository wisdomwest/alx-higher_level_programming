#!/usr/bin/python3
"""Module contains class rectangle"""

from models.base import Base


class Rectangle(Base):
    """represent rectangle object inherit from base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle Object"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.height = height
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter width property"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """function for area of rectangle"""
        return self.width * self.height

    def display(self):
        """function to display triangle in #"""
        for k in range(self.y):
            print("")

        for k in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """string rep of rectangle"""
        s1 = "[{}] ({}) ".format(self.__class__.__name__, self.id)
        s2 = "{}/{} - {}/{}".format(self.x, self.y, self.width, self.height)
        return s1 + s2

    def update(self, *args, **kwargs):
        """update method assigns arguement to attributes"""
        if args or len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    if args[i] is None:
                        self.__init__(
                                self.width, self.height, self.x, self.y)
                    else:
                        self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]
        else:
            if kwargs or len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        if value is None:
                            self.__init__(
                                    self.width, self.height, self.x, self.y)
                        else:
                            self.id = value
                    if key == "width":
                        self.width = value
                    if key == "height":
                        self.height = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value
