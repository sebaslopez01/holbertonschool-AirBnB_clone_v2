#!/usr/bin/python3
""" """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models import storage


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    @unittest.skipIf(type(storage) == FileStorage, "FileStorage ignore")
    def test_model(self):
        new = self.value(email='hola@gmail.com', password='1234')
        new.save()
        self.assertEqual(storage.all()['User'+'.'+new.id], new)

    @unittest.skipIf(type(storage) == DBStorage, "DBStorage ignore")
    def test_first_name(self):
        """ """
        new = self.value(first_name='Sebas',
                         email='none@gmail.com', password='1234')
        new.save()
        self.assertEqual(new.first_name, 'Sebas')

    @unittest.skipIf(type(storage) == DBStorage, "DBStorage ignore")
    def test_last_name(self):
        """ """
        new = self.value(last_name='Lopez',
                         email='none@gmail.com', password='1234')
        new.save()
        self.assertEqual(new.last_name, 'Lopez')

    @unittest.skipIf(type(storage) == DBStorage, "DBStorage ignore")
    def test_email(self):
        """ """
        new = self.value(email='none@gmail.com', password='1234')
        new.save()
        self.assertEqual(new.email, 'none@gmail.com')

    @unittest.skipIf(type(storage) == DBStorage, "DBStorage ignore")
    def test_password(self):
        """ """
        new = self.value(email='none@gmail.com', password='1234')
        new.save()
        self.assertEqual(new.password, '1234')
