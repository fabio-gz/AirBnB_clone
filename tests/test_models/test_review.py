#!/usr/bin/python3
"""
Test for the Review Class
"""
import unittest
import pep8
import datetime
from models.review import Review


class test_Review(unittest.TestCase):
    """
    Tester for the class Review
    """
    @classmethod
    def setUpClass(self):
        """Run method prior test
        """
        self.review = Review()
        self.review.place_id = "12345"
        self.review.user_id = "9999"
        self.review.text = "good place"

    def Testpep8(self):
        """Test for pep8 styleguide on the file
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.checkfile(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         'Found code style errors (and warning).')

    def test_data(self):
        """Test data assigment
        """
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review, Review)
        self.assertEqual(self.review.text, "good place")

    def test_save(self):
        """Test save method on City class
        """
        self.review.save()
        self.assertIsInstance(self.review.created_at, datetime.datetime)

    def test_dict(self):
        """Test the output of the dictionary
        """
        self.assertIn('text', self.review.__dict__)
        self.assertIn('place_id', self.review.__dict__)

    def test_empty_agmt(self):
        """test for the none argument
        """
        self.review.name = None
        self.assertIsNone(self.review.name)
