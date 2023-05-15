#!/usr/bin/python3
"""This module contains the definition of the BaseModel class"""
from datetime import datetime, timezone
import uuid


class BaseModel(object):
    """This class defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """This method sets the initialization values of an instance"""
        from models import storage
        key_list = list(kwargs.keys())
        if len(key_list) > 0:
            for key in key_list:
                value = kwargs[key]
                if key != "__class__":
                    if key in ['created_at', 'updated_at']:
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            setattr(self, 'id', str(uuid.uuid4()))
            setattr(self, 'created_at', datetime.now())
            setattr(self, 'updated_at', datetime.now())
            storage.new(self)

    def __str__(self):
        """The magic method returns the string representation of an instance.

        This method defines the value that will be returned when an instance
        name is passed as an argument to the print(). 
        """
        class_name = self.__class__.__name__
        obj_id = self.id
        obj_dict = self.__dict__
        return "[{}] ({}) {}".format(class_name, obj_id, obj_dict)

    def save(self):
        """Updates the public attribute update_at with the current datetime"""
        from models import storage
        setattr(self, 'updated_at', datetime.now())
        storage.save()

    def to_dict(self):
        """Create a dictionary representation with simple object type of
        BaseModel
        """
        bm_obj = {}
        bm_obj = self.__dict__.copy()
        bm_obj['created_at'] = getattr(self, 'created_at').isoformat()
        bm_obj['updated_at'] = getattr(self, 'updated_at').isoformat()
        bm_obj["__class__"] = self.__class__.__name__
        return bm_obj
