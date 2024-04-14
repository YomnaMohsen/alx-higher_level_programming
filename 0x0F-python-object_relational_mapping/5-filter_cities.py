#!/usr/bin/python3
"""a script that takes in the name of a state as an argument 
and lists all cities of that state, 
using the database hbtn_0e_4_usa"""

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
    name = argv[4]
    cur.execute("SELECT cities.name FROM cities INNER \
                   JOIN states ON cities.state_id = states.id \
                   WHERE states.name ='{};".format(name))
    city = cur.fetchall()

    for c in city:
        print(c)
    cur.close()
    db.close()
