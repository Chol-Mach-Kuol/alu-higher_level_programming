#!/usr/bin/python3
"""Module that checks if an object is exactly an instance of a given class."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, else False.

    Args:
        obj: The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if type(obj) is a_class, False otherwise.
    """
    return type(obj) is a_class
