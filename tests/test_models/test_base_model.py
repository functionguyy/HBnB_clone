#!/usr/bin/python3
"""Test Module for BaseModel Test Suite"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Base model test suite"""

    def test_attribute_id_1(self):
        """
        Test that class has attribute 'id'
        """
        bm = BaseModel()
        self.assertTrue(hasattr(bm, 'id'))

    def test_attribute_id_2(self):
        """
            Test that a BaseModel instance has a unique ID when Created
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_attribute_id_3(self):
        """
        Test that attr 'id' is a string
        """
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)

    def test_attribute_id_4(self):
        """
        Test for the unique ids of a large number of ids
        """
        ids = set()
        for i in range(1000):
            bm = BaseModel()
            ids.add(bm.id)
        self.assertEqual(len(ids), 1000)

    def test_attribute_created_at_1(self):
        """
        Test that has attribute 'created_at'
        """
        bm = BaseModel()
        self.assertTrue(hasattr(bm, 'created_at'))

    def test_attribute_created_at_2(self):
        """
        Test that attr 'created_at' is a datetime object
        """
        bm = BaseModel()
        self.assertTrue(isinstance(bm.created_at, datetime))

    def test_attribute_created_at_3(self):
        """
        Test that attr 'created_at' is current time
        """
        before_current = datetime.now()
        bm = BaseModel()
        after_current = datetime.now()
        self.assertTrue(before_current <= bm.created_at)
        self.assertTrue(after_current >= bm.created_at)

    def test_attribute_updated_at_1(self):
        """
        Test that class has attr 'updated_at'
        """
        bm = BaseModel()
        self.assertTrue(hasattr(bm, 'updated_at'))

    def test_attribute_updated_at_2(self):
        """
        Test that created_at and updated_at attrs are equal
        """
        bm = BaseModel()
        self.assertNotEqual(bm.created_at, bm.updated_at)

    def test_attribute_updated_at_3(self):
        """
        Test that updated_at is a string
        """
        bm = BaseModel()
        self.assertIsInstance(bm.updated_at, datetime)

    def test_attribute_updated_at_4(self):
        """
        Test that upated_at attr is current time
        """
        before_current = datetime.now()
        bm = BaseModel()
        after_current = datetime.now()
        self.assertTrue(before_current < bm.updated_at)
        self.assertTrue(after_current > bm.updated_at)

    def test_attribute_updated_at_5(self):
        """
        Test that the updated_at is change after a save
        """
        bm = BaseModel()
        first_updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(first_updated_at, bm.updated_at)

    def test_string_method(self):
        """
        Test that the str is producing the right output
        """
        bm = BaseModel()

        bm.name = "Omar Jammeh"
        bm.number = "123545"

        expected_output = "[BaseModel] ({}) {}".format(bm.id, bm.__dict__)
        self.assertEqual(str(bm), expected_output)

    def test_method_to_dict_1(self):
        """
        Test that to_dict method returns a dictionary object
        """
        bm = BaseModel()
        self.assertTrue(isinstance(bm.to_dict(), dict))

    def test_method_to_dict_2(self):
        """
        Test that to_dict method returns a dict object
        containing '__class__' key and value
        """
        bm = BaseModel()
        self.assertTrue(hasattr(bm, '__class__'))

    def test_method_to_dict_3(self):
        """
            Test that to_dict method returns a dictionary containing
            all keys values of dict of the instance
        """
        bm1 = BaseModel()
        bm1.id = "123"
        bm1.created_at = datetime.fromisoformat("2022-05-09T14:30:00.123456")
        bm1.updated_at = datetime.fromisoformat("2022-05-09T14:30:00.123456")
        bm1.name = "example"
        bm1.number = 42

        bm_dict = bm1.to_dict()

        self.assertEqual(bm_dict['id'], "123")
        self.assertEqual(bm_dict['created_at'], "2022-05-09T14:30:00.123456")
        self.assertEqual(bm_dict['updated_at'], "2022-05-09T14:30:00.123456")
        self.assertEqual(bm_dict['name'], "example")
        self.assertEqual(bm_dict['number'], 42)

    def test_method_to_dict_4(self):
        """
        Test for unknown attrs
        """
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertTrue('unknown' not in bm_dict)

    def test_method_to_dict_5(self):
        """
            Test that the value of '__class__' in the
            return dict is 'BaseModel'
        """
        bm = BaseModel()

        bm_dict = bm.to_dict()
        self.assertEqual(bm_dict['__class__'], 'BaseModel')

    def test_method_to_dict_6(self):
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


if __name__ == '__main__':
    unittest.main()
