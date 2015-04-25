import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    cities = [
        ('Boston', 'MA', 600000),
        ('Los Angeles', 'CA', 38000000),
        ('Houston', 'TX', 2100000),
        ('Philadelphia', 'PA', 1500000),
        ('San Antonio', 'TX', 1400000),
        ('San Diego', 'CA', 130000),
        ('Dallas', 'TX', 1200000),
        ('San Jose', 'CA', 900000),
        ('Jacksonville', 'FL', 800000),
        ('Indianapolis', 'IN', 800000),
        ('Austin', 'TX', 800000),
        ('Detroit', 'MI', 700000)
    ]
    c.execute("DROP TABLE if EXISTS Population")

    c.execute("""CREATE TABLE population (city TEXT, state TEXT, population INT)""")

    c.executemany("INSERT INTO Population VALUES(?, ?, ?)", cities)

    c.execute("SELECT avg(population) FROM Population WHERE Population > 100000")

    rows = c.fetchall()

    for r in rows:
        print r