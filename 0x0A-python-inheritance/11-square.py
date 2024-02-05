#!/usr/bin/python3
"""
class Square that inherits from Rectangle (9-rectangle.py)
"""


Rectangle = __import__('10-square').Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        __init__ is used for initialization
        Parameter:
            size: size of Square
        """
        self.__size = size
        """
        Method to find area of Square
        """
    def area(self):
        """
        finds area of Square
        """
        return self.__size * self.__size
    """
    __str__ for string representation of class Square
    """
    def __str__(self):
        """
        string representation of class Square
        """
        return f"[Square] {self.__size}/{self.__size}"
