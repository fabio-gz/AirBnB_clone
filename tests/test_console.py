#!/usr/bin/python3
"""
Test for the console file
"""
import unittest
import pep8
from console import HBNBCommand


class test_HBNBCommand(unittest.TestCase):
    """Class test for console"""

    def Testpep8(self):
        """test for pep8 styleguide
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         'Found code style errors (and warnings).')
