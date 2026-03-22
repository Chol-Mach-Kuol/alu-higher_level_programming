#!/usr/bin/python3
"""Module for Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
            x: The x position of the rectangle.
            y: The y position of the rectangle.
            id: The id of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x attribute."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y attribute."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle instance with the character #."""
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return string representation of Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update Rectangle attributes with args or kwargs.

        Args:
            args: Arguments in order: id, width, height, x, y.
            kwargs: Key/value pairs of attributes to update.
        """
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) > 0:
            for i, val in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], val)
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """Return dictionary representation of Rectangle.

        Returns:
            Dictionary with id, width, height, x, y.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
