#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City
        self.data = {'state_id': '123456789', 'name': 'Cali'}

    def test_state_id(self):
        """ """
        new = self.value(state_id='123456789')
        new.save()
        self.assertEqual(new.state_id, '123456789')

    def test_name(self):
        """ """
        new = self.value(name='Cali')
        new.save()
        self.assertEqual(new.name, 'Cali')
