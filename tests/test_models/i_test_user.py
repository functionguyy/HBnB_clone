#!/usr/bin/python3
"""User Test Module"""
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):
    """
    User class Test suite
    """

    def test_is_child_of_base_model(self):
        """
        test that User is a subclass of BaseModel
        """
        self.assertTrue(issubclass(User, BaseModel))

    def test_email_attr(self):
        """
        test to see the email is initailly empty
        """
        user = User()
        email = user.email
        self.assertEqual(len(email), 0)

    def test_password_attr(self):
        """
        tests too see that the password is an empty string
        """
        user = User()
        password = user.password
        self.assertTrue(isinstance(password, str))
        self.assertEqual(len(password), 0)

    def test_first_name_attr(self):
        """
        Test too see that the first_name is an empty string
        """
        user = User()
        first_name = user.first_name
        self.assertTrue(isinstance(first_name, str))
        self.assertEqual(len(first_name), 0)

    def test_last_name_attr(self):
        """
        Test to see that the last_name is an empty string
        """
        user = User()
        last_name = user.last_name
        self.assertTrue(isinstance(last_name, str))
        self.assertEqual(len(last_name))

    def test_unknown_attr(self):
        """
        Test for fails
        """
        user = User()
        with self.assertRaises(AttributeError):
            user.unknown
    def test_id_attr(self):
        """
        Test for the id attribute of the instance
        """
        user = User()
        user_id = user.id
        self.assertIsInstance(user_id, str)

    def test_created_at(self):
        """
        Test the created_at attribute of super class
        """
        user = User()
        current_time = datetime.now()
        created_at = user.created_at
        self.assertEqual(created_at, current_time)

    def test_updated_at(self):
        """
        Test the update_at attribute
        """
        user = User()
        updated_at = user.updated_at
        user.save()
        new_updated_at = user.updated_at
        self.assertNotEqual(updated_at, new_updated_at)

    def test_update_at_and_created_at(self):
        """
        Test that update_at and created_at are equal at initially
        """
        user = User()
        created_at = user.created_at
        updated_at = user.updated_at
        self.assertEqual(created_at, updated_at)

    def test_user_ids(self):
        """
        Test the unique ids
        """
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_user_crowded_ids(self):
        """
        Test the unique ids for very large user base
        """
        ids = set()
        for i in range(1000):
            user = User()
            ids.add(user.id)
        self.assertEqual(len(ids), 1000)

    def test_user_id_is_string(self):
        """
        Test that id is string
        """
        user = User()
        self.assertIsInstance(user.id, str)

    def test_user_string_method(self):
        """
        Tests the string representation of the user
        """
        user = User()
        user.name = "Omar Jammeh"
        user.number = 123455
        expect = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(expect, str(user))

    def test_user_save_method(self):
        """
        Test for unique updated_at of large amount
        """
        updateds = set()
        for i in range(1000):
            user = User()
            updateds.add(user.updated_at)
        self.assertEqual(len(updateds), 1000)
