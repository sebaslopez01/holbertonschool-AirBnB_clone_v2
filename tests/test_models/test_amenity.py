#!/usr/bin/python3
""" """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models import storage


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    @unittest.skipIf(type(storage) == FileStorage, "FileStorage ignore")
    def test_model(self):
        new = self.value(name='Bath')
        new.save()
        self.assertEqual(storage.all()['Amenity'+'.'+new.id], new)

    @unittest.skipIf(type(storage) == DBStorage, "DBStorage ignore")
    def test_name2(self):
        """ """
        new = self.value(name='Bath')
        new.save()
        self.assertEqual(new.name, 'Bath')
