#!/usr/bin/python3
"""This module contains the definition of the BaseModel class"""
from datetime import datetime, timezone
import uuid

class BaseModel(object):
    """This class defines all common attributes/methods for other classes"""

    def __init__(self):
        """This method sets the initialization values of an instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        "Magic method"
        return "["+str(self.__class__.__name__)+"] ("+str(self.id)+") "+str(self.__dict__)

    def save(self):
        """Updates the public attribute update_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Create a dictionary representation with simple object type of
        BaseModel

        """
        bm_obj = {}
        keys = self.__dict__.copy()
        for key in keys:
            if key == "updated_at":
                bm_obj[key] = self.__dict__[key].isoformat()
            elif key == "created_at":
                bm_obj[key] = self.__dict__[key].isoformat()
            else:
                bm_obj[key] = self.__dict__[key]

        bm_obj["__class__"] = self.__class__.__name__

        return bm_obj
