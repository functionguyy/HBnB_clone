#!/usr/bin/python3
"""File Storage Module"""
import json


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
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        json_string = json.dumps(FileStorage.__objects)
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
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

    def destroy(self, key):
        """
        Deletes an object from objects
        """
        FileStorage.__objects.pop(key)
        self.save()

    def update(self, key, attr, value):
        """
        Uses the key to add or update attr value
        """
        FileStorage.__objects[key][attr] = value
        self.save()

    def ids(self):
        """
        Returns a dictionary of class names and ids
        """
        object_ids = []
        objects = FileStorage.__objects
        for obj, value in objects.items():
            object_ids.append(value['id'])
        return object_ids
