#!/usr/bin/python3
"""Test ConsoleDocs"""
import pep8
import console
import inspect
from io import StringIO
from unittest.mock import patch
import unittest
HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class console"""
    def test_pep8_conformance_console(self):
        """Test PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test console"""

        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test HBNBCommand"""

        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")
class TestHBNBCommand_prompting(unittest.TestCase):
    """ Testing prompting -> HBNB command """

    def test_prompt_string(self):

        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):

        with patch("sys.stdout", new=StringIO()) as output:

            self.assertFalse(HBNBCommand().onecmd(""))

            self.assertEqual("", output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
