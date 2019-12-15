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
    cursor.execute("SELECT cities.name FROM states\
                    INNER JOIN cities\
                    ON cities.state_id=states.id\
                    WHERE states.name=%s\
                    ORDER BY cities.id asc", (sys.argv[4], ))
    rows = cursor.fetchall()
    city = ""
    for row in rows:
        for column in row:
            city += column + ', '
    city = city[:-2]
    print(city)
