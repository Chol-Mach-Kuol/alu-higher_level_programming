#!/usr/bin/python3
"""Module that defines a Rectangle class with customizable print symbol."""


class Rectangle:
    """Defines a rectangle with a configurable print symbol."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle and increment instance counter.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle.

        Returns:
            int: The current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle.

        Returns:
            int: The current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter, or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation using the print_symbol.

        Returns:
            str: The rectangle drawn with print_symbol, or empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        row = str(self.print_symbol) * self.__width
        return "\n".join(row for _ in range(self.__height))

    def __repr__(self):
        """Return a string to recreate the instance using eval().

        Returns:
            str: A string in the form 'Rectangle(width, height)'.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a farewell message and decrement instance counter."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
