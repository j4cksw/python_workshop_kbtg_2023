import sqlite3

connection = sqlite3.connect("vat_api.db")

with open("db_schema.sql") as schema_file:
    connection.executescript(schema_file.read())


