"""
Module: square

This module defines a class, Square, that represents a square with a private size attribute.

Classes:
    Square:
        This class provides a basic representation of a square with an attribute for its side length.
"""

class Square:
    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size: The size of the square's sides.
        """
        self.__size = size

