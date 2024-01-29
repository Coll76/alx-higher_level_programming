class Rectangle:
    """
    class id Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        __init__ is used for object initialization
        Note:
            self should not be included in the args
        Args:
            idth: width of rectangle
            height: height of rectangle
        """
        self.__width = width
        self.__height = height
        """
        getter for height
        """
    @property
    def height(self):
        """
        retrieves the private height instance variable
        """
        return self.__height
    """
    setter for height
    """
    @height.setter
    def height(self, value):
        """
        sets the value of height tovalue
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
        """
        getter for width
        """
    @property
    def width(self):
        """
        retrieves the width
        """
        return self.__width
    """
    setter for width
    """
    @width.setter
    def width(self, value):
        """
        sets the width to value
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
        """
        method that finds area
        """
    def area(self):
        """
        returns area of rectangle
        """
        return self.__height * self.__width
    """
    method that finds perimeter of rectangle
    """
    def perimeter(self):
        """
        returns perimeter of rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return self.__height * 2 + self.__width * 2
    """
    returns an informal string representation of an object
    """
    def __str__(self):
        """
        returns an informal string representation of an object
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])
    """
    repr used to create a ne object ith eval()
    """
    def __repr__(self):
        """
        can be used to create a ne instance using eval
        """
        return f"Rectangle({repr(self.__width)}, {repr(self.__height)})"
    """
    method that deletes an instnce
    """
    def __del__(self):
        """
        deletes an object
        """
        print("Bye rectangle...")
