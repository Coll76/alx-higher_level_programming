#!/usr/bin/python3
"""
Integer validator
Write a class BaseGeometry (based on 6-base_geometry.py)
"""


class BaseGeometry:
    """
    Docstyle for BaseGeometry
    """
    def area(self):
        """
        raises an Exception with the message area() is not implemented
        """
        raise Exception('area() is not implemented')
    """
    validates value
    """
    def integer_validator(self, name, value):
        """
        Parameters:
          self: stands for object
          name: always a string
          value: alays an integer > 0
        self: should not be included in the parameters
        """
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
