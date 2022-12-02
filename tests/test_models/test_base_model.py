#!/usr/bin/python3
""" """
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models import storage
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel
        self.data = {}

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        if type(storage) == FileStorage:
            try:
                os.remove('file.json')
            except:
                pass
        else:
            for obj in storage.all().values():
                storage.delete(obj)
            storage.save()

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skipIf(type(storage) == DBStorage, "DBStorage ignore")
    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    @unittest.skipIf(type(storage) == FileStorage, "FileStorage ignore")
    def test_save_db(self):
        if self.value != BaseModel:
            i = self.value(**self.data)
            i.save()
            key = self.name + "." + i.id
            self.assertEqual(storage.all()[key], i)

    def test_str(self):
        """ """
        i = self.value()
        val = i.__dict__.pop('_sa_instance_state', None)
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

        if val:
            i.__dict__['_sa_instance_state'] = val

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)
