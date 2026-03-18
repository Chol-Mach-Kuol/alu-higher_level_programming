#!/usr/bin/python3
"""Module that checks if an object is instance of a class or its subclass."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or a subclass of it.

    Args:
        obj: The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or inherits from it.
    """
    return isinstance(obj, a_class)
