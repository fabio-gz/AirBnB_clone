#!/usr/bin/python3
"""
Test for the Amenity Class
"""
import unittest
import pep8
import datetime
from models.state import State


class test_State(unittest.TestCase):
    """
    Tester for the class State
    """
    @classmethod
    def setUpClass(self):
        """Run method prior test
        """
        self.state = State()
        self.state.name = "Santander"

    def Testpep8(self):
        """Test for pep8 styleguide on the file
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.checkfile(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         'Found code style errors (and warning).')

    def test_data(self):
        """Test data assigment
        """
        self.assertIsInstance(self.state.name, str)
        self.assertIsInstance(self.state, State)
        self.assertEqual(self.state.name, "Santander")

    def test_save(self):
        """Test save method on Amenity class
        """
        self.state.save()
        self.assertIsInstance(self.state.created_at, datetime.datetime)

    def test_dict(self):
        """Test the output of the dictionary
        """
        self.assertIn('name', self.state.__dict__)

    def test_empty_agmt(self):
        """test for the none argument
        """
        self.state.name = None
        self.assertIsNone(self.state.name)
