#!/usr/bin/env python3
"""
A unit test for the State Model

Created on: 14th of May, 2023
Authors: Sonaike Oluwadamilola
         Joseph Ocholi
"""
import unittest
import pep8
import inspect
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    The State Model Test class
    """

    @classmethod
    def setUpClass(cls):
        """
        Method to set the start point of the doc test.
        """
        cls.setup = inspect.getmembers(State, inspect.isfunction)

    def test_pep8_conformance_State(self):
        """
        Test if the State Model conform to PEP8
        """
        pep8_style = pep8.StyleGuide(quiet=True)
        check_error = pep8_style.check_files(['models/state.py'])
        self.assertEqual(check_error.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_State(self):
        """
        Test if the Unitest State Model conforms to Pep8
        """

        pep8_style = pep8.StyleGuide(quiet=True)
        check_error = pep8_style.check_files(['tests/test_models/\
                                             test_state.py'])
        self.assertEqual(check_error.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(State.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(State.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def setUp(self):
        """
        Initialize an instance of State for all test cases
        """
        self.state = State()

    def tearDown(self):
        """
        Reset the instance of State for all test cases
        """
        del self.state

    def test_instance(self):
        """
        Test if the instance is of type State
        """
        self.assertIsInstance(self.state, State)

    def test_inherits(self):
        """
        Test if State inherits from BaseModel
        """
        self.assertIsInstance(self.state, BaseModel)

    def test_attribute_types(self):
        """
        Test attribute types
        """
        self.assertEqual(type(self.state.name), str)

    def test_init_default_args(self):
        """
        Test default value of name attribute
        """
        self.assertEqual(self.state.name, "")


if __name__ == '__main__':
    unittest.main()
