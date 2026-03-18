#!/usr/bin/python3
"""Module that provides a function to write a string to a UTF-8 text file."""


def write_file(filename="", text=""):
    """Write a string to a text file and return the number of chars written.

    Creates the file if it does not exist; overwrites it if it does.

    Args:
        filename (str): Path to the file to write. Defaults to empty string.
        text (str): The string content to write. Defaults to empty string.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
