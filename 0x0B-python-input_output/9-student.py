#!/usr/bin/python3
"""
Docstyle for class Student
"""


class Student:
    """
    class Student that defines a student by: (based on 9-student.py)
    """
    def __init__(self, first_name, last_name, age):
        """
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
    def to_json(self):
        """
        retrieves a dictionary representation of a Student
        """
        result = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }
        return result
