#!/usr/bin/python3
"""
script to list all states starting with aa capital N
"""


import sys
import MySQLdb

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    kerser = connection.cursor()
    kerser.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rowContent = kerser.fetchall()
    for rows in rowContent:
        print (rows)

    kerser.close()
    connection.close()
