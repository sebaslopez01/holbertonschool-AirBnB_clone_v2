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

    def test_place_id(self):
        """ """
        new = self.value(place_id='12345689')
        new.save()
        self.assertEqual(new.place_id, '12345689')

    def test_user_id(self):
        """ """
        new = self.value(user_id='12345689')
        new.save()
        self.assertEqual(new.user_id, '12345689')

    def test_text(self):
        """ """
        new = self.value(text='hola que hace')
        new.save()
        self.assertEqual(new.text, 'hola que hace')
