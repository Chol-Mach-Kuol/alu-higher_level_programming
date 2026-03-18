#!/usr/bin/python3
"""Module that defines MyList, a subclass of list with sorted printing."""


class MyList(list):
    """A list subclass that can print its elements in sorted order."""

    def print_sorted(self):
        """Print the list elements sorted in ascending order.

        The original list is not modified.
        """
        print(sorted(self))
