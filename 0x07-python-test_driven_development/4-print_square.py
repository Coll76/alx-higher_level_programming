#!/usr/bin/python3
"""
function that prints a square with the character #
"""


def print_square(size):
    """
    Parameter:
        size: represents size of suare
    Prints:
        square with the character #
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) == float and size < 0:
        raise TypeError('size must be an integer')
    print("\n".join("#" * size for _ in range(size)))
