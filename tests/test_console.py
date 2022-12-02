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

    @unittest.skipIf(type(storage) == FileStorage, 'Skip FileStorage')
    def test_create_db(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create State name="California"')
            res = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'create City state_id="{res}" name="Fremont"')
            res2 = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(
                f'create City state_id="{res}" name="San_Francisco"')
            res3 = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(
                f'create City state_id="{res}" name="San_Francisco_is_super_cool"')
            res4 = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(
                'create User email="my@me.com" password="pwd"\
 first_name="FN" last_name="LN"')
            res5 = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(
                f'create Place city_id="{res4}" user_id="{res5}"\
 name="My_house" description="no_description_yet" number_rooms=4\
 number_bathrooms=1 max_guest=3 price_by_night=100\
 latitude=120.12 longitude=101.4')
            res6 = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('all State')
            self.assertIn(res, f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('all City')
            self.assertIn(res2, f.getvalue().strip())
            self.assertIn(res3, f.getvalue().strip())
            self.assertIn(res4, f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'show Place {res6}')
            self.assertIn(res6, f.getvalue().strip())

        for obj in storage.all().values():
            storage.delete(obj)
        storage.save()

    @unittest.skipIf(type(storage) == DBStorage, 'Skip DbStorage')
    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create State')
            res = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create State name="California"')
            res2 = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(
                f'create City state_id="{res2}" name="Fremont"')
            res3 = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('all State')
            self.assertIn(res, f.getvalue().strip())
            self.assertIn(res2, f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('all City')
            self.assertIn(res2, f.getvalue().strip())
            self.assertIn(res3, f.getvalue().strip())
