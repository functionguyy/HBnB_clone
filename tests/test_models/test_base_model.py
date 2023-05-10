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

    def test_created_at_assigned_at_current_time(self):
        """
            Test that created_at is assigned the current datetime
            when an instance is created
        """
        bm1 = BaseModel()
        created_at = bm1.created_at
        current_time = datetime.now
        self.assertEqual(created_at, current_time)

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
