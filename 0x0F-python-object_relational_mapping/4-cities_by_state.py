#!/usr/bin/python3
"""
MySQLdb module for connecting to mysql server
"""

import MySQLdb
import sys

"""
Connects to mysql  server and joins 2 tables
And executes an sql query
"""


def main():
    """
    Wraps the code to a single unit
    """
    if len(sys.argv) != 4:
        print("Invlid number of args")
        return
    username, password, name = sys.argv[1:]
    db = MySQLdb.connect(
            passwd=password,
            user=username,
            host='localhost',
            db=name,
            port=3306
            )
    cur = db.cursor()
    # table = 'cities'
    cur.execute('''
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
            ''')
    ro = cur.fetchall()
    for r in ro:
        print(r)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
