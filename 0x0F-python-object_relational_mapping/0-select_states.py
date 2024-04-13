#!/usr/bin/python3
"""
 lists all states from the database hbtn_0e_0_usa
 take 3 arguments: mysql username, mysql password and database name
 must use the module
 should connect to a MySQL server running on localhost at port 3306
 Results must be sorted in ascending order by states.id

 """

import MySQLdb
import sys

def main():
    """
    connects to mysql server
    """
    if len(sys.argv) != 4:
            return
    username, password, database = sys.argv[1:]
    db = MySQLdb.connect(
            host = 'localhost',
            port = 3306,
            user = username,
            passwd = password,
            db = database
            )
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    ro = cur.fetchall()
    for r in ro:
        print(r)
    if 'cur' is not None:
        cur.close()
    db.close()
if __name__ == '__main__':
    main()
