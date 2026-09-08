import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('story_database.sqlite3')
cur = conn.cursor()

cur.execute("SELECT sub_id, name, describe_cleaned FROM subtasks WHERE sub_id = 641")
r = cur.fetchone()
print(f"Subtask {r[0]}: {r[1]}")
print(f"Desc:\n{r[2]}")
cur.execute("SELECT phase, raw_text, cleaned_text FROM dialogues WHERE sub_id = 641")
for d in cur.fetchall():
    print(f"Dialogue:\nRaw: {d[1]}\nClean: {d[2]}")
