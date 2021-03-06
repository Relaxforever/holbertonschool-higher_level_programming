#!/usr/bin/python3
""" module gets a database and prints it in ascending order """
import MySQLdb
import sys

if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost",
                          user=sys.argv[1],
                          passwd=sys.argv[2],
                          db=sys.argv[3],
                          port=3306)
    cursor = con.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM states\
                    INNER JOIN cities\
                    ON cities.state_id=states.id\
                    ORDER BY id asc")
    rows = cursor.fetchall()
    for row in rows:
        print("{}".format(row))
