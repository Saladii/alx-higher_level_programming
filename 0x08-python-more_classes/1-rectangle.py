#!/usr/bin/python3
""" class Ractangle """


class Rectangle:
    """
    Rectangle that defines a rectangle by:
    Private instance attribute: width (int)
    Private instance attribute: height (int)
    Instantiation with optional width and heigh
    """

    def __init__(self, width=0, height=0):
        """ construct method """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ geetter width property """
        return self._width

    @property
    def height(self):
        """ getter height property """
        return self.__height

    @width.setter
    def width(self, value):
        """ setter width property """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ setter height property """
        if not isinstance(value, int):
            raise TypeError('heght must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
