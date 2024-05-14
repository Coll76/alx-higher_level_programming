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
"""
COLLATE utf8_bin makes it case sensitive
"""
cur.execute('''
            SELECT *
            FROM states
            WHERE name COLLATE utf8mb4_bin LIKE "N%"
            ORDER BY states.id ASC
            ''')

result = cur.fetchall()
for data in result:
    print(data)
cur.close()
db.close()
