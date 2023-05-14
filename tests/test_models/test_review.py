#!/usr/bin/env python3
"""
A unit test for the Review Model

Created on: 14th of May, 2023
Authors: Sonaike Oluwadamilola
         Joseph Ocholi
"""
import unittest
import pep8
import inspect
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """
    The Review Model Test class
    """

    @classmethod
    def setUpClass(cls):
        """
        Method to set the start point of the doc test.
        """
        cls.setup = inspect.getmembers(Review, inspect.isfunction)

    def test_pep8_conformance_Review(self):
        """
        Test if the Review Model conform to PEP8
        """
        pep8_style = pep8.StyleGuide(quiet=True)
        check_error = pep8_style.check_files(['models/review.py'])
        self.assertEqual(check_error.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_Review(self):
        """
        Test if the Unitest Review Model conforms to Pep8
        """

        pep8_style = pep8.StyleGuide(quiet=True)
        check_error = pep8_style.check_files(['tests/test_models/\
                                             test_review.py'])
        self.assertEqual(check_error.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Review.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Review.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def setUp(self):
        """
        Create a new instance of Review before each test
        """
        self.review = Review()

    def tearDown(self):
        """
        Delete Review instance
        """
        del self.review

    def test_ID_exists(self):
        """
        Make sure that the ID has been generated and is not None
        """
        self.assertIsNotNone(self.review.id)

    def test_id_is_a_string(self):
        """
        Make sure that the type of id is a string
        """
        self.assertEqual(type(self.review.id), str)

    def test_created_at_exists(self):
        """
        Make sure that created_at has been generated and is not None
        """
        self.assertIsNotNone(self.review.created_at)

    def test_created_at_is_datetime_object(self):
        """
        Make sure that the type of created_at is a datetime object
        """
        self.assertEqual(type(self.review.created_at), datetime)

    def test_updated_at_exists(self):
        """
        Make sure that updated_at has been generated and is not None
        """
        self.assertIsNotNone(self.review.updated_at)

    def test_updated_at_is_datetime_object(self):
        """
        Make sure that the type of updated_at is a datetime object
        """
        self.assertEqual(type(self.review.updated_at), datetime)

    def test_class_attributes(self):
        """
        Make sure class attributes are present and correctly set
        """
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertEqual(self.review.place_id, "")
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertEqual(self.review.user_id, "")
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.text, "")

    def test_str(self):
        """
        Testing return of str
        """
        self.assertEqual(str(self.review), "[Review] ({}) {}".format(self.review.id, self.review.__dict__))

    def test_save(self):
        """
        Testing the save method
        """
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(old_updated_at, self.review.updated_at)

    def test_to_dict(self):
        """
        Testing the to_dict method
        """
        review_dict = self.review.to_dict()
        self.assertEqual(type(review_dict), dict)
        for attr in self.review.__dict__:
            if "__class__" != attr:
                self.assertTrue(attr in review_dict)


if __name__ == '__main__':
    unittest.main()
