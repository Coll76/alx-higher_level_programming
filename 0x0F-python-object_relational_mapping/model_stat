#!/usr/bin/python3
"""
Imports module SQLAlchemy for connecting python code to
mysql server
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

"""
contains the class definition of a State and
n instance Base = declarative_base()
State class:
    inherits from Base Tips
    links to the MySQL table states
    class attribute id that represents a column of an
    auto-generated, unique integer, can’t be null and is a primary key
    class attribute name that represents a column of
    a string with maximum 128 characters and can’t be null
connect to a MySQL server running on localhost at port 3306
classes who inherit from Base must be imported
before calling Base.metadata.create_all(engine)
"""


Base = declarative_base()


class State(Base):
    """
    create table called states with the columns id and name
    """
    __tablename__ = 'states'
    id = Column(
            Integer,
            unique=True,
            nullable=False,
            autoincrement=True,
            primary_key=True
            )
    name = Column(String(128), nullable=False)
