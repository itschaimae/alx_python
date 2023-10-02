"""
Module: square

This module defines a simple class, Square, that represents a square with private attributes for size.

Classes:
    Square:
        This class represents a square with methods to manipulate its size and calculate area and perimeter.
"""
class Square:
       """
    This class represents a square.

    Attributes:
        __size (int): The size of the square's sides.
    """
    
    def __init__(self, size):
        
        self.__size = size
