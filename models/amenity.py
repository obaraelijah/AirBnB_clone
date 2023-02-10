#!/usr/bin/python3
"""
This module provides the class Amenity
"""

from models import base_model

class Amenity(base_model.BaseModel):
    """
    Amenity class that inherits form BaseModel
    """
    
    name = ""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)