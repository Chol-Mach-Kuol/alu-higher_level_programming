#!/usr/bin/python3
"""Unittest for Square class."""
import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_basic_creation(self):
        """Test basic Square creation."""
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_id_auto(self):
        """Test auto id assignment."""
        s1 = Square(5)
        s2 = Square(3)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)

    def test_id_given(self):
        """Test given id."""
        s = Square(5, 0, 0, 12)
        self.assertEqual(s.id, 12)

    def test_size_getter_setter(self):
        """Test size getter and setter."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_type_error(self):
        """Test TypeError for size."""
        with self.assertRaises(TypeError) as e:
            s = Square(5)
            s.size = "9"
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_size_zero(self):
        """Test ValueError for zero size."""
        with self.assertRaises(ValueError) as e:
            Square(0)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_size_negative(self):
        """Test ValueError for negative size."""
        with self.assertRaises(ValueError) as e:
            Square(-1)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_x_negative(self):
        """Test ValueError for negative x."""
        with self.assertRaises(ValueError) as e:
            Square(5, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_y_negative(self):
        """Test ValueError for negative y."""
        with self.assertRaises(ValueError) as e:
            Square(5, 0, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_area(self):
        """Test area method."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        """Test display method."""
        s = Square(2)
        with patch('sys.stdout', new=StringIO()) as out:
            s.display()
            self.assertEqual(out.getvalue(), "##\n##\n")

    def test_display_with_xy(self):
        """Test display with x and y offsets."""
        s = Square(2, 2, 1)
        with patch('sys.stdout', new=StringIO()) as out:
            s.display()
            self.assertEqual(out.getvalue(), "\n  ##\n  ##\n")

    def test_str(self):
        """Test __str__ method."""
        s = Square(5, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (3) 1/2 - 5")

    def test_update_args(self):
        """Test update with args."""
        s = Square(5)
        s.update(10, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (10) 3/4 - 2")

    def test_update_kwargs(self):
        """Test update with kwargs."""
        s = Square(5)
        s.update(size=7, y=1)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.y, 1)

    def test_update_args_over_kwargs(self):
        """Test that args take priority over kwargs."""
        s = Square(5)
        s.update(10, 2, size=7)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 2)

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        s = Square(10, 2, 1, 1)
        d = s.to_dictionary()
        self.assertEqual(d, {'id': 1, 'size': 10, 'x': 2, 'y': 1})

    def test_x_type_error(self):
        """Test TypeError for x."""
        with self.assertRaises(TypeError) as e:
            Square(5, "1")
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_y_type_error(self):
        """Test TypeError for y."""
        with self.assertRaises(TypeError) as e:
            Square(5, 0, "1")
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_bool_size(self):
        """Test TypeError for bool size."""
        with self.assertRaises(TypeError):
            Square(True)


if __name__ == '__main__':
    unittest.main()
