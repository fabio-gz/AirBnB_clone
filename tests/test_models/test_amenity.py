#!/usr/bin/python3
"""
Test for the Amenity Class
"""
import unittest
import pep8
import datetime
from models.amenity import Amenity

class test_Amenity(unittest.TestCase):
    """
    Tester for the class Amenity
    """
    @classmethod
    def setUpClass(self):
        """Run method prior test
        """
        self.amenity = Amenity()
        self.amenity.name = "aromatherapy"

    def Testpep8(self):
        """Test for pep8 styleguide on the file
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.checkfile(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         'Found code style errors (and warning).')

    def test_data(self):
        """Test data assigment
        """
        self.assertIsInstance(self.amenity.name, str)
        self.assertIsInstance(self.amenity, Amenity)

    def test_save(self):
        """Test save method on Amenity class
        """
        self.amenity.save()
        self.assertIsInstance(self.amenity.created_at, datetime.datetime)

    def test_dict(self):
        """Test the output of the dictionary
        """
        self.assertIn('name', self.amenity.__dict__)

    def test_empty_agmt(self):
        """test for the none argument
        """
        self.amenity.name = None
        self.assertIsNone(self.amenity.name)
