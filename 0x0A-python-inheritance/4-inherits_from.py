#!/usr/bin/python3
"""
issubclass functionality
"""


def inherits_from(obj, a_class):
    """
    Parameters:
        obj: object to check if its subclass of a_class
        a_class: class to check if its the base class
    Return: True if obj is subclass of a_class else false
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
