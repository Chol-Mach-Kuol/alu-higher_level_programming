#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """Defines a square by its size (private, no validation)."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: The size of the square (no type/value verification).
        """
        self.__size = size
