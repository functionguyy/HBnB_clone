#!/usr/bin/python3
"""Test Module for the file_storage class"""
import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test suite for file_storage_class"""
    def setUp(self):
        """
        Create an instance of the FileStorage class
        """
        self.file_path = "file.json"
        self.file_storage = FileStorage()
        self.base_model = BaseModel()
        self.user = User()
        self.place = Place()
        self.state = State()
        self.city = City()
        self.amenity = Amenity()
        self.review = Review()
        self.file_storage.new(self.base_model)
        self.file_storage.new(self.user)
        self.file_storage.new(self.place)
        self.file_storage.new(self.state)
        self.file_storage.new(self.city)
        self.file_storage.new(self.amenity)
        self.file_storage.new(self.review)
        self.file_storage.save()

    def tearDown(self):
        """
        Deletes the JSON file if created
        """
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """
        Test that all method returns a dictionary
        """
        objects = self.file_storage.all()
        self.assertTrue(type(objects), dict)

    def test_new(self):
        """
        Test that new method sets an instance in __objects
        """
        before_count = len(self.file_storage.all())
        obj = BaseModel()
        self.file_storage.new(obj)
        self.file_storage.save()
        after_count = len(self.file_storage.all())
        self.assertTrue(after_count - before_count, 1)

    def test_save(self):
        """
        Test that objects are saved and reloaded correctly
        """
        self.file_storage.save()
        with open(self.file_path, 'r') as f:
            data = f.read()
        self.assertNotEqual(data, '')

    def test_reload(self):
        """
        Test that objects are saved and reloaded correctly
        """
        obj_id = self.user.id
        obj_path = self.file_path
        del self.file_storage
        new_file_storage = FileStorage()
        new_file_storage.reload()
        objects = new_file_storage.all()
        self.assertTrue(obj_id in objects.keys())

    def test_destroy(self):
        """
        Test that destroy method deletes an object from __objects
        """
        before_count = len(self.file_storage.all())
        self.file_storage.destroy(f"BaseModel.{self.base_model.id}")
        self.file_storage.save()
        after_count = len(self.file_storage.all())
        self.assertTrue(before_count - after_count, 1)

    def test_update(self):
        """
        Test that update method updates an object's attribute
        """
        obj_id = self.user.id
        obj_attr = "first_name"
        obj_value = "Bobby"
        self.file_storage.update(f"User.{obj_id}", obj_attr, obj_value)
        self.file_storage.save()
        objects = self.file_storage.all()
        self.assertTrue(objects[f"User.{obj_id}"].first_name, obj_value)

    def test_ids(self):
        """
        Test that ids method returns a list of object ids
        """
        ids = self.file_storage.ids()
        self.assertTrue(len(ids), 7)

    def test_classes(self):
        """
        Test that classes method returns a list of object classes
        """
        classes = self.file_storage.classes()
        self.assertTrue(len(classes), 7)


if __name__ == '__main__':
    unittest.main()
