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

    @classmethod
    def tearDownClass(self):
        """End the test
        """
        try:
            remove("file.json")
        except:
            pass

    def Testpep8(self):
        """test for pep8 styleguide
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py',
                                        'models/user.py', 'models/amenity.py',
                                        'models/city.py', 'models/state.py',
                                        'models/place.py', 'models/review.py'])
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
        self.my_model.name = 'Skywalker'
        self.my_model.save()
        d = self.my_model.to_dict()

        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)
        self.assertNotEqual(self.my_model.created_at, self.my_model.updated_at)
        self.assertEqual(d['name'], 'Skywalker')

        self.my_model.name = 'Vader'
        self.my_model.save()
        d2 = self.my_model.to_dict()
        self.assertEqual(d['created_at'], d2['created_at'])


    def test_str_(self):
        """
        test the str representation
        """
        self.my_model = BaseModel()
        srep = ("[{}] ({}) {}".format(self.my_model.__class__.__name__,
                                      self.my_model.id, self.my_model.__dict__))
        self.assertEqual(srep, str(self.my_model))

    def test_to_dict(self):
        """test toc check dictionary values of the instance
        """
        self.my_model = BaseModel()
        d = self.my_model.to_dict()

        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['created_at'], self.my_model.created_at.isoformat())
        self.assertEqual(d['updated_at'], self.my_model.updated_at.isoformat())

    def test_empty_agmt(self):
        """No argument passes
        """
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        self.assertEqual("__init__() missing 1 required"+
                         " positional argument: 'self'", str(e.exception))
