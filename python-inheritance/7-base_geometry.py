#!/usr/bin/python3
"""Module that defines BaseGeometry with area and integer_validator methods."""


class BaseGeometry:
    """A base class for geometry shapes with validation functionality."""

    def area(self):
        """Raise an Exception indicating area is not implemented.

        Raises:
            Exception: Always raises with message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): The name of the parameter (used in error messages).
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
