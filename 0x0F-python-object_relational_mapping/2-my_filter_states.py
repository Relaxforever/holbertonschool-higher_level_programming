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
    cursor.execute("SELECT * from states WHERE name\
                   LIKE BINARY '{}' ORDER BY id asc"
                   .format(sys.argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print("{}".format(row))
