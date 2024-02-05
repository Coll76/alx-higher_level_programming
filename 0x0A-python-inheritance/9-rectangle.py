#!/usr/bin/python3
"""
class Rectangle that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        __init__ is used for initialization
        self: should not be included in the parameters
        Parameters:
            width: rectangle width
            height: rectangle height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        """
        For area of Rectangle
        """
    def area(self):
        """
        Return area of Rectangle
        """
        return self.__width * self.__height
    """
    __str__ used for string representation of the rectangle
    """
    def __str__(self):
        """
        informal rep of Rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
