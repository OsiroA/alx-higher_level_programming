#!/usr/bin/python3
'''
This script lists all cities in a specified state a given database
'''


import MySQLdb
from sys import argv
if __name__ == "__main__":
    contd = 0
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                 FROM cities \
                 LEFT JOIN states ON cities.state_id = states.id \
                 ORDER BY cities.id ASC")
    rows = cur.fetchall()

    for row in rows:
        if row[2] == argv[4]:
            if contd > 0:
                print(", ", end="")
            print(row[1], end="")
            contd = contd + 1
    print()
    # print(*[row[0] for row in rows], sep=", ")
    # for row in rows:
        # print(row)
    # if rows is not None:
      #  print(", ".join([row[2] if row[4] == argv[4]]))
    cur.close()
    db.close()
