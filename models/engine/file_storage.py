#!/usr/bin/python3
"""File Storage Module for serialization and deserialization from the JSON"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects, only if the file pathe exist
        """
        try:
            with open(self.__file_path, encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, obj in obj_dict.items():
                    class_name, id = key.split('.')
                    self.__objects[key] = eval(class_name)(**obj)
        except FileNotFoundError:
            pass

    def destroy(self, key):
        """
        Deletes an object from objects
        """
        if key in self.__objects:
            self.__objects.pop(key)
            self.save()
        else:
            print("** no instance found **")

    def update(self, key, attr, value):
        """
        Uses the key to add or update attr value
        """
        if key not in self.__objects:
            print("** no instance found **")
            return
        if hasattr(self.__objects[key], attr):
            current_value = getattr(self.__objects[key], attr)
            if type(current_value) == int:
                value = int(value)
            elif type(current_value) == float:
                value = float(value)
        if attr in ['age', 'height']:
            value = int(value)
        setattr(self.__objects[key], attr, value)
        self.save()

    def ids(self):
        """
        Returns a dictionary of class names and ids
        """
        object_ids = []
        objects = self.__objects
        for key, obj in objects.items():
            object_ids.append(obj.to_dict()['id'])
        return object_ids

    def classes(self):
        """
        Return a list of class names created
        """
        objects_classes = []
        objects = self.__objects
        for key, obj in objects.items():
            object_classes.append(obj.to_dict()['__class__'])
        return objects_classes
