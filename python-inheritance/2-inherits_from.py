"""
Module: 2-inherits_from
This module contains a function to check if an object is an instance of a class that directly or indirectly inherits from a specified class.
"""

def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherits (directly or indirectly) from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a subclass of the specified class; otherwise, False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
