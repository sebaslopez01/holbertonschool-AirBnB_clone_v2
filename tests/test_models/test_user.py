#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value(first_name='Sebas')

        self.assertEqual(new.first_name, 'Sebas')

    def test_last_name(self):
        """ """
        new = self.value(last_name='Lopez')
        self.assertEqual(new.last_name, 'Lopez')

    def test_email(self):
        """ """
        new = self.value(email='none@gmail.com')
        self.assertEqual(new.email, 'none@gmail.com')

    def test_password(self):
        """ """
        new = self.value(password='password')
        self.assertEqual(new.password, 'password')
