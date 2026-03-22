#!/usr/bin/python3
"""Unittest for Rectangle class."""
import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_basic_creation(self):
        """Test basic Rectangle creation."""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_id_auto(self):
        """Test auto id assignment."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

    def test_id_given(self):
        """Test given id."""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_width_getter_setter(self):
        """Test width getter and setter."""
        r = Rectangle(10, 2)
        r.width = 5
        self.assertEqual(r.width, 5)

    def test_height_getter_setter(self):
        """Test height getter and setter."""
        r = Rectangle(10, 2)
        r.height = 5
        self.assertEqual(r.height, 5)

    def test_x_getter_setter(self):
        """Test x getter and setter."""
        r = Rectangle(10, 2)
        r.x = 5
        self.assertEqual(r.x, 5)

    def test_y_getter_setter(self):
        """Test y getter and setter."""
        r = Rectangle(10, 2)
        r.y = 5
        self.assertEqual(r.y, 5)

    def test_width_type_error(self):
        """Test TypeError for width."""
        with self.assertRaises(TypeError) as e:
            Rectangle(10, "2")
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_width_string(self):
        """Test TypeError for string width."""
        with self.assertRaises(TypeError) as e:
            Rectangle("10", 2)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_width_zero(self):
        """Test ValueError for zero width."""
        with self.assertRaises(ValueError) as e:
            Rectangle(0, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_width_negative(self):
        """Test ValueError for negative width."""
        with self.assertRaises(ValueError) as e:
            r = Rectangle(10, 2)
            r.width = -10
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_height_zero(self):
        """Test ValueError for zero height."""
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 0)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_height_negative(self):
        """Test ValueError for negative height."""
        with self.assertRaises(ValueError) as e:
            Rectangle(10, -2)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_x_type_error(self):
        """Test TypeError for x."""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 2)
            r.x = {}
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_x_negative(self):
        """Test ValueError for negative x."""
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_y_type_error(self):
        """Test TypeError for y."""
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 2, 3, "1")
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_y_negative(self):
        """Test ValueError for negative y."""
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_area(self):
        """Test area method."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_area_large(self):
        """Test area with large values."""
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)

    def test_display(self):
        """Test display method."""
        r = Rectangle(4, 2)
        with patch('sys.stdout', new=StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), "####\n####\n")

    def test_display_with_xy(self):
        """Test display with x and y offsets."""
        r = Rectangle(2, 2, 2, 2)
        with patch('sys.stdout', new=StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), "\n\n  ##\n  ##\n")

    def test_str(self):
        """Test __str__ method."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        """Test update with args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Test update with kwargs."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1, width=2)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.width, 2)

    def test_update_args_over_kwargs(self):
        """Test that args take priority over kwargs."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, height=5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        r = Rectangle(10, 2, 1, 9, 1)
        d = r.to_dictionary()
        self.assertEqual(d, {'id': 1, 'width': 10, 'height': 2,
                             'x': 1, 'y': 9})

    def test_bool_width(self):
        """Test TypeError for bool width."""
        with self.assertRaises(TypeError):
            Rectangle(True, 2)


if __name__ == '__main__':
    unittest.main()
