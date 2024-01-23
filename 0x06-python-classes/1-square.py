#!/usr/bin/python3
"""
Docstyle for class Square
"""


class Square:
    """
    set the size attribute to private
    """

    __size = None

    def __init__(self, size=None):
        """
        The __init__ is used as a constructor
        Note:
            Do not include `self` in the ``Args``
        Args:
            _Square_size: the size of Square
        """

        if size is not None:
            _Square_size = size
            self._Square_size = _Square_size
