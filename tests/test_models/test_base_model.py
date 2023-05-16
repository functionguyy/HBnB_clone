#!/usr/bin/python3
"""Test Module for BaseModel Test Suite"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Base model test suite"""

    def setUp(self):
        self.bm = BaseModel()

    def test_InstanceHasIdAtrribute(self):
        """Test that a BaseModel instance has id attribute"""
        self.assertTrue(hasattr(self.bm, 'id'))

    def test_idIsUnique(self):
        """Test that a BaseModel instance has a unique ID when Created.
        The test is conducted for a large number instances
        """
        #store unique ids
        ids = set()
        #create 1000 BaseModel instances
        for i in range(1000):
            bm = BaseModel()
            ids.add(bm.id)
        self.assertEqual(len(ids), 1000)


    def test__idAtrributeIsString(self):
        """Test that the 'id' of a BaseModel is a string"""
        self.assertIsInstance(self.bm.id, str)


    def test_instanceHasCreatedAtAttribute(self):
        """Test that BaseModel instance has attribute created_at"""
        self.assertTrue(hasattr(self.bm, 'created_at'))

    def test_CreatedAtAttributeIsDatetimeObject(self):
        """Test that BaseModel instance attribute 'created_at' is a datetime object
        """
        self.assertIsInstance(self.bm.created_at, datetime)

    def test_InstanceHasUpdatedAtAttribute(self):
        """Test that BaseModel instance has attribute updated_at"""
        self.assertTrue(hasattr(self.bm, 'updated_at'), 'not present')

    def test_UpdateAtNotEqualCreatedAtAttribute(self):
        """Test that created_at and updated_at attribute values are different"""
        self.assertNotEqual(self.bm.created_at, self.bm.updated_at)

    def test_UpdatedAtAttributeIsDatetimeObject(self):
        """Test that updated_at instance attribute value is a datetime object"""
        self.assertIsInstance(self.bm.updated_at, datetime)

    def test_InstanceMethod_save(self):
        """Test that the save instance method changes the value of updated_at"""
        beforeSave = self.bm.updated_at
        self.bm.save()
        afterSave = self.bm.updated_at
        self.assertNotEqual(beforeSave, afterSave, 'updated_at not changed')

    def test_InstanceMethod_str(self):
        """Test that __str__ method returns string representation of instance"""
        self.bm.name = "Omar Jammeh"
        self.bm.number = "123545"
        className = self.bm.__class__.__name__
        instanceId = self.bm.id
        instanceAttr = self.bm.__dict__

        output = f"[{className}] ({instanceId}) {instanceAttr}"
        self.assertEqual(str(self.bm), output)

    def test_InstanceMethod_to_dict(self):
        """Test that to_dict method return dictionary of instance attribute"""
        bm_obj = self.bm.to_dict()
        bm_obj_keys = list(bm_obj)
        self.assertIsInstance(bm_obj, dict, 'Not a dictionary instance')

        # test the presence of keys
        self.assertIn('__class__', bm_obj_keys, 'No __class__ key')
        self.assertIn('created_at', bm_obj_keys, 'No created_at key')
        self.assertIn('updated_at', bm_obj_keys, 'No updated_at key')
        self.assertIn('id', bm_obj_keys, 'No id key')

        # test value of the keys
        self.assertIsInstance(bm_obj['created_at'], str, 'Not a string object')
        self.assertIsInstance(bm_obj['updated_at'], str, 'Not a string object')
        self.assertIsInstance(bm_obj['__class__'], str, 'Not a string object')
        self.assertIsInstance(bm_obj['id'], str, 'Not a string object')


if __name__ == '__main__':
    unittest.main()
