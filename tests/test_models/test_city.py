#!/usr/bin/python3
"""Test Module for the city class"""
from models.city import City
import unittest
import os


class TestCity(unittest.TestCase):
    """Test suite for city class
    """
    def test_create_city(self):
        """
        Test that create city instance
        """
        new_city = City()
        self.assertIsInstance(new_city, City)
        os.remove('file.json')

    def test_city_attributes(self):
        """
        Test instance attributes
        """
        new_city = City()
        self.assertTrue(hasattr(new_city, "state_id"))
        self.assertEqual(new_city.state_id, "")
        self.assertTrue(hasattr(new_city, "name"))
        self.assertEqual(new_city.name, "")
        os.remove('file.json')

    def test_city_str_method(self):
        """
        Test string representation
        """
        new_city = City()
        self.assertEqual(
            str(new_city),
            "[City] ({}) {}".format(new_city.id, new_city.__dict__))
        os.remove('file.json')


if __name__ == "__main__":
    unittest.main()
