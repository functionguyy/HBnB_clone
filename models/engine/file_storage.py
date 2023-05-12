#!/usr/bin/python3
"""FileStorage Class is defined inside this Module"""
import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json" #JSON file to store serialized instances
    __objects = {} # store objects by <class name>.id

    def all(self):
        """returns the __objects class attribute"""
        return self.__class__.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id

        args:
            obj: object to be written to text file
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__class__.__objects[key] = obj.to_dict()

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__class__.__file_path, "w", encoding="utf-s") as f:
            json.dump(self.__class__.__objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects, only if the file pathe exist"""
        try:
            with open(self.__class__.__file_path,"r", encoding='utf-8') as f:
                self.__class__..__objects = json.load(json_string)
        except FileNotFoundError:
            pass
