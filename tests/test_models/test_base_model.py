#!/usr/binpython3
"""
A unitest for the Base Model

Created on: 8th of May, 2023
Authors: Sonaike Oluwadamilola
         Joseph Ocholi
"""
import unittest
import pep8
import inspect
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    The Base Model Test class
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the the doc test
        """

        cls.setup = inspect.getmembers(BaseModel, inspect.isfunction)

    def setUp(self):
        """
        Set up the test
        """

        self.model = BaseModel()

    def test_pep8_conformance_BaseModel(self):
        """
        Test if the Base Model conforms to Pep8
        """

        pep8_style = pep8.StyleGuide(quiet=True)
        check_error = pep8_style.check_files(['models/base_model.py'])
        self.assertEqual(check_error.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_BaseModel(self):
        """
        Test if the Unitest Base Model conforms to Pep8
        """

        pep8_style = pep8.StyleGuide(quiet=True)
        check_error = pep8_style.check_files(['tests/test_models/\
                                             test_base_model.py'])
        self.assertEqual(check_error.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_class_docstring(self):
        """
        Test if the docstring documentation for the class exist
        """

        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_function_docstring(self):
        """
        Test if the docstring documentation for the functions exist
        """

        for value in self.setup:
            self.assertTrue(len(value[1].__doc__) >= 1)

    def test_module_docstring(self):
        """
        Test if the docstring documentation for the module exist
        """

        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_instance(self):
        """
        Test if the created object is an instance of BaseModel.
        """

        self.assertIsInstance(self.model, BaseModel)

    def test_id_type(self):
        """
        Test if the id attribute is of type string.
        """

        self.assertIsInstance(self.model.id, str)

    def test_created_at_type(self):
        """
        Test if the created_at attribute is of type datetime.
        """

        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_type(self):
        """
        Test if the updated_at attribute is of type datetime.
        """

        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save(self):
        """
        Test if the updated_at attribute is updated after calling save().
        """

        initial_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(initial_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """
        Test if to_dict() returns a dictionary with the correct keys
        and values.
        """

        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["created_at"],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"],
                         self.model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
