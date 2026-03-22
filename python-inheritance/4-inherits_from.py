#!/usr/bin/python3
"""Module that checks if an object is an instance of a subclass only."""


def inherits_from(obj, a_class):
    """Return True if obj's class inherited (directly or not) from a_class.

    Returns False if obj is a direct instance of a_class itself.

    Args:
        obj: The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj's class is a strict subclass of a_class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
