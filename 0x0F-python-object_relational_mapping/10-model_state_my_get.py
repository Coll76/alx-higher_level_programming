#!/usr/bin/python3
"""
prints the State object with the name passed as
argument from the database hbtn_0e_6_usa

Your script should take 4 arguments: mysql username,
mysql password, database name and
state name to search (SQL injection free)
You must use the module SQLAlchemy
You must import State and Base from
model_state - from model_state import Base, State
Your script should connect to a MySQL server
running on localhost at port 3306
You can assume you have one record with the state name to search
Results must display the states.id
If no state has the name you searched for, display Not found
"""
from sqlalchemy import Column, String, Integer, create_engine, asc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
import sys


def main():
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]
                )
            )
    session = sessionmaker(bind=engine)
    sess = session()

    output = sess.query(State).filter(
            State.name == sys.argv[4]
            ).order_by(asc(State.id)).first()

    if not output:
        print("Not found")
    else:
        print(output.id)

    sess.close()


if __name__ == "__main__":
    main()
