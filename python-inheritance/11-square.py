#!/usr/bin/python3
"""Module that defines Square with its own string representation."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square shape with its own string representation."""

    def __init__(self, size):
        """Initialize a Square with a validated size.

        Args:
            size (int): The side length of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return a string description of the square.

        Returns:
            str: The square in format '[Square] <size>/<size>'.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
