#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeingKey


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), nullable = False, ForeingKey("cities.id"))
    user_id = Column(String(60), nullable = False, ForeingKey("users.id"))
    name = Column(String(128), nullable = False)
    description = Column((1024), nullable = False)
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
