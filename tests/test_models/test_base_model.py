#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Base model test suite"""

    test_instance_id(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    test_created_at_assigned_at_current_time(self):
        bm1 = BaseModel()
        created_at = bm1.created_at
        current_time = datetime.now
        self.assertEqual(created_at, current_time)

    test_to_dict_returns_all_attr_values(self):
        bm1 = BaseModel()
        bm1.id = "123"
        bm1.created_at = "2022-05-09T14:30:00.000000"
        bm1.updated_at = "2022-05-09T14:30:00.000000"
        bm1.name = "example"
        bm1.number = 42

        bm_dict = bm1.to_dict()

        assertEqual(bm_dict['id'], "123")
        assertEqual(bm_dict['created_at'], "2022-05-09T14:30:00.000000")
        assertEqual(bm_dict['updated'], "2022-05-09T14:30:00.000000")
        assertEqual(bm_dict['name'], "example")
        assertEqual(bm_dict['number'], 42)

    test_to_dict_contains_class_key(self):
        bm = BaseModel()

        bm_dict = bm.to_dict()

        self.assertTrue("__class__" in bm_dict)
        self.assertEqual(bm_dict['__class__'], 'BaseModel')

    test_to_dict_iso_format(self):
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
