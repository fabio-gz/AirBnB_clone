#!/usr/bin/python3
"""
Test for the console file
"""
import unittest
import pep8
import io
from unittest.mock import patch
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

    def test_help_c(self):
        """ test for help create command"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual("Creates a new instance of the class\n",
                             f.getvalue())

    def test_help_s(self):
        """ test for help show command"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual("Prints string rep of an instance\n", f.getvalue())

    def test_create_error(self):
        """test class not found"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create chair")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

    def test_show_error(self):
        """test class missing"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual("** class name missing **\n", f.getvalue())
