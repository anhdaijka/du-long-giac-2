import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')
conn = sqlite3.connect('story_database.sqlite3')
cur = conn.cursor()

print("=== SEARCH FOR 'Ô Sơ' ===")
for r in cur.execute("SELECT sub_id, name, describe_cleaned FROM subtasks WHERE describe_cleaned LIKE '%Ô Sơ%'").fetchall():
    print(f"Subtask {r[0]}: {r[1]}")
    print(f"Desc: {r[2]}\n")

print("=== SEARCH FOR 'Cáp Xá' ===")
for r in cur.execute("SELECT sub_id, name, describe_cleaned FROM subtasks WHERE describe_cleaned LIKE '%Cáp Xá%'").fetchall():
    print(f"Subtask {r[0]}: {r[1]}")
    print(f"Desc: {r[2]}\n")

print("=== SEARCH FOR 'Nhất Phẩm Đường' ===")
for r in cur.execute("SELECT sub_id, name, describe_cleaned FROM subtasks WHERE describe_cleaned LIKE '%Nhất Phẩm Đường%' LIMIT 3").fetchall():
    print(f"Subtask {r[0]}: {r[1]}")
    print(f"Desc: {r[2]}\n")
