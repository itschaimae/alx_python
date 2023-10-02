"""
Module: square

This module defines a class, Square, that represents a square with a private size attribute.

Classes:
    Square:
        This class provides a basic representation of a square with an attribute for its side length.

        Attributes:
            __size (int): The size of the square's sides.

        Methods:
            __init__(self, size=0):
                Initializes a new Square instance with a given size.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
"""

class Square:
    def __init__(self, size=0):
        """
        Initializes a new Square instance with a given size.

        Args:
            size (int, optional): The size of the square's sides. Default is 0.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size


