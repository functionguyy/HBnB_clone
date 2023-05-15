#!/usr/bin/python3
"""This module contains the definition for the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Subclass of BaseModel class

    Args:
        name: string - empty string
    """
    name = ""
