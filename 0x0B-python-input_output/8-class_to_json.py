#!/usr/bin/python3
"""
function that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object:
"""


def class_to_json(obj):
    """
    returns the dictionary description
    """
    if not hasattr(obj, '__dict__'):
        return obj
    reslt = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            reslt[key] = value
        if hasattr(value, '__dict__'):
            reslt[key] = class_to_json(value)
        else:
            pass
    return reslt
