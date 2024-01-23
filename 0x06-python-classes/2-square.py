#!/usr/bin/python3
"""
Docstyle for the class Square
"""


class Square:
    """
    __init__ is used for initialization of various objects
    """
    def __init__(self, size=0):

        """
        Note:
            do not include the self ithin the args
        Args:
            size: stands for the size of the Square
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
