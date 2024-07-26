import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy.schema import PrimaryKeyConstraint


Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    __table_args__ = (
        PrimaryKeyConstraint(user_from_id, user_to_id),
        {},
    )

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    firstname = Column(String(100))
    lastname = Column(String(100))
    email = Column(String(150), nullable=False)

class MediaEnum(enum.Enum):
    PHOTO='photo'
    VIDEO='video'

class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    type = Column('value', Enum(MediaEnum))
    url = Column(String(300))
    post_id = Column(Integer, ForeignKey('post.id'))

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(500))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
