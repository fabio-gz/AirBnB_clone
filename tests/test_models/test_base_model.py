#!/usr/bin/python3
"""
Test for base model class
"""
import datetime
import uuid
import unittest
import pep8
from models.base_model import BaseModel


class test_BaseModel(unittest.TestCase):
    """tester for base class"""

    @classmethod
    def setUpClass(self):
        """run methof prior test"""
        self.my_model = BaseModel()
        self.my_model.name = 'Skywalker'
        self.my_model.my_number = 70

    def Testpep8(self):
        """test for pep8 styleguide"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         'Found code style errors (and warnings).')

    def test_data(self):
        self.assertIsInstance(self.my_model.id, str)
        self.assertEqual(self.my_model.name, 'Skywalker')
        self.assertEqual(self.my_model.my_number, 70)
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)
