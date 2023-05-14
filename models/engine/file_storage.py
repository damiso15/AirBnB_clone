#!/usr/bin/env python3
"""
A File Storage class

Created on: 9th of May, 2023
Authors: Sonaike Oluwadamilola
         Joseph Ocholi
"""
import json
from importlib import import_module


class FileStorage:
    """
    A File storage class that serializes instances to a JSON file
    and deserializes JSON file to instances

    Attributes:
        file_path (str): path to the JSON file
        objects (dict): empty but will store all objects by <class name>.id
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary __objects

        Returns:
            The dictionary __objects
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        This method sets the object with key <obj class name>.id
        """

        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        This method serializes __objects to the JSON file
        """

        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump({key: value.to_dict() for key, value in
                       FileStorage.__objects.items()}, json_file)

    def reload(self):
        """
        This method deserializes the JSON file to __objects
        """

        BaseModel = import_module('models.base_model').BaseModel
        try:
            with open(FileStorage.__file_path, 'r') as obj:
                FileStorage.__objects = {key: BaseModel(**value) for key,
                                         value in json.load(obj).items()}
        except FileNotFoundError:
            pass
