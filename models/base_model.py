#!/usr/bin/python3
"""This module contains the definition of the BaseModel class"""
from datetime import datetime, timezone
import uuid
from models import *


class BaseModel(object):
    """This class defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """This method sets the initialization values of an instance"""
        key_list = list(kwargs.keys())
        if len(key_list) > 0:
            for key in key_list:
                value = kwargs[key]
                if key != "__class__":
                    if key in ['created_at', 'updated_at']:
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        "Magic method"
        return "["+str(self.__class__.__name__)+"] ("+str(self.id)+") "+str(self.__dict__)

    def save(self):
        """Updates the public attribute update_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()
