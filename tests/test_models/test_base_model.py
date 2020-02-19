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
        """run methof prior test
        """
        self.my_model = BaseModel()
        self.my_model.name = 'Skywalker'
        self.my_model.my_number = 70

    def Testpep8(self):
        """test for pep8 styleguide
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         'Found code style errors (and warnings).')

    def test_data(self):
        """data asignment
        """
        self.assertIsInstance(self.my_model.id, str)
        self.assertEqual(self.my_model.name, 'Skywalker')
        self.assertEqual(self.my_model.my_number, 70)
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)

    def test_save(self):
        """test save method to update instance attribute
        """
        self.my_model = BaseModel()
        self.my_model.save()

        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)
        self.assertNotEqual(self.my_model.created_at, self.my_model.updated_at)

    def test_to_dict(self):
        """test toc check dictionary values of the instance
        """
        self.my_model = BaseModel()
        d = self.my_model.to_dict()

        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['created_at'], self.my_model.created_at.isoformat())
        self.assertEqual(d['updated_at'], self.my_model.updated_at.isoformat())

    def test_empty_agmt(self):
        self.my_model = BaseModel()
        self.my_model.name = None
        self.my_model.my_number = None

        self.assertIsNone(self.my_model.name)
        self.assertIsNone(self.my_model.my_number)
