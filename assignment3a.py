import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    # delete database if table exists
    c.execute("DROP TABLE if EXISTS numbers")

    # Create Database Table
    c.execute("CREATE TABLE numbers(num INT)")

    #Insert each number to the database
    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)",(random.randint(0,100),))
