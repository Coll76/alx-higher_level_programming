#!/usr/bin/python3
import MySQLdb
import sys

def main():
    if len(sys.argv) != 5:
        print("Invalid number of arguments")
        return
    username, password, database, state_name_searched = sys.argv[1:]
    db = MySQLdb.connect(passwd = password, db = database, user = username, host = 'localhost', port = 3306)
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name = '+ state_name_searched)
    output = cur.fetchall()
    for ou in output:
        print(ou)
    cur.close()
    db.close()
if __name__ == "__main__":
    main()
