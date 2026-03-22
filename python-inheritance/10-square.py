#!/usr/bin/python3
"""Module that defines Square inheriting from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square shape defined by a single size value."""

    def __init__(self, size):
        """Initialize a Square with a validated size.

        Args:
            size (int): The side length of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
