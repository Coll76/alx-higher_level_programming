#!/usr/bin/python3
"""
Rectangle that inherits from Base
"""


from models.base import Base
import json


class Rectangle(Base):
    """
    __init__ is used for initialization and acts as a class constructor
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Parameters:
            width(int): width of rectangle
            height(int): height
            x(int): co-ordinate of the rectangle
            y(int): co-ordinate of the rectangle
            id(int): identifier of thr rectangle
        """
        self.validator('width', width)
        self.validator('height', height)
        self.validator('y', y)
        self.validator('x', x)
        super().__init__(id)
        """
        acts as a validator
        """
    def validator(self, attribute_name, value):
        """
        validates the attributes
        """
        if not isinstance(value, int):
            raise TypeError(f'{attribute_name} must be an integer')
        if attribute_name in {'width', 'height'} and value <=0:
            raise ValueError(f'{attribute_name} must be > 0')
        if attribute_name in {'x', 'y'} and value < 0:
            raise ValueError(f'{attribute_name} must be >= 0')
        setattr(self, f'_{type(self).__name__}__{attribute_name}', value)
        """
        getter to retrieve the privatewidth instance width variable
        """
    @property
    def width(self):
        """
        retrieve instaance attribute
        """
        return self.__width
    """
    setter for width
    """
    @width.setter
    def width(self, value):
        self.validator('width', value)
    """
    getter to retrieve thr private height instance
    """
    @property
    def height(self):
        """
        retrieve thr height instance attribute
        """
        return self.__height
    """
    setter for height
    """
    @height.setter
    def height(self, value):
        """
        sets the private instance height
        """
        self.validator('height', value)
    """
    getter for private instace x
    """
    @property
    def x(self):
        """
        retrieves the private instace x
        """
        return self.__x
    """
    setter for x
    """
    @x.setter
    def x(self, value):
        """
        sets the private instance x to value
        """
        self.validator('x', value)
        """
        getter for the private instance y
        """
    @property
    def y(self):
        """
        retrieve thr private instance y
        """
        return self.__y
    """
    sets the private instance y
    """
    @y.setter
    def y(self, value):
        """
        sets the private instance y to value
        """
        self.validator('y', value)
        """
        returns the area value of the Rectangle instance.
        """
    def area(self):
        """
        returns the area value of the Rectangle instance.
        """
        return self.__width * self.__height
    """
    model that prints in stdout the Rectangle
    instance with the character #
    """
    def display(self):
        """
        prints in stdout the Rectangle instance
        """
        if self.__width is not None or self.__height is not None:
            for _ in range(self.__y):
                print()
            for _ in range(self.__height):
                print(' ' * self.__x + '#' * self.__width)
        """
        __str__ to provide a string representation of the
        object and it enhances readability and represents your objects
        as strings and enables customization to include specific information
        that is relevant to the class
        """
    def __str__(self):
        """
        __string representation of the object
        """
        return (
                f'[Rectangle] ({self.id}) {self.__x}/{self.__y} - '
                f'{self.__width}/{self.__height}'
                )
        """
        assigns an argument to each attribute:
        Update the class Rectangle by adding the public method
        """
    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']
            if 'id' in kwargs:
                self.id = kwargs['id']
        """
        Rectangle instance to dictionary representation
        """
    def to_dictionary(self):
        """
        converts to JSON format
        """
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
            }
