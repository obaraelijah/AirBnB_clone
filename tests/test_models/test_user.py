

#!/usr/bin/python3

"""
Suite to test subclass User in models.user
"""

import unittest

from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """
    Test attributes attributes
    """
    
    def test_subclass_in_user(self):
        """
        Tests users attributes
        """
        self.assertTrue(issubclass(User, BaseModel))
    
    def test_attributes_in_user(self):
        i = User()
        self.assertIs(type(i.first_name), str)
        self.assertIs(type(i.last_name), str)
        self.assertTrue(i.first_name == "")
        self.assertTrue(i.last_name == "")
        self.assertIs(type(i.passworrd), str)
        self.assertIs(type(i.email), str)
        self.assertTrue(i.password == "")
        self.assertTrue(i.email == "")