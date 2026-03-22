#!/usr/bin/python3
"""Module that provides a function to get a dict of an object's attributes."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a class whose attributes are all JSON-serializable.

    Returns:
        dict: The __dict__ of the object instance.
    """
    return obj.__dict__
