"""
models.rectangle
================

This module defines the Rectangle class, which inherits from the Base class and represents rectangles.

Classes:
    - Rectangle: The Rectangle class for managing rectangle attributes.

"""

from models.base import Base

class Rectangle(Base):
    """
    The Rectangle class represents a rectangle and inherits from the Base class.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): X-coordinate of the rectangle.
        y (int): Y-coordinate of the rectangle.

    Args:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int, optional): X-coordinate of the rectangle (default is 0).
        y (int, optional): Y-coordinate of the rectangle (default is 0).
        id (int, optional): An integer representing the ID (default is None, which generates a new ID).

    Methods:
        area(self): Calculate and return the area of the rectangle.
        display(self): Display the rectangle using "#" characters.
        __str__(self): Return a string representation of the rectangle.
        update(self, *args, **kwargs): Update the attributes of the rectangle.
    """
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X-coordinate of the rectangle (default is 0).
            y (int, optional): Y-coordinate of the rectangle (default is 0).
            id (int, optional): An integer representing the ID (default is None, which generates a new ID).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Display the rectangle using "#" characters.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string in the format "[Rectangle] (<id>) <x>/<y> - <width>/<height>".
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle.

        Args:
            *args: Variable-length arguments (id, width, height, x, y) in that order.
            **kwargs: Keyword arguments for updating specific attributes (id, width, height, x, y).
        """
        if args:
            arg_names = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, arg_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

