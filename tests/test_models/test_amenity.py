#!/usr/bin/python3
"""Test Module for amenity class"""
import unittest
from models.amenity import Amenity
import os


class TestAmenity(unittest.TestCase):
    """
    Test suite for amenity class
    """
    def test_create_amenity(self):
        """
        Test that creates amenity instance
        """
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, Amenity)
        os.remove('file.json')

    def test_amenity_attributes(self):
        """
        Test that has attr name
        """
        new_amenity = Amenity()
        self.assertTrue(hasattr(new_amenity, "name"))
        self.assertEqual(new_amenity.name, "")
        os.remove('file.json')

    def test_amenity_str_method(self):
        """
        Test string representation
        """
        new_amenity = Amenity()
        self.assertEqual(
            str(new_amenity),
            "[Amenity] ({}) {}".format(new_amenity.id, new_amenity.__dict__))
        os.remove('file.json')


if __name__ == "__main__":
    unittest.main()
