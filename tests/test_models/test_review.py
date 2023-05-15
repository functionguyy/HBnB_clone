#!/usr/bin/python3
"""Test Module for review class"""
import unittest
from models.review import Review
import os


class TestReview(unittest.TestCase):
    """
    Test suite for review class
    """
    def test_instance_creation(self):
        """Test that creating an instance of Review works"""
        review = Review()
        self.assertIsInstance(review, Review)
        os.remove('file.json')

    def test_text_default_value(self):
        """Test that Review.text is an empty string by default"""
        review = Review()
        self.assertEqual(review.text, "")
        os.remove('file.json')

    def test_setting_text(self):
        """Test that setting Review.text works"""
        review = Review()
        review.text = "This is a review text"
        self.assertEqual(review.text, "This is a review text")
        os.remove('file.json')

    def test_place_id_default_value(self):
        """Test that Review.place_id is an empty string by default"""
        review = Review()
        self.assertEqual(review.place_id, "")
        os.remove('file.json')

    def test_setting_place_id(self):
        """Test that setting Review.place_id works"""
        review = Review()
        review.place_id = "Place ID 123"
        self.assertEqual(review.place_id, "Place ID 123")
        os.remove('file.json')

    def test_user_id_default_value(self):
        """Test that Review.user_id is an empty string by default"""
        review = Review()
        self.assertEqual(review.user_id, "")
        os.remove('file.json')


if __name__ == "__main__":
    unittest.main()
