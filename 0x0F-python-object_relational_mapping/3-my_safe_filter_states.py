#!/usr/bin/python3
"""
import module MySQLdb to connect python code
to our mysql server. Impoet sys to manipulate the commnd line arguments
"""

import MySQLdb
import sys

"""
Elimination of SQL  injection in such a way tht it does not occur
"""


def main():
    """
    Used to warp the data into a single unit
    Accepts arguments from the console
    Gets the password, username, database, state_name_searched
    """
    if len(sys.argv) != 5:
        print("Invalid number of arguments")
        return
    username, password, database, state_name_searched = sys.argv[1:]
    db = MySQLdb.connect(
            passwd=password,
            db=database,
            user=username,
            host='localhost',
            port=3306
            )
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name = %s', (state_name_searched,))
    output = cur.fetchall()
    for ou in output:
        print(ou)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
