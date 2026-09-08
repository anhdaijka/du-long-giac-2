import sqlite3

conn = sqlite3.connect('story_database.sqlite3')
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cur.fetchall()
print("Tables:", tables)

for t in tables:
    tname = t[0]
    cur.execute(f"SELECT count(*) FROM [{tname}]")
    count = cur.fetchone()[0]
    print(f"Table {tname}: {count} rows")

    # print columns
    cur.execute(f"PRAGMA table_info([{tname}])")
    cols = cur.fetchall()
    col_names = [c[1] for c in cols]
    print(f"  Columns: {col_names}")
