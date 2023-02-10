#!/usr/bin/python3

"""
This module provides the class City
"""


from models import base_model


class City(base_model.BaseModel):
    """
    City class that inherits from BaseModel
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
