#!/usr/bin/python3
"""
function that writes an Object to a text
file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text
    file, using a JSON representation
    """
    with open(filename, 'w', encoding='UTF-8') as file_t:
        fil = json.dump(my_obj, file_t)
        return fil
