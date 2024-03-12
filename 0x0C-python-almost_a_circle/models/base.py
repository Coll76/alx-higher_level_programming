#!/usr/bin/python3
"""
This class will be the “base” of all other
classes in this project
"""

import json


class Base:
    """
    private class attribute
    """
    __nb_objects = 0
    """
    class constructor for initialization
    """
    def __init__(self, id=None):
        """
        Parameters:
            id: if id is not None assign public instance id ith id
            else increament __nb_objects
        """
        if id is not None:
            self.id = id
        else:
            id = Base.__nb_objects = Base.__nb_objects = Base.__nb_objects + 1
            self.id = id
        """
        Dictionary to JSON string
        """
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            json_of_dict = json.dumps(list_dictionaries)
            return json_of_dict
        """
        writes the JSON string representation of list_objs to a file:
        """
    @classmethod
    def save_to_file(cls, list_objs):
        """
        JSON string to file
        """
        if list_objs is None:
            list_objs = []
        file_name = f'{cls.__name__}.json'
        json_str = cls.to_json_string(list_objs)
        with open(file_name, 'w') as file_t:
            file_t.write(json_str)
