#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
should take 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
"""
import MySQLdb
import sys

if len(sys.argv) != 5:
    print("Invalid arguments")
    exit(98)

username, password, database, state = sys.argv[1:]
db = MySQLdb.connect(host='localhost', passwd=password, user=username, db=database, port=3306)
cursor = db.cursor()
cursor.execute('''
    SELECT cities.name
    FROM {}.states JOIN cities ON cities.state_id=states.id
    WHERE states.name = '{}'
    ORDER BY cities.id ASC
    '''.format(database, state))

rows = cursor.fetchall()
ro = ', '.join([row[0] for row in rows])
print(ro)
cursor.close()
db.close()
