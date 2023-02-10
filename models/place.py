#!/usr/bin/python3

"""
This module provides the class Place
"""


from models import base_model


class Place(base_model.BaseModel):
    """
    Place class that inherits from BaseModel
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitiude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
