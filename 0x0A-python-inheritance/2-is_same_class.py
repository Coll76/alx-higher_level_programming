#!/usr/bin/python3
"""
function to check if subclass
"""


def is_same_class(obj, a_class):
    """
    Parameters:
        obj: object for hich to check
        a_class: class to be considered
    Return:
        True if obj is an instace of a_class else False
    """
    if isinstance(obj, a_class):
        return type(obj) is a_class
