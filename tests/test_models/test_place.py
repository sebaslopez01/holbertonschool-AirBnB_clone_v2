#!/usr/bin/python3
""" """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.city import City
from models.user import User
from models.state import State
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models import storage


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    @unittest.skipIf(type(storage) == FileStorage, "FileStorage ignore")
    def test_model(self):
        state = State(name='California')
        state.save()
        city = City(name='Cali', state_id=state.id)
        city.save()
        user = User(email='dawd@gmail.com', password='1234')
        user.save()
        new = self.value(city_id=city.id, user_id=user.id,
                         name='Church', description='Hola que hace',
                         number_rooms=2, number_bathrooms=3,
                         max_guest=4, price_by_night=20)
        new.save()
        self.assertEqual(storage.all()['Place'+'.'+new.id], new)

    @unittest.skipIf(type(storage) == DBStorage, "DBStorage ignore")
    def test_city_id(self):
        """ """
        new = self.value(city_id='123456789', user_id='123456789',
                         name='Church', description='Hola que hace',
                         number_rooms=2, number_bathrooms=3,
                         max_guest=4, price_by_night=20)
        self.assertEqual(new.city_id, '123456789')

    @unittest.skipIf(type(storage) == DBStorage, "DBStorage ignore")
    def test_user_id(self):
        """ """
        new = self.value(city_id='123456789', user_id='123456789',
                         name='Church', description='Hola que hace',
                         number_rooms=2, number_bathrooms=3,
                         max_guest=4, price_by_night=20)
        self.assertEqual(new.user_id, '123456789')

    @unittest.skipIf(type(storage) == DBStorage, "DBStorage ignore")
    def test_name(self):
        """ """
        new = self.value(city_id='123456789', user_id='123456789',
                         name='Church', description='Hola que hace',
                         number_rooms=2, number_bathrooms=3,
                         max_guest=4, price_by_night=20)
        self.assertEqual(new.name, 'Church')

    @unittest.skipIf(type(storage) == DBStorage, "DBStorage ignore")
    def test_description(self):
        """ """
        new = self.value(city_id='123456789', user_id='123456789',
                         name='Church', description='Hola que hace',
                         number_rooms=2, number_bathrooms=3,
                         max_guest=4, price_by_night=20)
        self.assertEqual(new.description, 'Hola que hace')

    @unittest.skipIf(type(storage) == DBStorage, "DBStorage ignore")
    def test_number_rooms(self):
        """ """
        new = self.value(city_id='123456789', user_id='123456789',
                         name='Church', description='Hola que hace',
                         number_rooms=2, number_bathrooms=3,
                         max_guest=4, price_by_night=20)
        self.assertEqual(new.number_rooms, 2)

    @unittest.skipIf(type(storage) == DBStorage, "DBStorage ignore")
    def test_number_bathrooms(self):
        """ """
        new = self.value(city_id='123456789', user_id='123456789',
                         name='Church', description='Hola que hace',
                         number_rooms=2, number_bathrooms=3,
                         max_guest=4, price_by_night=20)
        self.assertEqual(new.number_bathrooms, 3)

    @unittest.skipIf(type(storage) == DBStorage, "DBStorage ignore")
    def test_max_guest(self):
        """ """
        new = self.value(city_id='123456789', user_id='123456789',
                         name='Church', description='Hola que hace',
                         number_rooms=2, number_bathrooms=3,
                         max_guest=4, price_by_night=20)
        self.assertEqual(new.max_guest, 4)

    @unittest.skipIf(type(storage) == DBStorage, "DBStorage ignore")
    def test_price_by_night(self):
        """ """
        new = self.value(city_id='123456789', user_id='123456789',
                         name='Church', description='Hola que hace',
                         number_rooms=2, number_bathrooms=3,
                         max_guest=4, price_by_night=20)
        self.assertEqual(new.price_by_night, 20)

    @unittest.skipIf(type(storage) == DBStorage, "DBStorage ignore")
    def test_latitude(self):
        """ """
        new = self.value(city_id='123456789', user_id='123456789',
                         name='Church', description='Hola que hace',
                         number_rooms=2, number_bathrooms=3,
                         max_guest=4, price_by_night=20,
                         latitude=101.5)
        new.save()
        self.assertEqual(new.latitude, 101.5)

    @unittest.skipIf(type(storage) == DBStorage, "DBStorage ignore")
    def test_longitude(self):
        """ """
        new = self.value(city_id='123456789', user_id='123456789',
                         name='Church', description='Hola que hace',
                         number_rooms=2, number_bathrooms=3,
                         max_guest=4, price_by_night=20,
                         latitude=101.5, longitude=200.4)
        new.save()
        self.assertEqual(new.longitude, 200.4)

    @unittest.skipIf(type(storage) == DBStorage, "DBStorage ignore")
    def test_amenity_ids(self):
        """ """
        new = self.value(amenity_ids=[10, 4, 5])
        new.save()
        self.assertEqual(new.amenity_ids, [10, 4, 5])
