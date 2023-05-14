#!/usr/bin/python3
"""This module contains definition for Review class"""
from base_model import BaseModel


class Review(BaseModel):
    """Subclass of the BaseModel class


    Attributes:
        place_id (str): it will be the Place.id
        user_id (str): it will be User.id
        text (str): empty string
    """
    place_id = ""
    user_id = ""
    text = ""
