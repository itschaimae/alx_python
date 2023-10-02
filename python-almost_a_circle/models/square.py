"""
models.square
=============

This module defines the Square class, which inherits from the Rectangle class and represents squares.

Classes:
    - Square: The Square class for managing square attributes.

"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    The Square class represents a square and inherits from the Rectangle class.

    Attributes:
        size (int): Size of the square.
        x (int): X-coordinate of the square.
        y (int): Y-coordinate of the square.

    Args:
        size (int): Size of the square.
        x (int, optional): X-coordinate of the square (default is 0).
        y (int, optional): Y-coordinate of the square (default is 0).
        id (int, optional): An integer representing the ID (default is None, which generates a new ID).

    Methods:
        __init__(self, size, x=0, y=0, id=None): Initialize a new Square instance.
        __str__(self): Return a string representation of the square.
        update(self, *args, **kwargs): Update the attributes of the square.
        size(self): Getter method for retrieving the size of the square.
        size(self, value): Setter method for setting the size of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.

        Args:
            size (int): Size of the square.
            x (int, optional): X-coordinate of the square (default is 0).
            y (int, optional): Y-coordinate of the square (default is 0).
            id (int, optional): An integer representing the ID (default is None, which generates a new ID).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size of the square.

        Args:
            value (int): The size to set for the square.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string in the format "[Square] (<id>) <x>/<y> - <size>".
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

