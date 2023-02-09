#!/usr/bin/python3
"""
This module provides the class state
"""

from models import base_model

class State(base_model.BaseModel):
    """
    state class that inherits from the Basemodel
    """
    
    name = ""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)