#!/usr/bin/python3
""" """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.state import State
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models import storage


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    @unittest.skipIf(type(storage) == FileStorage, "FileStorage ignore")
    def test_model(self):
        state = State(name='California')
        state.save()
        new = self.value(name='Cali', state_id=state.id)
        new.save()
        self.assertEqual(storage.all()['City'+'.'+new.id], new)

    @unittest.skipIf(type(storage) == DBStorage, "DBStorage ignore")
    def test_state_id(self):
        """ """
        new = self.value(name='Cali', state_id='123456789')
        new.save()
        self.assertEqual(new.state_id, '123456789')

    @unittest.skipIf(type(storage) == DBStorage, "DBStorage ignore")
    def test_name(self):
        """ """
        new = self.value(name='Cali', state_id='123456789')
        new.save()
        self.assertEqual(new.name, 'Cali')
