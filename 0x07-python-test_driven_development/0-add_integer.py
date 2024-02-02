#!/usr/bin/python3
"""
fuction used to add integers
"""


def add_integer(a, b=98):
    """
    adds integers
    Parameters:
        a (int or float): first number
        b (int or float): second number

    Returns:
        int: sum of a and b

    Raises:
        TypeError: if a or b are neither int nor float

    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(100.3, -2)
        98
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
