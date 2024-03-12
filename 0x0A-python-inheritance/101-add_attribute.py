#!/usr/bin/python3
"""
function that adds a new attribute to an object if it’s possible
"""


class add_attribute(MyClass):
    """
    adds a new attribute to an object if it’s possible
    """
    def __init__(self, obj, name, value):
        """
        __init is used for initialization
        """
        self.name = name
        self.value = value
        self.obj = obj
