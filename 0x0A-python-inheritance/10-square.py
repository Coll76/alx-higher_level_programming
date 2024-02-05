#!/usr/bin/python3
"""
Class Square that inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        __init__ is used for initialization
        Parameters:
            size: size of Square
        """
        self.integer_validator("size", size)
        self.__size = size
        """
        method to find area of Square
        """
    def area(self):
        """
        finds area of Square
        """
        return self.__size * self.__size
    """
    __str__ prints string representation of Rectangle
    """
    def __str__(self):
        """
        string representation of Rectangle
        """
        return f"[Rectangle] {self.__size}/{self.__size}"
