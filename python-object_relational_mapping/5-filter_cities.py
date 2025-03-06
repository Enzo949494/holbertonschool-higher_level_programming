#!/usr/bin/python3
"""
Lists all cities of a state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """
    Connects to the database, retrieves and displays all cities
    of a given state, sorted by cities.id.
    This version is safe from SQL injection.
    """
    # Connect to the MySQL server on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the SQL query using parameterized queries to prevent injection
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
    """
    cursor.execute(query, (sys.argv[4],))

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Print the city names as a comma-separated list
