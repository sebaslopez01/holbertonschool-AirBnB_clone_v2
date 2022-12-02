#!/usr/bin/pythone
"""Module for testing console"""

import os
import unittest
from unittest.mock import patch
from io import StringIO
from models import storage
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    def setUp(self) -> None:
        self.console = HBNBCommand()

    def tearDown(self):
        try:
            os.remove('file.json')
        except IOError:
            pass

    @unittest.skipIf(type(storage) == DBStorage, 'Skip DbStorage')
    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create State')
            res = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create State name="California"')
            res2 = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'create City state_id="{res2}" name="Fremont')
            res3 = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('all State')
            self.assertIn(res, f.getvalue().strip())
            self.assertIn(res2, f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('all City')
            self.assertIn(res2, f.getvalue().strip())
            self.assertIn(res3, f.getvalue().strip())
