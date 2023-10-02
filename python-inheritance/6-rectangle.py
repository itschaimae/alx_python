"""
Module: 6-rectangle
This module defines a class, Rectangle, which inherits from BaseGeometry and represents a rectangle.
"""

class BaseGeometry:
    """
    A class representing basic geometry with an area() method and integer validation.
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
            name: A string representing the name of the value.
            value: The value to be validated.

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
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
