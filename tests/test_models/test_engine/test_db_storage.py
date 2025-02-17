#!/usr/bin/python3
""" Module for testing DB storage"""
import os
import unittest
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class TestDBStorage(unittest.TestCase):
    # def setUp(self) -> None:
    #     if type(storage) == DBStorage:
    #         self.storage = storage
    #         self.user = User(email='none@gmail.com', password='password')
    #         self.user.save()
    #         self.state = State(name='California')
    #         self.state.save()
    #         self.city = City(name='San Francisco', state_id=self.state.id)
    #         self.city.save()
    #         self.place = Place(user_id=self.user.id,
    #                            city_id=self.city.id, name='Church')
    #         self.place.save()
    #         self.review = Review(user_id=self.user.id,
    #                              palce_id=self.place.id, text='Very good')
    #         self.review.save()
    #         self.amenity = Amenity(name='TV')
    #         self.amenity.save()

    def tearDown(self) -> None:
        if type(storage) == DBStorage:
            for obj in storage.all().values():
                storage.delete(obj)
            storage.save()

    @unittest.skipIf(type(storage) == FileStorage, "File Storage ignore")
    def test_instance_creation(self):
        self.assertEqual(type(storage), DBStorage)

    @unittest.skipIf(type(storage) == FileStorage, "File Storage ignore")
    def test_all(self):
        state = State(name='California')
        state.save()
        states = storage.all(State)
        self.assertEqual(state.id, states['State'+'.'+state.id].id)
