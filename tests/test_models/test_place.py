#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value(city_id='123456789')
        self.assertEqual(new.city_id, '123456789')

    def test_user_id(self):
        """ """
        new = self.value(user_id='123456789')
        self.assertEqual(new.user_id, '123456789')

    def test_name(self):
        """ """
        new = self.value(name='California')
        self.assertEqual(new.name, 'California')

    def test_description(self):
        """ """
        new = self.value(description='Hola que hace')
        self.assertEqual(new.description, 'Hola que hace')

    def test_number_rooms(self):
        """ """
        new = self.value(number_rooms=2)
        self.assertEqual(new.number_rooms, 2)

    def test_number_bathrooms(self):
        """ """
        new = self.value(number_bathrooms=3)
        self.assertEqual(new.number_bathrooms, 3)

    def test_max_guest(self):
        """ """
        new = self.value(max_guest=4)
        self.assertEqual(new.max_guest, 4)

    def test_price_by_night(self):
        """ """
        new = self.value(price_by_night=20)
        self.assertEqual(new.price_by_night, 20)

    def test_latitude(self):
        """ """
        new = self.value(latitude=101.5)
        new.save()
        self.assertEqual(new.latitude, 101.5)

    def test_longitude(self):
        """ """
        new = self.value(longitude=200.4)
        new.save()
        self.assertEqual(new.longitude, 200.4)

    def test_amenity_ids(self):
        """ """
        new = self.value(amenity_ids=[10, 4, 5])
        new.save()
        self.assertEqual(new.amenity_ids, [10, 4, 5])
