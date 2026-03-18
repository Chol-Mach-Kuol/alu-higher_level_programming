#!/usr/bin/python3
"""Module that defines a Student class with serialization and reload."""


class Student:
    """Defines a student with full serialization and deserialization."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of the Student instance.

        Args:
            attrs (list): Optional list of attribute names to include.
                If None, all attributes are returned.

        Returns:
            dict: A dictionary of the student's attributes.
        """
        if isinstance(attrs, list):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance from a dictionary.

        Args:
            json (dict): A dictionary mapping attribute names to their values.
        """
        for key, value in json.items():
            setattr(self, key, value)
