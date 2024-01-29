#!/usr/bin/python3
"""
Docstyle for class Rectangle
"""


class Rectangle:
    """
    Class Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        __init__ used to initialize objects/instances
        Note:
            self should not be ritten ithin the Args
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.__width = width
        self.__height = height
        """
        getter for height
        """
    @property
    def height(self):
        """
        retrieves the height private instance variable
        """
        return self.__height
    """
    setter for height
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
        """
        retrieves the private instance variable
        """
    @property
    def width(self):
        """
        getter for width
        """
        return self.__width
    """
    setter for width
    """
    @width.setter
    def width(self, value):
        """
        sets the instance width variable to value
        """
        if not isinstance(value, int):
            raise NameError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
        """
        method for Area of rectangle
        """
    def area(self):
        """
        return area of rectangle
        """
        return self.__height * self.__width
        """
        method for perimeter of Rectangle
        """
    def perimeter(self):
        """
        returns perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__height * 2 + self.__width * 2
