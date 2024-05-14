#!/usr/bin/python3
"""
use the module MySQLdb
"""
import MySQLdb
import sys

if len(sys.argv) != 5:
    print("Invalid arguments")

username, password, database, state_name_searched = sys.argv[1:]

db = MySQLdb.connect(
        user=username,
        host='localhost',
        passwd=password,
        port=3306,
        db=database
        )
cur = db.cursor()
cur.execute('''
            SELECT *
            FROM states
            WHERE name COLLATE utf8mb4_bin="{}"
            ORDER BY states.id ASC
            '''.format(state_name_searched))

result = cur.fetchall()
for data in result:
    print(data)
cur.close()
db.close()
