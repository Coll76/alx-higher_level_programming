#!/usr/bin/python3
"""
Docstyle for the class Square
"""


class Square:
    """
    __init__ is used for object initialization
    """
    def __init__(self, size=0):
        """
        Note:
            `self` should not be ritten in ``Args``
        Args:
            size: this stands for size of Square
        """

        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        """
        area is used to find the total area of Square
        """
    def area(self):
        """
            Note:
                `self` should not be ritten in ``Args`
        """
        return self.__size ** 2
