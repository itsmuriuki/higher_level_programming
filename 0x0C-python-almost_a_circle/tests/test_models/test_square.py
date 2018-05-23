#!/usr/bin/python3
"""Unittest for Square class file"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import sys


class TestSquare(unittest.TestCase):

    """Unittest for the Square class"""

    def test_setter_getter_size(self):
        """Test getter and setter"""

        Base._Base__nb_objects = 0

        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)

        self.assertEqual(s1.size, 5)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s3.size, 3)

    def test_square_id(self):
        """Test square id"""

        Base._Base__nb_objects = 0

        s1 = Square(5)
        self.assertEqual(s1.id, 1)

        s2 = Square(2, 2)
        self.assertEqual(s2.id, 2)

        s3 = Square(3, 1, 3)
        self.assertEqual(s3.id, 3)

    def test_display_square1(self):
        """Test display function"""

        Base._Base__nb_objects = 0

        s1 = Square(3)
        loc_stdout = StringIO()
        sys.stdout = loc_stdout
        s1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("###\n###\n###\n", loc_stdout.getvalue())

    def test_display_square2(self):
        """Test display function"""

        Base._Base__nb_objects = 0

        s2 = Square(2, 2)
        loc_stdout = StringIO()
        sys.stdout = loc_stdout
        s2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("  ##\n  ##\n", loc_stdout.getvalue())

    def test_display_square3(self):
        """Test display function"""

        Base._Base__nb_objects = 0

        s3 = Square(3, 1, 3)
        loc_stdout = StringIO()
        sys.stdout = loc_stdout
        s3.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("\n\n\n ###\n ###\n ###\n", loc_stdout.getvalue())

    def test_square_area(self):
        """Test area function"""

        Base._Base__nb_objects = 0

        s1 = Square(3)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)

        self.assertEqual(s1.area(), 9)
        self.assertEqual(s2.area(), 4)
        self.assertEqual(s3.area(), 9)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 3)

    def test_string_format1(self):
        """Test format of string"""

        Base._Base__nb_objects = 0

        s1 = Square(3)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 3")

    def test_string_format2(self):
        """Test format of string"""

        Base._Base__nb_objects = 0

        s2 = Square(2, 2)
        self.assertEqual(s2.__str__(), "[Square] (1) 2/0 - 2")

    def test_string_format3(self):
        """Test format of string"""

        Base._Base__nb_objects = 0

        s3 = Square(3, 1, 3)
        self.assertEqual(s3.__str__(), "[Square] (1) 1/3 - 3")

    def test_update_square_orig(self):
        """Test update function"""

        Base._Base__nb_objects = 0

        s1 = Square(5)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")

    def test_update_square_1args(self):
        """Test update function"""

        Base._Base__nb_objects = 0
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 5")

    def test_update_square_2args(self):
        """Test update function"""

        Base._Base__nb_objects = 0
        s1 = Square(5)
        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")

    def test_update_square_3args(self):
        """Test update function"""

        Base._Base__nb_objects = 0
        s1 = Square(1, 2)
        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/0 - 2")

    def test_update_square_4args(self):
        """Test update function"""

        Base._Base__nb_objects = 0
        s1 = Square(1, 2, 3)
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")

    def test_update_square_1kwarg(self):
        """Test update function"""

        Base._Base__nb_objects = 0

        s1 = Square(1, 2, 3, 4)
        s1.update(x=12)
        self.assertEqual(s1.__str__(), "[Square] (4) 12/3 - 1")

    def test_update_square_2kwarg(self):
        """Test update function"""

        Base._Base__nb_objects = 0

        s1 = Square(1, 2, 12, 4)
        s1.update(size=7, y=1)
        self.assertEqual(s1.__str__(), "[Square] (4) 2/1 - 7")

    def test_update_square_3kwarg(self):
        """Test update function"""

        Base._Base__nb_objects = 0

        s1 = Square(1, 7, 12, 1)
        s1.update(size=8, id=89, y=2)
        self.assertEqual(s1.__str__(), "[Square] (89) 7/2 - 8")

    def test_to_dictionary_square(self):
        """Test dictionary function"""

        Base._Base__nb_objects = 0

        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        expected_dict = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1_dictionary, expected_dict)

        s1.update(10, 10, 10, 10)
        s1_dictionary = s1.to_dictionary()
        expected_dict = {'id': 10, 'x': 10, 'size': 10, 'y': 10}
        self.assertEqual(s1_dictionary, expected_dict)

    def test_dictionary_json(self):
        """Test dictionary to json"""

        Base._Base__nb_objects = 0

        s1 = Square(10, 7, 2, 8)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        expected_dict = {'size': 10, 'x': 7, 'y': 2, 'id': 8}
        self.assertEqual(dictionary, expected_dict)
        self.assertEqual(type(dictionary), dict)
        expected_json = "[{\"size\": 10, \"x\": 7, \"y\": 2, \"id\": 8}]"
        self.assertEqual(json_dictionary, expected_json)
        self.assertEqual(type(json_dictionary), str)


if __name__ == '__main__':
    unittest.main()
