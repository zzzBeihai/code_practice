import sqlite3
conn = sqlite3.connect('classroom.db')
cur = conn.cursor()

while True:
    number = input("请输入教室房间号，输入0退出：")
    if number == '0':
        break
    cur.execute("SELECT in_use FROM manage WHERE number = ?", (number,))
    row = cur.fetchone()
    if row:
        if row[0] == 1:
            print(f"{number}教室为在用状态")
        else:
            print(f"{number}教室为空闲状态")
    else:
        ans = input(f"{number}教室不存在，要新增吗？（Y/N）")
        if ans == 'Y':
            floor = number[0] + "楼"
            cur.execute("INSERT INTO manage(number, floor, capacity, in_use)"
                        "VALUES(?,?,?,?)",
                        (number, floor, 30, 0)
                        )
            conn.commit()
            print("success!")
cur.close()
conn.close()