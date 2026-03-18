#!/usr/bin/python3
"""Module that provides a function to serialize an object to a JSON string."""
import json


def to_json_string(my_obj):
    """Return the JSON string representation of an object.

    Args:
        my_obj: The Python object to serialize.

    Returns:
        str: The JSON representation of my_obj.
    """
    return json.dumps(my_obj)
