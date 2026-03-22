#!/usr/bin/python3
"""Module for adding two integers.

This module provides a function to add two integers or floats,
casting floats to integers before addition.
It raises TypeError for non-numeric inputs.
"""


def add_integer(a, b=98):
    """Adds two integers or floats, casting floats to integers.

    Returns the integer addition of a and b.
    Raises TypeError if a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
