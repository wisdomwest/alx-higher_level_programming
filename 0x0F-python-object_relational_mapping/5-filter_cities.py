#!/usr/bin/python3
"""List all states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    query = """
         SELECT cities.name FROM cities
         JOIN states ON cities.state_id = states.id
         WHERE states.name = %s
         ORDER BY cities.id ASC
    """
    cur.execute(query, (argv[4],))
    query_rows = cur.fetchall()
    data = map(lambda x: x[0], query_rows)
    result = ", ".join(data)
    print(result)
    cur.close()
    conn.close()
