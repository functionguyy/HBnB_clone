#!/usr/bin/python3
"""Test Module for state class test suite"""
import unittest
from models.state import State
import os


class TestState(unittest.TestCase):
    """
    Test suite for state class
    """
    def test_create_state(self):
        """
        Test that instance created
        """
        new_state = State()
        self.assertIsInstance(new_state, State)
        os.remove('file.json')

    def test_state_attributes(self):
        """
        Test instance attributes
        """
        new_state = State()
        self.assertTrue(hasattr(new_state, "name"))
        self.assertEqual(new_state.name, "")
        os.remove('file.json')

    def test_state_str_method(self):
        """
        Test instance representation
        """
        new_state = State()
        self.assertEqual(
            str(new_state),
            "[State] ({}) {}".format(new_state.id, new_state.__dict__))
        os.remove('file.json')


if __name__ == "__main__":
    unittest.main()
