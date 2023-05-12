#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Base model test suite"""

    def test_instance_id(self):
        """
            Test that a BaseModel instance has a unique ID when Created
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_id_is_string(self):
        """
        Test that id is a string
        """
        bm = BaseModel()
        self.assertIsIstance(bm.id, str)

    def test_large_instance_ids(self):
        """
        Test for the unique ids of a large number of ids
        """
        ids = set()
        for i in range(1000):
            bm = BaseModel()
            ids.add(bm.id)
        self.assertEqual(len(ids), 1000)

    def test_created_at_assigned_at_current_time(self):
        """
            Test that created_at is assigned the current datetime
            when an instance is created
        """
        bm1 = BaseModel()
        created_at = bm1.created_at
        current_time = datetime.now
        self.assertEqual(created_at, current_time)

    def test_created_at_and_updated_at(self):
        """
        Test that created_at and updated_at attrs are equal
        """
        bm = BaseModel()
        created_at = bm.created_at
        updated_at = bm.updated_at
        self.assertEqual(created_at, updated_at)

    def test_created_at_is_string(self):
        """
        Test that created_at is a string
        """
        bm = BaseModel()
        created_at = bm.created_at
        self.assertIsInstance(created_at, datetime)

    def test_updated_at_is_string(self):
        """
        Test that updated_at is a string
        """
        bm = BaseModel()
        updated_at = bm.updated_at
        self.assertIsInstance(updated_at, datetime)

    def test_string_method(self):
        """
        Test that the str is producing the right output
        """
        bm = BaseModel()

        bm.name = "Omar Jammeh"
        bm.number = "123545"

        expected_output = "[BaseModel] ({}) {}".format(bm.id, bm.__dict__)
        self.assertEqual(str(bm), expected_output)

    def test_to_dict_returns_all_attr_values(self):
        """
            Test that to_dict method returns a dictionary containing
            all keys values of dict of the instance
        """
        bm1 = BaseModel()
        bm1.id = "123"
        bm1.created_at = "2022-05-09T14:30:00.000000"
        bm1.updated_at = "2022-05-09T14:30:00.000000"
        bm1.name = "example"
        bm1.number = 42

        bm_dict = bm1.to_dict()

        self.assertEqual(bm_dict['id'], "123")
        self.assertEqual(bm_dict['created_at'], "2022-05-09T14:30:00.000000")
        self.assertEqual(bm_dict['updated'], "2022-05-09T14:30:00.000000")
        self.assertEqual(bm_dict['name'], "example")
        self.assertEqual(bm_dict['number'], 42)

    def test_to_dict_unknown_attrs(self):
        """
        Test for unknown attrs
        """
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertTrue('unknown' not in bm_dict)

    def test_to_dict_contains_class_key(self):
        """
            Test that dictionary contains __class__ key
        """
        bm = BaseModel()

        bm_dict = bm.to_dict()

        self.assertTrue("__class__" in bm_dict)
        self.assertEqual(bm_dict['__class__'], 'BaseModel')

    def test_to_dict_iso_format(self):
        """
            Test that the to_dict method converts created_at and
            update_at to string object in ISO format.
        """
        bm = BaseModel()

        bm_dict = bm.to_dict()

        created_at = bm.created_at
        updated_at = bm.updated_at
        self.assertTrue(isinstance(bm_dict['created_at'], str))
        self.assertTrue(isinstance(bm_dict['updated_at'], str))
        self.assertEqual(len(bm_dict['created_at']), 26)
        self.assertEqual(len(bm_dict['updated_at']), 26)
        self.assertEqual(created_at[10], 'T')
        self.assertEqual(updated_at[10], 'T')
