#!/usr/bin/python3
"""
class Square that inherits from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    __init__ is used as class constructor
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Parameters:
            size(int): width and height must be assigned to the value of size
            x(int): co-ordinate of square
            y(int): co-ordinate of square
            id: unique for the square
        """
        super().__init__(size, size, x, y, id)
        """
        __str__ gives an informal string repesentation of an object
        """
    def __str__(self):
        """
        return string repesentation of an object
        """
        return f'[Square] ({self.id}) {self.__x}/{self.__y} - {self.__width}'
    """
    area method to override that of superclass Rectangle
    """
    def area(self):
        """
        overrides that of superclass Rectangle
        """
        return self.__width * self.__height
    """
    method to print to stdout as well as override that of Rectangle
    """
    def display(self):
        """
        print to stdout uses #
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__height)
    """
    getter for size
    """
    @property
    def size(self):
        """
        retrieves the size value of Square
        """
        return self.__width
    """
    setter for size
    """
    @size.setter
    def size(self, value):
        """
        sets the size to value
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('size should be > 0')
        self.__width = value
        self.__height = value
    """
    Update the class Square by adding the public method
    def update(self, *args, **kwargs) that assigns attributes
    """
    def update(self, *args, **kwargs):
        """
        Update the class Square
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__size = args[1]
            if len(args) >= 3:
                self.__x = args[2]
            if len(args) >= 4:
                self.__y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.__size = kwargs['size']
            if 'y' in kwargs:
                self.__y = kwargs['y']
            if 'x' in kwargs:
                self.__x = kwargs['x']
        """
        returns the dictionary representation of a Square
        """
    def to_dictionary(self):
        """
        returns the dictionary representation of a Square
        """
        return {
            'id': self.id,
            'size': self.__size,
            'x': self.__x,
            'y': self.__y
            }
if __name__ == "__main__":
    s1 = Square(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)
    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

