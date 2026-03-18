#!/usr/bin/python3
"""Module that provides a function to read and print a UTF-8 text file."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its content to stdout.

    Args:
        filename (str): Path to the file to read. Defaults to empty string.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
