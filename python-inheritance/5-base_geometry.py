"""
Module: 5-base_geometry
This module defines a class, BaseGeometry, with an area() method and an integer_validator() method.
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

