#!/usr/bin/python3
"""
Docstyle for class Rectangle
"""


class Rectangle:
    """
    class Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        __init__ is used for initializing objects/instances
        Note:
            self should not be ithin Args
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.__width = width
        self.__height = height
        """
        acts as a getter to retrieve the width
        """
    @property
    def width(self):
        """
        retrieve width
        """
        return self.__width
    """
    acts as a setter to set the width to value
    """
    @width.setter
    def width(self, value):
        """
        set the idth to value
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
        """
        acts a getter for height of Rectangle
        """
    @property
    def height(self):
        """
        returns private height of Rectangle
        """
        return self.__height
    """
    acts as a setter for height using value
    """
    @height.setter
    def height(self, value):
        """
        sets height to value
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
