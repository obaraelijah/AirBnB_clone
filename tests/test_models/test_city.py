#!/usr/bin/python3

"""
Test modules for class city in  models city
"""

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """
    Test case for class city
    """
    
    def initEnv(self):
        self.city = City()
        self.city_attr = ["state_id", "name"]

    def test_has_attributes(self):
        for items in self.city_attr:
            self.assertIs(type(getattr(self.city, items)), str)
