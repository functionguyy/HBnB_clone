#!/usr/bin/python3
"""This module contains the definition for City class"""
from base_model import BaseModel


class City(BaseModel):
    """Subclass of BaseModel class


    Args:
        state_id: The id of the state
        name: string
    """
    state_id = ""
    name = ""
