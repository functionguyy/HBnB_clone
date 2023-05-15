#!/usr/bin/python3
"""User Test Module"""
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime
import json


class TestUser(unittest.TestCase):
    """
    User class Test suite
    """

    def test_attributes(self):
        """
        Test that User instance has all expected attributes
        """
        user = User()
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_attribute_id_2(self):
        """
        Test the unique ids
        """
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_attribute_id_3(self):
        """
        Test the unique ids for very large user base
        """
        ids = set()
        for i in range(1000):
            user = User()
            ids.add(user.id)
        self.assertEqual(len(ids), 1000)

    def test_attribute_unknown_1(self):
        """
        Test for fails
        """
        user = User()
        with self.assertRaises(AttributeError):
            user.unknown

    def test_attribute_updated_at_1(self):
        """
        Test the update_at attribute
        """
        user = User()
        updated_at = user.updated_at
        user.save()
        new_updated_at = user.updated_at
        self.assertNotEqual(updated_at, new_updated_at)

    def test_created_at_updated_at_attributes(self):
        """
        Test that the created_at is current time
        """
        before = datetime.now()
        user = User()
        after = datetime.now()
        self.assertTrue(before < user.created_at)
        self.assertTrue(after > user.created_at)
        self.assertTrue(before < user.updated_at)
        self.assertTrue(after > user.updated_at)

    def test_inheritance(self):
        """
        Test that User class inherits from BaseModel
        """
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_attribute_types(self):
        """
        Test that User instance attributes are of the correct type
        """
        user = User()
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_attribute_updates(self):
        """
        Test that the attributes can be updated
        """
        user = User()
        user.email = "test@example.com"
        user.first_name = "Omar"
        user.last_name = "Jammeh"
        user.password = "whydoyoucare"
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.first_name, "Omar")
        self.assertEqual(user.last_name, "Jammeh")
        self.assertEqual(user.password, "whydoyoucare")

    def test_empty_strings(self):
        """
        Test that User instance attributes are initialized to empty strings
        """
        user = User()
        self.assertEqual(user.email, '')
        self.assertEqual(user.password, '')
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')

    def test_kwargs_initialization_2(self):
        """
        Test that User instance is initialized correctly using kwargs
        """
        data = {
            'id': '1234',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-01T00:00:00',
            'email': 'test@example.com',
            'password': 'password',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        user = User(**data)
        self.assertEqual(user.id, '1234')
        self.assertEqual(user.created_at, datetime(2022, 1, 1, 0, 0))
        self.assertEqual(user.updated_at, datetime(2022, 1, 1, 0, 0))
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.password, 'password')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

    def test_to_dict(self):
        """
        Test that to_dict() method returns a
        dictionary with all keys/values of User instance
        """
        data = {
            'id': '1234',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-01T00:00:00',
            'email': 'test@example.com',
            'password': 'password',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        user = User(**data)
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['id'], '1234')
        self.assertEqual(user_dict['created_at'], '2022-01-01T00:00:00')
        self.assertEqual(user_dict['updated_at'], '2022-01-01T00:00:00')
        self.assertEqual(user_dict['email'], 'test@example.com')
        self.assertEqual(user_dict['password'], 'password')

    def test_password_saved_to_json_file(self):
        user = User()
        user.password = "password123"
        user.save()
        key = f"{user.__class__.__name__}.{user.id}"

        with open("file.json", "r") as f:
            data = json.load(f)
            user_dict = data[key]
        self.assertTrue(user_dict["password"] == "password123")

    def test_method_str(self):
        """
        Tests the string representation of the user
        """
        user = User()
        user.name = "Omar Jammeh"
        user.number = 123455
        expect = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(expect, str(user))


if __name__ == '__main__':
    unittest.main()
