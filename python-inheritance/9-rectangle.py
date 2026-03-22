#!/usr/bin/python3
"""Module that defines a full Rectangle with area and string representation."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle shape with area computation and string representation."""

    def __init__(self, width, height):
        """Initialize a Rectangle with validated width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """Return a string description of the rectangle.

        Returns:
            str: The rectangle in format '[Rectangle] <width>/<height>'.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
