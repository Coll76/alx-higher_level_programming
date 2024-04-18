#!/usr/bin/python3
"""
Modules imported to onnect to database server
"""

import sys
from sqlalchemy import create_engine, String, Integer, Column
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

"""
lists all State objects from the database hbtn_0e_6_usa
take 3 arguments: mysql username, mysql password and database name
import State and Base from model_state
should connect to a MySQL server running on localhost at port 3306
sorted in ascending order by states.id
"""


def main():
    """
    wraps up the code to a single unit
    """
    if len(sys.argv) != 4:
        print('Invalid arguments')
        return
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]
                ),
            pool_pre_ping=True)

    Output = engine.execute('SELECT * FROM states ORDER BY states.id ASC')
    for ro in Output:
        print(ro)
    Output.close()


if __name__ == "__main__":
    main()
