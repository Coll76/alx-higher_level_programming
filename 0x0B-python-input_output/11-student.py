#!/usr/bin/python3
"""
class Student that defines a student by: (based on 9-student.py)
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        __init__ used for initialization
        Args:
            first_name: first name
            last_name: last name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        """
        retrieves a dictionary representation of a Student
        """
    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student
        """
        if attrs is None:
            return self.__dict__
        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result
    """
    replaces all attributes of the Student instance
    """
    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
