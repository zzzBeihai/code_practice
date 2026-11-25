import sqlite3

conn = sqlite3.connect("classroom.db")
cur = conn.cursor()
cur.execute("SELECT nuber, capacity FROM manage WHERE in_use = 1")
for number, capacity in cur.fetchall():
    print(number, capacity)
conn.close()