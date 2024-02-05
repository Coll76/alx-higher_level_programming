#!/usr/bin/python3
"""
checks for isinstance functionality
"""


def is_kind_of_class(obj, a_class):
    """
    Parameter:
        obj: object to check
        a_class: class to compare to
    Return: True if obj is of a_class else false
    """
    return isinstance(obj, a_class)
