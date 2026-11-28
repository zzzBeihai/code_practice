import sqlite3
conn = sqlite3.connect("...")
cur = conn.cursor()

sid = input("学号：")
name = input("姓名：")
cur.execute("SELECT name, score FROM student WHERE sod = ?", (sid,))
row = cur.fetchone()
if row:
    print(row[0], row[1])
elif input("是否新增？（Y|N）").lower() == "y":
    cur.execute("INSERT INTO student(sid, name, score) VALUES(?,?,?)", (sid, name, 0))
    conn.commit()
cur.execute("SELECT name, score FROM student ORDER BY sid")
for row in cur.fetchall():
    print(row)
cur.close()
conn.close()
