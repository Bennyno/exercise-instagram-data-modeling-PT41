import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), unique = True, nullable=False)
    favorite_id = Column(Integer, ForeignKey("favorites.id"))
    favorites = relationship("Favorites")
    


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    favorite_planet_id = Column(Integer, ForeignKey("planets.id"))
    favorite_planet = relationship("Planets")
    favorite_character_id = Column(Integer, ForeignKey("people.id"))
    favorite_character = relationship("People")
  
    

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(String(250))
    mass = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250), nullable=True)
    eye_color = Column(String(250), nullable=True)
    birth_year = Column(String(250))
    gender = Column(String(250), nullable=True)
    homeworld_id = Column(Integer, ForeignKey("planets.id"))
    homeworld = relationship("Planets")



class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    rotation_period = Column(String(250))
    orbital_period = Column(String(250))
    diameter = Column(String(250))
    climate = Column(String(250))
    gravity = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(String(250))
    population = Column(String(250))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e