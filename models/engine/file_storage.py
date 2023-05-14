#!/usr/bin/env python3
"""
A File Storage class

Created on: 9th of May, 2023
Authors: Sonaike Oluwadamilola
         Joseph Ocholi
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

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

        try:
            with open(FileStorage.__file_path, 'r') as obj:
                json_objs = json.load(obj)
                for key, value in json_objs.items():
                    class_name = value['__class__']
                    instance = self.classes[class_name](**value)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass
