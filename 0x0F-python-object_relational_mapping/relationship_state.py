#!/usr/bin/python3
'''
This is a script thst contains a class definition
'''
import sys
# from model_state import Base, State
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    '''
    This inherits from Base and links to the MySQL tsble
    '''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')
