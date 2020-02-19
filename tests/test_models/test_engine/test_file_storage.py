#!/usr/bin/python3
""" UnitTest for file storage """
import pep8
import uuid
import unittest
import os
from models.engine.file_storage import FileStorage


class test_FileStorage(unittest.TestCase):

      """ Unittest for class FileStorage """
      def test_pep8_conformance(self):
            """ test for pep8 styleguide """
            pep8style = pep8.StyleGuide(quiet=True)
            result = pep8style.check_files(['models/engine/file_storage.py'])
            self.assertEqual(result.total_errors, 0,
                             'Found code style errors (and warnings).')

      def test_all(self):
            file_t = FileStorage()
            x = file_t.all()
            self.assertIsInstance(x, dict)

if __name__ == "__main__":
      unittest.main()
