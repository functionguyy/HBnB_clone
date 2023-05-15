#!/usr/bin/python3
"""Test Module Place class"""
import unittest
from models.place import Place
import os


class TestPlace(unittest.TestCase):
    """
    Test suite for place class
    """

    def test_create_instance(self):
        """
        Test that creates an instance of State
        """
        place = Place()
        self.assertIsInstance(place, Place)
        os.remove('file.json')

    def test_attribute_name(self):
        """
        Test that has attr name as an empty string
        """
        place = Place()
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(len(place.name) == 0)
        os.remove('file.json')

    def test_attribute_name_1(self):
        """
        Test that setting name works
        """
        place = Place()
        place.name = "Busumbala"
        self.assertEqual(place.name, "Busumbala")
        os.remove('file.json')

    def test_attribute_description_1(self):
        """
        Test that has attr description and is empty
        """
        place = Place()
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(len(place.description) == 0)
        os.remove('file.json')

    def test_attribute_description_2(self):
        """
        Test that setting attr description works
        """
        place = Place()
        place.description = "Nice place"
        self.assertTrue(place.description == "Nice place")
        os.remove('file.json')

    def test_attributes_3(self):
        """
        Test other attributes
        """
        new_place = Place()
        self.assertTrue(hasattr(new_place, "number_rooms"))
        self.assertEqual(new_place.number_rooms, 0)
        self.assertTrue(hasattr(new_place, "number_bathrooms"))
        self.assertEqual(new_place.number_bathrooms, 0)
        self.assertTrue(hasattr(new_place, "max_guest"))
        self.assertEqual(new_place.max_guest, 0)
        self.assertTrue(hasattr(new_place, "price_by_night"))
        self.assertEqual(new_place.price_by_night, 0)
        self.assertTrue(hasattr(new_place, "latitude"))
        self.assertEqual(new_place.latitude, 0.0)
        self.assertTrue(hasattr(new_place, "longitude"))
        self.assertEqual(new_place.longitude, 0.0)
        self.assertTrue(hasattr(new_place, "amenity_ids"))
        self.assertEqual(new_place.amenity_ids, [])
        os.remove('file.json')


if __name__ == "__main__":
    unittest.main()
