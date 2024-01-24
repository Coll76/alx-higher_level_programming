#!/usr/bin/python3
"""
Docstyle for the class Square
"""


class Square:
    """
    __init__ ill be used for object initialization
    and helps factor out code to reduce redundancy
    """
    def __init__(self, size=0):
        """
        Note:
            `self` should not be included ithin the ``args``
        Args:
            size: this is the size of this Square
        the instance attribute e shall create ill be private
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        """
        function size ill be used to retrieve the size attribute
        assign the value argument the __size
        property defines the getter for size property
        """
    @property
    def size(self):
        """
        retrieves size
        """
        return self.__size
        """
        the setter
        size.setter decorator defines a setter for the size property
        """
    @size.setter
    def size(self, value):
        """
        used as a setter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        """
        finds area of Square
        """
    def area(self):
        """
        find area
        """
        return self.__size ** 2
