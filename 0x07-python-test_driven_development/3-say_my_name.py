#!/usr/bin/python3
"""
function that prints name of a person
"""


def say_my_name(first_name, last_name=""):
    """
    Parameters:
        @first_name: first name of individual
        @flast_name: last name of individual
    Prints:
        string: full name of person
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print(f"My name is {first_name} {last_name}")
