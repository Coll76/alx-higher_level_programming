#!/usr/bin/python3
"""
import to connect to server
"""

import sys
from sqlalchemy import create_engine, String, Integer, Column
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

"""
prints the first State object from the database hbtn_0e_6_usa
take 3 arguments: mysql username, mysql password and database name
import State and Base from model_state
connect to a MySQL server running on localhost at port 3306
 sorted in ascending order by states.id
"""


def main():
    """
    wraps code to single unit
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
    output = sess.query(State).filter(State.id == 1).first()
    if output is None:
        print(" ")
        print()
    else:
        print(f"{output.id}: {output.name}")
    sess.close()


if __name__ == "__main__":
    main()
