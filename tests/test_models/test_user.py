#!/usr/bin/python3
"""
Test for the User class
"""
import unittest
import pep8
import datetime
from models.user import User
from models.base_model import BaseModel

class test_User(unittest.TestCase):
    """
    Tester for the class user
    """
    @classmethod
    def setUpClass(self):
        """run method prior test
        """
        self.user = User()
        self.user.email = "fabio@fabio.com"
        self.user.password = "12345"
        self.user.first_name = "fabio"
        self.user.last_name = "gomez"

    def Testpep8(self):
        """Test for pep8 styleguide on the file
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.checkfiles(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         'Found code style errors (and warning).')

    def test_data(self):
        """Test the data assigment
        """
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertEqual(self.user.first_name, "fabio")
        self.assertIsInstance(self.user, User)

    def test_save(self):
        """Test save method on User class
        """
        self.user.save()
        self.assertIsInstance(self.user.created_at, datetime.datetime)

    def test_dict(self):
        """Test to check the dictionary created
        """
        self.assertIn('password', self.user.__dict__)
        self.assertIn('email', self.user.__dict__)
        self.assertIn('first_name', self.user.__dict__)
        self.assertIn('last_name', self.user.__dict__)

    def test_empty_agmt(self):
        """Test if the data provided is None
        """
        self.user = User()
        self.user.email = None
        self.user.password = None

        self.assertIsNone(self.user.email)
        self.assertIsNone(self.user.password)
