#!/usr/bin/python3
"""Review Module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Subclass of the BaseModel class
    Public class attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string -empty string: it will be User.id
        text = string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
