#!/usr/bin/python3
"""
uses the module MySQLdb
"""
import MySQLdb
import sys

if len(sys.argv) != 4:
    print("Invalid arguments")

username, password, database = sys.argv[1:]
db = MySQLdb.connect(
        user=username,
        host='localhost',
        db=database,
        passwd=password,
        port=3306
        )
cur = db.cursor()
cur.execute('SELECT * FROM states WHERE name LIKE "N%" ORDER BY states.id ASC')
result = cur.fetchall()
for data in result:
    print(data)
cur.close()
db.close()
