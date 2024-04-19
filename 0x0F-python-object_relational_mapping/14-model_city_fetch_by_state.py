#!/usr/bin/python3
"""
"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

"""
"""


def main():
    """
    """
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]
                ),
            pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    sess = session()
    output = sess.query(City, State).join(State).filter(City.state_id == State.id).order_by(City.id.asc()).all()
    for city, state in output:
        print(f"{state.name}: ({city.id} {city.name}")
    sess.close()
    

if __name__ == "__main__":
    main()
