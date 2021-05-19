import sqlite3
import json

conn_sql = sqlite3.connect('database.db')
cursor = conn_sql.cursor()

cursor.execute("DELETE FROM posts WHERE name <> 0")
cursor.execute("DELETE FROM users WHERE name <> 0")

cursor.execute(" INSERT INTO users(name, password, role) VALUES('vladik', 'password', 2)")
cursor.execute(" INSERT INTO users(name, password, role) VALUES('petya', 'password', 1)")

cursor.execute(" INSERT INTO posts(name, id_users, name, category, author, price, telephone) VALUES('TEST', 1, 'TEST', 'TEST', 'TEST', 'TEST', 'TEST')")
cursor.execute(" INSERT INTO posts(name, id_users, name, category, author, price, telephone) VALUES('TEST', 1, 'TEST', 'TEST', 'TEST', 'TEST', 'TEST')")

cursor.close()
conn_sql.commit()
conn_sql.close()
