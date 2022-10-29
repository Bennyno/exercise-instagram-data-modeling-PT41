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
    id = Column(Integer, primary_key=True) 
    caption = Column(String(250), nullable=True) 
    user_id = Column(Integer, nullable=True) 
    Likes = Column(Integer, nullable=True)
    image_size = Column(Integer, nullable=True) 
    date_created = Column(DateTime, nullable=True) 
    date_updated = Column(DateTime, nullable=True) 
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')

class Comment(Base):    
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e