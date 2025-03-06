#!/usr/bin/python3
"""
Defines a State class and an instance of Base for SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
# Create the Base class for declarative mapping
Base = declarative_base()


class State(Base):
    """
    State class that links to the MySQL table 'states'.
    Attributes:
        id (int): The state's id, primary key,
        auto-generated, unique, not null.
        name (str): The state's name, string with max 128 characters, not null.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


class City(Base):
    """
    City class that links to the MySQL table 'cities'.
    Attributes:
        id (int): The city's id, primary key, auto-generated, unique, not null.
        name (str): The city's name, string with max 128 characters, not null.
        state_id (int): The state's id, foreign key to states.id, not null.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
