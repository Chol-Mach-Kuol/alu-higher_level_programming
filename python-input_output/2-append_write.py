#!/usr/bin/python3
"""Module that provides a function to append a string to a text file."""


def append_write(filename="", text=""):
    """Append a string to a text file and return the number of chars added.

    Creates the file if it does not exist.

    Args:
        filename (str): Path to the file to append to. Defaults to "".
        text (str): The string content to append. Defaults to empty string.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
