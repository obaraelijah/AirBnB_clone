#!/usr/bin/python3

"""
This module provides the class Review
"""

from models import base_model


class Review(base_model.BaseModel):
    """
    Review class that inherits from BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)