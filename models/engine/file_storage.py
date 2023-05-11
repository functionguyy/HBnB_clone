#!/usr/bin/python3
"""File Storage Module"""
import json


class FileStorage:
    """
    Serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path =file.json
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return __objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.name}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        json_string = json.dumps(self.all())
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            f.write(json_string)

    def reload(self):
        """
        Deserializes the JSON file to __objects, only if the file pathe exist
        """
        try:
            with open(FileStorage.__file_path, encoding='utf-8') as f:
                json_string = f.read()
                FileStorage.__objects = json.loads(json_string)
        except FileNotFoundError:
            pass
