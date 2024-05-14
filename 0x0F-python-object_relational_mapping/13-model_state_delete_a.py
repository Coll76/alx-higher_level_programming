#!/usr/bin/python3
"""
use the module SQLAlchemy
"""
import sys
from sqlalchemy import create_engine, String, Integer, Column
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

"""
deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
take 3 arguments: mysql username, mysql password and database name
import State and Base from model_state
connect to a MySQL server running on localhost at port 3306
code should not be executed when imported
"""


def main():
    """
    Encapsulates the code
    """
    if len(sys.argv) != 4:
        print("Invalid arguments")
        return

    username, password, database = sys.argv[1:]
    engine = create_engine(
                        'mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1],
                            sys.argv[2],
                            sys.argv[3]
                            ))

    session = sessionmaker(bind=engine)
    sess = session()

    deleted_rec = sess.query(State).filter(
            State.name.ilike('%a')).delete(synchronize_session=False)
    """
    Commit the changes
    """
    sess.commit()

    rest_of_recs = sess.query(State).order_by(State.id.asc()).all()
    for data in rest_of_recs:
        print(f"{data.id}: {data.name}")

    sess.close()


if __name__ == "__main__":
    main()
