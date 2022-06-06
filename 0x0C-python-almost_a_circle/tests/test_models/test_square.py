#!/usr/bin/python3
"""
Test for the Square class
"""

import unittest
import inspect
from models import square
from models.base import Base
Square = square.Square


class TestSquareDocs(unittest.TestCase):
    """Tests the Square class' style and documentation"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.sq_funcs = inspect.getmembers(Square, inspect.isfunction)

    def test_module_docstring(self):
        """Tests for the presence of a module docstring"""
        self.assertTrue(len(square.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the presence of a class docstring"""
        self.assertTrue(len(Square.__doc__) >= 1)



class TestSquare(unittest.TestCase):
    """Test the functionality of the Square class"""
    @classmethod
    def setUpClass(cls):
        """set up the tests"""
        Base._Base__nb_objects = 0
        cls.s1 = Square(1)
        cls.s2 = Square(2, 3)
        cls.s3 = Square(4, 5, 6)
        cls.s4 = Square(7, 8, 9, 10)

    def test_size(self):
        """Test for functioning size"""
        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s2.size, 2)
        self.assertEqual(self.s3.size, 4)
        self.assertEqual(self.s4.size, 7)

    def test_width(self):
        self.assertEqual(self.s1.width, 1)
        self.assertEqual(self.s2.width, 2)
        self.assertEqual(self.s3.width, 4)
        self.assertEqual(self.s4.width, 7)

    def test_height(self):
        """Test for functioning height"""
        self.assertEqual(self.s1.height, 1)
        self.assertEqual(self.s2.height, 2)
        self.assertEqual(self.s3.height, 4)
        self.assertEqual(self.s4.height, 7)

    def test_x(self):
        """Test for functioning x"""
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 3)
        self.assertEqual(self.s3.x, 5)
        self.assertEqual(self.s4.x, 8)

    def test_y(self):
        """Test for functioning y"""
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s3.y, 6)
        self.assertEqual(self.s4.y, 9)

    def test_noArgs(self):
        """Test with no args"""
        with self.assertRaises(TypeError):
            s = Square()

    def test_sizeWrongData(self):
        """Test non-ints for size"""
        with self.assertRaises(TypeError):
            s = Square("hello")
        with self.assertRaises(TypeError):
            s = Square(True)

    def test_xWrongData(self):
        """Test non-ints for x"""
        with self.assertRaises(TypeError):
            s = Square(1, "hello")
        with self.assertRaises(TypeError):
            s = Square(1, True)

    def test_yWrongData(self):
        """Test non-ints for y"""
        with self.assertRaises(TypeError):
            s = Square(1, 1, "hello")
        with self.assertRaises(TypeError):
            s = Square(1, 1, True)

    def test_size_neg(self):
        """Test ints <= 0 for size"""
        with self.assertRaises(ValueError):
            s = Square(-1)
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_x_neg(self):
        """Test ints < 0 for x"""
        with self.assertRaises(ValueError):
            s = Square(1, -1)

    def test_y_neg(self):
        """Test ints <= 0 for y"""
        with self.assertRaises(ValueError):
            s = Square(1, 1, -1)

    def test_area(self):
        """test area"""
        self.assertEqual(self.s1.area(), 1)
        self.assertEqual(self.s2.area(), 4)
        self.assertEqual(self.s3.area(), 16)
        self.assertEqual(self.s4.area(), 49)

    def test_issubclass(self):
        """test to check sub class"""
        self.assertTrue(issubclass(Square, Base), True)

    def test_tooManyArgs(self):
        """tests for too many arguments"""
        with self.assertRaises(TypeError):
            s = Square(1, 2, 3, 4, 5, 6, 7, 8, 9)

    def test_setter(self):
        """tests setter"""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.size, 1)
        s.size = 100
        self.assertEqual(s.size, 100)
