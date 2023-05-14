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
from models.city import City


class TestCity(unittest.TestCase):
    """
    The City Model Test class
    """

    @classmethod
    def setUpClass(cls):
        """
        Method to set the start point of the doc test.
        """
        cls.setup = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_conformance_City(self):
        """
        Test if the City Model conform to PEP8
        """
        pep8_style = pep8.StyleGuide(quiet=True)
        check_error = pep8_style.check_files(['models/city.py'])
        self.assertEqual(check_error.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_City(self):
        """
        Test if the Unitest City Model conforms to Pep8
        """

        pep8_style = pep8.StyleGuide(quiet=True)
        check_error = pep8_style.check_files(['tests/test_models/\
                                             test_city.py'])
        self.assertEqual(check_error.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(City.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(City.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def setUp(self):
        """
        Initialize an instance of models.city.City for tests
        """
        self.test_city = City()

    def tearDown(self):
        """
        Cleans up after each test method has run.
        """
        del self.test_city

    def test_is_instance_base_model(self):
        """
        Test if test_city is an instance of BaseModel
        """
        self.assertIsInstance(self.test_city, BaseModel)

    def test_if_name_exists(self):
        """
        Test if the attribute 'name' is present in the instance
        """
        self.assertTrue(hasattr(self.test_city, 'name'))
        self.assertEqual(self.test_city.name, "")

    def test_if_state_id_exists(self):
        """
        Test if the attribute 'state_id' is present in the instance
        """
        self.assertTrue(hasattr(self.test_city, 'state_id'))
        self.assertEqual(self.test_city.state_id, "")

    def test_to_dict(self):
        """
        Test the to_dict method
        """
        city_dict = self.test_city.to_dict()
        self.assertEqual(self.test_city.__class__.__name__, 'City')
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)
        self.assertEqual(city_dict['__class__'], 'City')


if __name__ == '__main__':
    unittest.main()
