#!/usr/bin/python3
"""
class MyInt inherits from int
"""


class MyInt(int):
    """
    has == and != operators inverted
    """
    def __eq__(self, other):
        """
        changes == to !=
        other represents right hand side of the comparison
        """
        return super().__ne__(other)
    """
    changes != to ==
    """
    def __ne__(self, other):
        """
        other represents right hand side of the comparison
        """
        return super().__eq__(other)
