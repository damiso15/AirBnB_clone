#!/usr/bin/env python3
"""
A unit test for the Place Model

Created on: 14th of May, 2023
Authors: Sonaike Oluwadamilola
         Joseph Ocholi
"""
import unittest
import pep8
import inspect
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """
    The Place Model Test class
    """

    @classmethod
    def setUpClass(cls):
        """
        Method to set the start point of the doc test.
        """
        cls.setup = inspect.getmembers(Place(), inspect.isfunction)

    def test_pep8_conformance_Place(self):
        """
        Test if the Place Model conform to PEP8
        """
        pep8_style = pep8.StyleGuide(quiet=True)
        check_error = pep8_style.check_files(['models/place.py'])
        self.assertEqual(check_error.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_Place(self):
        """
        Test if the Unitest Place Model conforms to Pep8
        """

        pep8_style = pep8.StyleGuide(quiet=True)
        check_error = pep8_style.check_files(['tests/test_models/\
                                             test_place.py'])
        self.assertEqual(check_error.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Place.__doc__) >= 0)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Place.__doc__) >= 0)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 0)

    def setUp(self):
        """
        Create a new instance of Place before each test
        """
        self.place = Place()

    def tearDown(self):
        """
        Delete Place instance
        """
        del self.place

    def test_ID_exists(self):
        """
        Make sure that the ID has been generated and is not None
        """
        self.assertIsNotNone(self.place.id)

    def test_id_is_a_string(self):
        """
        Make sure that the type of id is a string
        """
        self.assertEqual(type(self.place.id), str)

    def test_created_at_exists(self):
        """
        Make sure that created_at has been generated and is not None
        """
        self.assertIsNotNone(self.place.created_at)

    def test_created_at_is_datetime_object(self):
        """
        Make sure that the type of created_at is a datetime object
        """
        self.assertEqual(type(self.place.created_at), datetime)

    def test_updated_at_exists(self):
        """
        Make sure that updated_at has been generated and is not None
        """
        self.assertIsNotNone(self.place.updated_at)

    def test_updated_at_is_datetime_object(self):
        """
        Make sure that the type of updated_at is a datetime object
        """
        self.assertEqual(type(self.place.updated_at), datetime)

    def test_class_attributes(self):
        """
        Make sure class attributes are present and correctly set
        """
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertEqual(self.place.city_id, "")
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertEqual(self.place.user_id, "")
        self.assertTrue(hasattr(self.place, "name"))
        self.assertEqual(self.place.name, "")
        self.assertTrue(hasattr(self.place, "description"))
        self.assertEqual(self.place.description, "")
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertEqual(self.place.number_rooms, 0)
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertEqual(self.place.max_guest, 0)
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertEqual(self.place.price_by_night, 0)
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertEqual(self.place.latitude, 0.0)
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertEqual(self.place.longitude, 0.0)
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertEqual(self.place.amenity_ids, [])

    def test_str(self):
        """
        Testing return of str
        """
        self.assertEqual(str(self.place), "[Place] ({}) {}".
                         format(self.place.id, self.place.__dict__))

    def test_save(self):
        """
        Testing the save method
        """
        old_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(old_updated_at, self.place.updated_at)

    def test_to_dict(self):
        """
        Testing the to_dict method
        """
        place_dict = self.place.to_dict()
        self.assertEqual(type(place_dict), dict)
        for attr in self.place.__dict__:
            if "__class__" != attr:
                self.assertTrue(attr in place_dict)


if __name__ == '__main__':
    unittest.main()
