#!/usr/bin/env python3
"""
A unitest for the Base Model

Created on: 8th of May, 2023
Authors: Sonaike Oluwadamilola
         Joseph Ocholi
"""
import unittest
import pep8
import inspect
import os
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    A File storage class that serializes instances to a JSON file
    and deserializes JSON file to instances Test class
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the the doc test
        """

        cls.setup = inspect.getmembers(FileStorage(), inspect.isfunction)

    def setUp(self):
        """
        This mnethod set the start point of the test cases
        """

        self.file_path = FileStorage._FileStorage__file_path
        self.storage = FileStorage()
        FileStorage._FileStorage__objects.clear()

    def test_pep8_conformance_FileStorage(self):
        """
        Test if the File Storage conforms to Pep8
        """

        pep8_style = pep8.StyleGuide(quiet=True)
        check_error = pep8_style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(check_error.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_FileStorage(self):
        """
        Test if the test File Storage file conforms to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_engine/\
                                        test_file_storage.py'])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_class_docstring(self):
        """
        Test if the docstring documentation for the class exist
        """

        self.assertTrue(len(FileStorage.__doc__) >= 0)

    def test_function_docstring(self):
        """
        Test if the docstring documentation for the functions exist
        """

        for value in self.setup:
            self.assertTrue(len(value[1].__doc__) >= 0)

    def test_module_docstring(self):
        """
        Test if the docstring documentation for the module exist
        """

        self.assertTrue(len(BaseModel.__doc__) >= 0)

    def tearDown(self):
        """
        This method reset every tests
        """

        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tear_all(self):
        """
        This method tests the all method and returns all objects
        """

        base = BaseModel()
        self.storage.new(base)
        self.storage.save()
        objects = self.storage.all()
        key = "{}.{}".format(type(base).__name__, base.id)
        self.assertTrue(key in self.storage.all())

    def test_new(self):
        """
        This method tests the new method adds an object to the
        __objects dictionary
        """

        base = BaseModel()
        self.storage.new(base)
        key = "{}.{}".format(type(base).__name__, base.id)
        self.assertTrue(key in self.storage.all())

    def test_save(self):
        """
        This method tests the save method serializes objects to the JSON file
        """
        base = BaseModel()
        self.storage.new(base)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, 'r') as f:
            self.assertTrue(len(f.read()) > 0)

    def test_reload(self):
        """
        This method tests the reload method deserializes objects from the
        JSON file
        """

        base = BaseModel()
        self.storage.new(base)
        self.storage.save()
        FileStorage._FileStorage__objects = {}
        self.storage.reload()
        objects = self.storage.all()
        key = "{}.{}".format(type(base).__name__, base.id)
        self.assertTrue(key in objects)

    def test_objects_empty(self):
        """
        This method tests if the object is an empty string
        """

        self.assertEqual(len(FileStorage.all(FileStorage)), 0)


if __name__ == "__main__":
    unittest.main()
