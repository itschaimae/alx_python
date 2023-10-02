
"""
Module: square

This module defines the Square class, which represents a square shape.

Classes:
    Square: A class for representing a square shape.
"""

class Square:
    """
    Square class represents a square shape.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a new Square instance with the given size.
        size (property): Gets the size of the square.
        size (setter): Sets the size of the square, raising TypeError and ValueError if invalid values are provided.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square and raises TypeError and ValueError if invalid values are provided.

        Args:
            value (int): The new size to set.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.__size = value
