#!/usr/bin/python3
"""Place Module"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Subclass of the BaseModel class

    Args:
        city_id: it will be the City.id
        user_id: it will be the User.id
        name: string-empty string
        description: string-empty string
        number_rooms: integer
        number_bathrooms: integer
        max_guest: integer
        price_by_night: integer
        latitude: float
        longitude: float
        amenity_ids: list of Amenity.id later
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
