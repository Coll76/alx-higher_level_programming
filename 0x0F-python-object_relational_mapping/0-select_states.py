#!/usr/bin/python3
"""
module MySQLdb for manipulation of database
"""
import MySQLdb
import sys

if len(sys.argv) != 4:
    print("Invalid arguments")

username, password, database = sys.argv[1:]

db = MySQLdb.connect(
        host='localhost',
        user=username,
        db=database,
        port=3306,
        passwd=password
        )
cur = db.cursor()
cur.execute('SELECT * FROM states ORDER BY states.id ASC')
result = cur.fetchall()
for data in result:
    print(data)
cur.close()
db.close()
