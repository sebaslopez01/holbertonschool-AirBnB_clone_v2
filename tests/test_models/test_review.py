#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review
        self.data = {
            'place_id': '123456789',
            'user_id': '123456789',
            'text': 'hola que hace'
        }

    def test_place_id(self):
        """ """
        new = self.value(place_id='12345689',
                         user_id='12345689', text='hola que hace')
        new.save()
        self.assertEqual(new.place_id, '12345689')

    def test_user_id(self):
        """ """
        new = self.value(place_id='12345689',
                         user_id='12345689', text='hola que hace')
        new.save()
        self.assertEqual(new.user_id, '12345689')

    def test_text(self):
        """ """
        new = self.value(place_id='12345689',
                         user_id='12345689', text='hola que hace')
        new.save()
        self.assertEqual(new.text, 'hola que hace')
