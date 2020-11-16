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
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    first_name = Column(String(40), nullable=False)
    last_name = Column(String(80), nullable=False)
    nickname = Column(String(120), nullable=False)
    email = Column(String(120), nullable=False)
    password = Column(String(40), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    image = Column(String(400), nullable=False)
    text = Column(String(400))
    # published_at = Column(timestamp)

class Post_comment(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    likes = Column(Integer, nullable=False)
    # published_at = Column(timestamp)
    
class Comment_likes(Base):
    __tablename__ = 'comment_likes'
    author_id = Column(Integer, ForeignKey('user.id'))
    post_comment_id = Column(Integer, ForeignKey('post.id'))
    # published_at = Column(timestamp)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')