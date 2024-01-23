#!/usr/bin/python3
"""
Docstyle for class Square
"""


class Square:
    """
    set the size attribute to private
    """

    __size = None

    def __init__(self, _Square_size):
        """
        The __init__ is used as a constructor
        Note:
            Do not include `self` in the ``Args``
        Args:
            _Square_size: the size of Square
        """

        if _Square_size is not None:
            self._Square_size = _Square_size
