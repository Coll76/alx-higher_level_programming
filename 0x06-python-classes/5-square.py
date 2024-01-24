#!/usr/bin/python3
"""
Docstyle for class Square
"""


class Square:
    """
    __init is used for object initialization
    """
    def __init__(self, size=0):
        """
        in this case e shall create an private instance attribute
        Note:
            self should not be included itin Args
        Args:
            size: size of the suare
        """
        self.__size = size
        """
        getter method to retrieve the size
        """
    @property
    def size(self):
        """
        retrieve the size attribute
        """
        return self.__size
    """
    setter method sets the size attribute
    """
    @size.setter
    def size(self, value):
        """
        set the size to value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        """
        area method is used to find area of suare
        """
    def area(self):
        """
        returns the current suare area
        """
        return self.__size ** 2
    """
    the my_print method prints output for area
    """
    def my_print(self):
        """
        prints the suare ith the character #
        """
        for _ in range(self.__size):
            if self.__size == 0:
                print()
            else:
                print("#" * self.__size)
