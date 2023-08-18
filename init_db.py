import sqlite3

connection = sqlite3.connect("vat_api.db")

with open("db_schema.sql") as schema_file:
    connection.executescript(schema_file.read())

cur = connection.cursor()
cur.execute("INSERT INTO TYPES (id, title) VALUES (1, 'book')")
cur.execute("INSERT INTO TYPES (id, title) VALUES (2, 'food')")

connection.commit()
connection.close()