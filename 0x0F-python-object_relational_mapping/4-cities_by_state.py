#!/usr/bin/python3
"""a script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM cities")
    states = cur.fetchall()

    for state in states:
        print(state)
    cur.close()
    db.close()
