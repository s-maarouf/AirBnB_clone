#!/usr/bin/python3
"""Test for console"""
import unittest
import pep8
import os
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage



class TestConsole(unittest.TestCase):
    """Test for console"""

    def test_pep8_console(self):
        """test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_docstrings_in_console(self):
        """test docstrings"""
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)

    def test_create(self):
        """test create"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State name=\"California\"")
            state_id = f.getvalue()
            self.assertTrue(len(state_id) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City state_id=\"{}\" name=\"San_Francisco\"".format(state_id[:-1]))
            city_id = f.getvalue()
            self.assertTrue(len(city_id) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User email=\"

    def test_show(self):
        """test show"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State name=\"California\"")
            state_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City state_id=\"{}\" name=\"San_Francisco\"".format(state_id[:-1]))
            city_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User email=\"

    def test_destroy(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State name=\"California\"")
            state_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City state_id=\"{}\" name=\"San_Francisco\"".format(state_id[:-1]))
            city_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User email=\"

    def test_all(self):
        """test all"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State name=\"California\"")
            state_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City state_id=\"{}\" name=\"San_Francisco\"".format(state_id[:-1]))
            city_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User email=\"

    def test_update(self):
        """test update"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State name=\"California\"")
            state_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City state_id=\"{}\" name=\"San_Francisco\"".format(state_id[:-1]))
            city_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User email=\"

    def test_quit(self):
        """test quit"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        """test EOF"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_emptyline(self):
        """test emptyline"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))

    def test_help(self):
        """test help"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help"))

    def test_count(self):
        """test count"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count"))

    def test_destroy(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy"))

    def test_update(self):
        """test update"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update"))

    def test_show(self):
        """test show"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show"))

    def test_create(self):
        """test create"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))

    def test_all(self):
        """test all"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all"))

    def test_create(self):
        """test create"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))

    def test_create(self):
        """test create"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))

    def test_create(self):
        """test create"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))

    def test_create(self):
        """test create"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))

    def test_create(self):
        """test create"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))

    def test_create(self):
        """test create"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))

    def test_create(self):
        """test create"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))

    def test_create(self):
        """test create"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))

if __name__ == '__main__':
    unittest.main()
