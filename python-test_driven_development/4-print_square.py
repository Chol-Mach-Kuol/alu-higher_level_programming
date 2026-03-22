#!/usr/bin/python3
"""Module for printing a square.

This module provides a function to print a square of a given size
using the '#' character.
"""


def print_square(size):
    """Prints a square with the character '#' of the given size.

    Raises TypeError if size is not an integer or is a negative float.
    Raises ValueError if size is less than 0.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
