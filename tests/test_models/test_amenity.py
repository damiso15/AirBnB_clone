#!/usr/bin/env python3
"""
A unit test for the Amenity Model

Created on: 14th of May, 2023
Authors: Sonaike Oluwadamilola
         Joseph Ocholi
"""
import unittest
import pep8
import inspect
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """
    The Amenity Model Test class
    """

    @classmethod
    def setUpClass(cls):
        """
        Method to set the start point of the doc test.
        """
        cls.setup = inspect.getmembers(Amenity(), inspect.isfunction)

    def test_pep8_conformance_Amenity(self):
        """
        Test if the Amenity Model conform to PEP8
        """
        pep8_style = pep8.StyleGuide(quiet=True)
        check_error = pep8_style.check_files(['models/amenity.py'])
        self.assertEqual(check_error.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_Amenity(self):
        """
        Test if the Unitest Amenity Model conforms to Pep8
        """

        pep8_style = pep8.StyleGuide(quiet=True)
        check_error = pep8_style.check_files(['tests/test_models/\
                                             test_amenity.py'])
        self.assertEqual(check_error.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Amenity.__doc__) >= 0)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Amenity.__doc__) >= 0)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 0)

    def setUp(self):
        """
        Create a new instance of Amenity before each test
        """
        self.amenity = Amenity()

    def tearDown(self):
        """
        Delete Amenity instance
        """
        del self.amenity

    def test_ID_exists(self):
        """
        Make sure that the ID has been generated and is not None
        """
        self.assertIsNotNone(self.amenity.id)

    def test_id_is_a_string(self):
        """
        Make sure that the type of id is a string
        """
        self.assertEqual(type(self.amenity.id), str)

    def test_created_at_exists(self):
        """
        Make sure that created_at has been generated and is not None
        """
        self.assertIsNotNone(self.amenity.created_at)

    def test_created_at_is_datetime_object(self):
        """
        Make sure that the type of created_at is a datetime object
        """
        self.assertEqual(type(self.amenity.created_at), datetime)

    def test_updated_at_exists(self):
        """
        Make sure that updated_at has been generated and is not None
        """
        self.assertIsNotNone(self.amenity.updated_at)

    def test_updated_at_is_datetime_object(self):
        """
        Make sure that the type of updated_at is a datetime object
        """
        self.assertEqual(type(self.amenity.updated_at), datetime)

    def test_name_exists(self):
        """
        Make sure that name exists and is an empty string
        """
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

    def test_str(self):
        """
        Testing return of str
        """
        self.assertEqual(str(self.amenity), "[Amenity] ({}) {}"
                         .format(self.amenity.id, self.amenity.__dict__))

    def test_save(self):
        """
        Testing the save method
        """
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)

    def test_to_dict(self):
        """
        Testing the to_dict method
        """
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(type(amenity_dict), dict)
        for attr in self.amenity.__dict__:
            if "__class__" != attr:
                self.assertTrue(attr in amenity_dict)
        self.assertTrue("__class__" in amenity_dict)


if __name__ == "__main__":
    unittest.main()
