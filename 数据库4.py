import sqlite3 as sql
conn = sql.connect("...")
cur = conn.cursor()
while True:
    barcode = input("Enter a barcode: ")
    if barcode == "0":
        break
    cur.execute("SELECT available FROM book WHERE barcode = ?", (barcode,))
    available = cur.fetchone()
    if available is not None:
        print(f"{barcode}: {"available" if available[0] == 1 else "not available" }) ")
    else:
        ans = input("Y or N?")

