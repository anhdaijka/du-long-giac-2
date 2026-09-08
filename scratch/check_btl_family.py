import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Search in story_database.sqlite3 or server for "cha", "mẹ", "phụ thân", "mẫu thân", "bạch", "thủ lĩnh nghĩa quân"
import sqlite3

conn = sqlite3.connect('story_database.sqlite3')
cur = conn.cursor()

print("=== CHECKING BACH THU LAM BACKGROUND IN SQLITE ===")
cur.execute("SELECT sub_id, cleaned_text FROM dialogues WHERE cleaned_text LIKE '%Bạch Thu Lâm%' OR cleaned_text LIKE '%Thu Lâm%'")
for r in cur.fetchall():
    for line in r[1].splitlines():
        if any(k in line for k in ["cha", "mẹ", "phụ", "mẫu", "xuất thân", "gia đình", "tộc"]):
            print(f"Sub {r[0]}: {line}")

cur.execute("SELECT sub_id, describe_cleaned FROM subtasks WHERE describe_cleaned LIKE '%Bạch Thu Lâm%' OR describe_cleaned LIKE '%Thu Lâm%'")
for r in cur.fetchall():
    for line in r[1].splitlines():
        if any(k in line for k in ["cha", "mẹ", "phụ", "mẫu", "xuất thân", "gia đình", "tộc"]):
            print(f"Subtask {r[0]}: {line}")
