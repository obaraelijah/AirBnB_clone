#!/usr/bin/python3

"""
Test suite for models.state
"""
import unittest

from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    """
     Test cases for class State
    """
    def initEnv(self):
        self.state = State()
    
    def test_state_as_subclass(self):
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_name_attr(self):
        self.assertTrue(hasattr(self.state, "name"))