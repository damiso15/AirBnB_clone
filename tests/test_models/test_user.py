#!/usr/bin/env python3
"""
A unit test for the City Model

Created on: 14th of May, 2023
Authors: Sonaike Oluwadamilola
         Joseph Ocholi
"""
import unittest
import pep8
import inspect
from models.base_model import BaseModel
from models.user import User


class TestCity(unittest.TestCase):
    """
    The user Model Test class
    """

    @classmethod
    def setUpClass(cls):
        """
        Method to set the start point of the doc test.
        """
        cls.setup = inspect.getmembers(User(), inspect.isfunction)

    def test_pep8_conformance_User(self):
        """
        Test if the User Model conform to PEP8
        """
        pep8_style = pep8.StyleGuide(quiet=True)
        check_error = pep8_style.check_files(['models/user.py'])
        self.assertEqual(check_error.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_User(self):
        """
        Test if the Unitest User Model conforms to Pep8
        """

        pep8_style = pep8.StyleGuide(quiet=True)
        check_error = pep8_style.check_files(['tests/test_models/\
                                             test_user.py'])
        self.assertEqual(check_error.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(User.__doc__) >= 0)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(User.__doc__) >= 0)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 0)

    def setUp(self):
        """
        Method to set the start point of the test. New instance of User.
        """
        self.user = User()

    def test_instance(self):
        """
        Test if the instance belongs to class User and BaseModel.
        """
        self.assertIsInstance(self.user, BaseModel)

    def test_instance_attributes(self):
        """
        Test the instance attributes.
        """
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_attr_type(self):
        """
        Test the attribute types.
        """
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.last_name), str)

    def test_attr_value(self):
        """
        Test the value of the attributes.
        """
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")


if __name__ == '__main__':
    unittest.main()
