#!/usr/bin/python3
"""
function that creates an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”
    Parameter:
        filename: JSON file
    """
    with open(filename, 'r', encoding='UTF-8') as file_t:
        fil = json.load(file_t)
    return fil
