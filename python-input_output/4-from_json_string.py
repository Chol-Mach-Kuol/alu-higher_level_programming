#!/usr/bin/python3
"""Module that provides a function to deserialize a JSON string."""
import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string.

    Args:
        my_str (str): A JSON-formatted string to deserialize.

    Returns:
        object: The Python data structure represented by my_str.
    """
    return json.loads(my_str)
