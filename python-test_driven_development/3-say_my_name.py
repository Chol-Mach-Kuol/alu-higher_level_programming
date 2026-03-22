#!/usr/bin/python3
"""Module for printing a name.

This module provides a function to print a formatted name string
with first and last name validation.
"""


def say_my_name(first_name, last_name=""):
    """Prints 'My name is <first_name> <last_name>'.

    Raises TypeError if first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
