#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import association_table


class Amenity(BaseModel, Base):
    """An amenity to stay"""
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    place_amenities = relationship(
        'Place', secondary='place_amenity', backref='amenities', viewonly=False)
