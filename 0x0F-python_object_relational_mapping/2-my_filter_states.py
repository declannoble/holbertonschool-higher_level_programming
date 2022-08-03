#!/usr/bin/python3

import sys


import sys
import MySQLdb

if __name__ == "__main__":
    dbConnection = MySQLdb(host="localhost", 
                        port=3306, 
                        user=sys.argv[1], 
                        passwd=sys.argv[2]
                        db=sys.argv[3]
                        charset="utf8")

    dbCursor = dbConnection.cursor()
    dbCursor.execute(f"SELECT * FROM states where states.name = {sys.argv[4]} ORDER BY id ASC")

    dbQuery = dbCursor.fetchall()
    for row in dbQuery:
        print(row)

    dbCursor.close()
    dbConnection.close()
    
    
