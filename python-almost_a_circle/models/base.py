
"""
models.base
============

This module defines the Base class, which serves as the foundation for managing ID attributes in other classes.

Classes:
    - Base: The Base class for managing IDs.

Module Attributes:
    - __all__ (List[str]): A list of module names that should be imported when using "from models.base import *".

"""

__all__ = ['Base']

class Base:
    """
    The Base class serves as the foundation for managing ID attributes in other classes.

    Attributes:
        __nb_objects (int): A private class attribute used to generate unique IDs.

    Args:
        id (int, optional): An integer representing the ID. If provided, the instance is assigned the given ID.
            If not provided, a new ID is generated automatically.

    Attributes:
        id (int): A public instance attribute representing the ID of the instance.

    Methods:
        __init__(self, id=None): Constructor method for creating a new Base instance.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.

        Args:
            id (int, optional): An integer representing the ID. If provided, the instance is assigned the given ID.
                If not provided, a new ID is generated automatically.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
