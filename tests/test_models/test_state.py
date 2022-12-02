#!/usr/bin/python3
""" """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models import storage


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    @unittest.skipIf(type(storage) == FileStorage, "FileStorage ignore")
    def test_model(self):
        new = self.value(name='California')
        new.save()
        self.assertEqual(storage.all()['State'+'.'+new.id], new)

    @unittest.skipIf(type(storage) == DBStorage, "DBStorage ignore")
    def test_name3(self):
        """ """
        new = self.value(name='California')
        new.save()
        self.assertEqual(new.name, 'California')
