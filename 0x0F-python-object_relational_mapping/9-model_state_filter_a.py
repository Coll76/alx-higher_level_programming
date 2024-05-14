#!/usr/bin/python3
"""
use the module SQLAlchemy
lists all State objects that contain the
letter a from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine, String, Integer, Column
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


def main():
    """
    Encapsulates the code
    """
    if len(sys.argv) != 4:
        print("Invalid arguments")

    username, password, database = sys.argv[1:]

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                username, password, database)
            )
    session = sessionmaker(bind=engine)
    sess = session()
    result = sess.query(State).filter(
            State.name.ilike('%a%')).order_by(State.id.asc()).all()
    for data in result:
        print(f"{data.id}: {data.name}")

    sess.close()


if __name__ == "__main__":
    main()
