#!/usr/bin/env python3
"""
A unit test for the console

Created on: 17th of May, 2023
Authors: Sonaike Oluwadamilola
         Joseph Ocholi
"""
import unittest
import pep8
import inspect
import doctest
import console
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
    """
    The Console Test Class
    """

    @classmethod
    def setUpClass(cls):
        """
        Method to set the start point of the doc test.
        """
        cls.setup = inspect.getmembers(HBNBCommand(), inspect.isfunction)

    def test_pep8_conformance_HBNBCommand(self):
        """
        Test if the HBNBCommand conform to PEP8
        """
        pep8_style = pep8.StyleGuide(quiet=True)
        check_error = pep8_style.check_files(['console.py'])
        self.assertEqual(check_error.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_HBNBCommand(self):
        """
        Test if the Unitest HBNBCommand conforms to Pep8
        """

        pep8_style = pep8.StyleGuide(quiet=True)
        check_error = pep8_style.check_files(['tests/test_console.py'])
        self.assertEqual(check_error.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(HBNBCommand.__doc__) >= 0)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(HBNBCommand.__doc__) >= 0)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 0)

    def setUp(self):
        """
        Initialize an instance of console.HBNBCommand for tests
        """
        self.cli = HBNBCommand()

    def tearDown(self):
        """
        Cleans up after each test method has run
        """
        storage = FileStorage()
        storage.reload()
        all_objs = storage.all()
        all_objs.clear()
        storage.save()

    def test_quit(self):
        """
        Cleans up after each test method has run
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("quit")
            self.assertEqual(f.getvalue(), '')

    def test_EOF(self):
        """
        Test the method EOF
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("EOF")
            self.assertEqual(f.getvalue(), '')

    def test_create(self):
        """
        Test the method create
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create")
            self.assertEqual(f.getvalue(), '** class name missing **\n')

    def test_show(self):
        """
        Test the method show
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("show")
            self.assertEqual(f.getvalue(), '** class name missing **\n')

    def test_destroy(self):
        """
        Test the method destroy
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("destroy")
            self.assertEqual(f.getvalue(), '** class name missing **\n')

    def test_all(self):
        """
        Test the method all
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("all")
            self.assertEqual(f.getvalue(), '[]\n')

    def test_update(self):
        """
        Test the method update
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("update")
            self.assertEqual(f.getvalue(), '** class name missing **\n')

    def test_onecmd(self):
        """
        Test the onecmd
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("help show")
            output = f.getvalue()
            print("onecmd output:", output)


def load_tests(loader, tests, ignore):
    """
    Loads the doctest
    """
    tests.addTests(doctest.DocTestSuite(console))
    return tests


if __name__ == '__main__':
    unittest.main()
