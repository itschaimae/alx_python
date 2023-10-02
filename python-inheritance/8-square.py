# 8-square.py

class BaseGeometry:
    """
    A base class representing basic geometry.
    """
    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: This method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that a value is an integer and greater than 0.

        Args:
            name (str): A string representing the name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    A class representing a rectangle with width and height.
    """
    def __init__(self, width, height):
        """
        Initialize a rectangle with a given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle in the format "[Rectangle] <width>/<height>".
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """
    A class representing a square, which is a special case of a rectangle with equal sides.
    """
    def __init__(self, size):
        """
        Initialize a square with a given size.

        Args:
            size (int): The size of the square (equal sides).
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string representation of the square in the format "[Square] <size>/<size>".
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
