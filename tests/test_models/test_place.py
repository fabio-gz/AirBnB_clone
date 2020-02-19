#!/usr/bin/python3
"""
Test for the Place Class
"""
import unittest
import pep8
import datetime
from models.place import Place


class test_Place(unittest.TestCase):
    """
    Tester for the Place City
    """
    @classmethod
    def setUpClass(self):
        """Run method prior test
        """
        self.place = Place()
        self.place.city_id = "12345"
        self.place.user_id = "7777"
        self.place.name = "Cristian"
        self.place.description = "nice"
        self.place.number_rooms = 2
        self.place.number_bathrooms = 3
        self.place.max_guest = 5
        self.place.prince_by_night = 100
        self.place.latitude = 3.5
        self.place.longitude = 4.7
        self.place.amenity_ids = ['aromatherapy', 'tennis']

    def Testpep8(self):
        """Test for pep8 styleguide on the file
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.checkfile(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         'Found code style errors (and warning).')

    def test_data(self):
        """Test data assigment
        """
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)
        self.assertIsInstance(self.place, Place)
        self.assertEqual(self.place.name, "Cristian")

    def test_save(self):
        """Test save method on Place class
        """
        self.place.save()
        self.assertIsInstance(self.place.created_at, datetime.datetime)

    def test_dict(self):
        """Test the output of the dictionary
        """
        self.assertIn('name', self.place.__dict__)
        self.assertIn('user_id', self.place.__dict__)
        self.assertIn('amenity_ids', self.place.__dict__)

    def test_empty_agmt(self):
        """test for the none argument
        """
        self.place.name = None
        self.assertIsNone(self.place.name)
