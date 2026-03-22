#!/usr/bin/python3
"""Module for Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size: The size of the square.
            x: The x position of the square.
            y: The y position of the square.
            id: The id of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation of Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update Square attributes with args or kwargs.

        Args:
            args: Arguments in order: id, size, x, y.
            kwargs: Key/value pairs of attributes to update.
        """
        attrs = ['id', 'size', 'x', 'y']
        if args and len(args) > 0:
            for i, val in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], val)
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """Return dictionary representation of Square.

        Returns:
            Dictionary with id, size, x, y.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
