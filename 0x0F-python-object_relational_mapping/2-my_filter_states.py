#!/usr/bin/python3
"""
 lists all states from the database hbtn_0e_0_usa
 take 3 arguments: mysql username, mysql password and database name
 must use the module
 should connect to a MySQL server running on localhost at port 3306
 Results must be sorted in ascending order by states.id
lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys


def main():
    """
    connects to mysql server
    """
    if len(sys.argv) != 5:
            return
    username, password, database, nam = sys.argv[1:]
    db = MySQLdb.connect(
            host = 'localhost',
            port = 3306,
            user = username,
            passwd = password,
            db = database
            )
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE "N%" AND name = "{}" ORDER BY id ASC'.format(nam))
    ro = cur.fetchall()
    for r in ro:
        print(r)
    if cur:
        cur.close()
    if db:
        db.close()
if __name__ == '__main__':
    main()
