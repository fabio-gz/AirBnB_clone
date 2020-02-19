#!/usr/bin/python3
"""
Test for the City Class
"""
import unittest
import pep8
import datetime
from models.city import City


class test_City(unittest.TestCase):
    """
    Tester for the class City
    """
    @classmethod
    def setUpClass(self):
        """Run method prior test
        """
        self.city = City()
        self.city.state_id = "12345"
        self.city.name = "Bucaramanga"

    def Testpep8(self):
        """Test for pep8 styleguide on the file
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.checkfile(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         'Found code style errors (and warning).')

    def test_data(self):
        """Test data assigment
        """
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city, City)
        self.assertEqual(self.city.name, "Bucaramanga")

    def test_save(self):
        """Test save method on City class
        """
        self.city.save()
        self.assertIsInstance(self.city.created_at, datetime.datetime)

    def test_dict(self):
        """Test the output of the dictionary
        """
        self.assertIn('name', self.city.__dict__)
        self.assertIn('state_id', self.city.__dict__)

    def test_empty_agmt(self):
        """test for the none argument
        """
        self.city.name = None
        self.assertIsNone(self.city.name)
