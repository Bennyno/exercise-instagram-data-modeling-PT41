import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    user_login = Column(String(250), unique = True, nullable=False)
    user_password = Column(String, nullable=False)
    # user_id = Column(Integer, ForeignKey('user.id'))
    # user = relationship('User') 
    


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique= True, nullable = False)
    email = Column(String(250), unique= True, nullable = False)
    first_name = Column(String(250), nullable = False)
    last_name = Column(String(250), nullable = False)
    dob = Column(Integer, nullable = False)
    media_id = Column(Integer, ForeignKey('media.id'))
    media = relationship('Media')
        
class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique= True, nullable = False)
    email = Column(String(250), unique= True, nullable = False)
    first_name = Column(String(250), nullable = False)
    last_name = Column(String(250), nullable = False)
    dob = Column(Integer, nullable = False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True) ## ID of the user who owns this post
    caption = Column(String(250), nullable=True) ## Photo caption
    user_id = Column(Integer, nullable=True) #*ID of the user who owns this photo
    Likes = Column(Integer, nullable=True) ## how many likes the photo has
    image_size = Column(Integer, nullable=True) ## Image size on server
    date_created = Column(DateTime, nullable=True) #* When this image was created (cher
    date_updated = Column(DateTime, nullable=True) ## Last time this image was updated
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')

class Comment(Base):    
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post')
    



# class Planets(Base):
#     __tablename__ = 'planets'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250))
#     rotation_period = Column(String(250))
#     orbital_period = Column(String(250))
#     diameter = Column(String(250))
#     climate = Column(String(250))
#     gravity = Column(String(250))
#     terrain = Column(String(250))
#     surface_water = Column(String(250))
#     population = Column(String(250))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e