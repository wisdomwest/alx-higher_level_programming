#!/usr/bin/python3
"""List all states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    query = """
         SELECT cities.id, cities.name, states.name
         FROM cities
         JOIN states ON cities.state_id = states.id
         ORDER BY cities.id ASC
    """
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
