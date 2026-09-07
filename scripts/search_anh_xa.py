import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')
conn = sqlite3.connect('story_database.sqlite3')
cur = conn.cursor()

print("=== SEARCH FOR 'Ảnh Xã' ===")
tables = [
    ('tasks', ['name', 'describe_cleaned']),
    ('subtasks', ['name', 'describe_cleaned']),
    ('dialogues', ['cleaned_text']),
    ('armycamp_lore', ['camp_name', 'speaker_or_subject', 'cleaned_text']),
    ('linktask_tales', ['category_name', 'cleaned_text']),
    ('faction_primer_stories', ['cleaned_text']),
    ('feature_system_stories', ['system_name', 'subject', 'cleaned_text']),
    ('world_ambient_dialogues', ['map_name', 'cleaned_msg'])
]

found = 0
for table, cols in tables:
    for col in cols:
        query = f"SELECT rowid, {col} FROM {table} WHERE {col} LIKE '%Ảnh Xã%'"
        rows = cur.execute(query).fetchall()
        if rows:
            print(f"Table: {table}, Column: {col} -> {len(rows)} matches")
            for r in rows[:5]:
                text = r[1][:200].replace('\n', ' ')
                print(f"  [rowid {r[0]}]: {text}")
            found += len(rows)

print(f"\nTotal matches for 'Ảnh Xã': {found}")
