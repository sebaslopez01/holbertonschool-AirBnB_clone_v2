#!/usr/bin/python3
""" """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models import storage


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    @unittest.skipIf(type(storage) == FileStorage, "FileStorage ignore")
    def test_model(self):
        state = State(name='California')
        state.save()
        city = City(name='Cali', state_id=state.id)
        city.save()
        user = User(email='hola@gmail.com', password='1234')
        user.save()
        place = Place(city_id=city.id, user_id=user.id,
                      name='Church', description='Hola que hace',
                      number_rooms=2, number_bathrooms=3,
                      max_guest=4, price_by_night=20)
        place.save()
        new = self.value(place_id=place.id, user_id=user.id, text='hola')
        new.save()
        self.assertEqual(storage.all()['Review'+'.'+new.id], new)

    @unittest.skipIf(type(storage) == DBStorage, "DBStorage ignore")
    def test_place_id(self):
        """ """
        new = self.value(place_id='12345689',
                         user_id='12345689', text='hola que hace')
        new.save()
        self.assertEqual(new.place_id, '12345689')

    @unittest.skipIf(type(storage) == DBStorage, "DBStorage ignore")
    def test_user_id(self):
        """ """
        new = self.value(place_id='12345689',
                         user_id='12345689', text='hola que hace')
        new.save()
        self.assertEqual(new.user_id, '12345689')

    @unittest.skipIf(type(storage) == DBStorage, "DBStorage ignore")
    def test_text(self):
        """ """
        new = self.value(place_id='12345689',
                         user_id='12345689', text='hola que hace')
        new.save()
        self.assertEqual(new.text, 'hola que hace')
