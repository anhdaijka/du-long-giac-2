import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('story_database.sqlite3')
cur = conn.cursor()

print("=== DIALOGUES WITH BẠCH THU LÂM (Thu Di) ===")
cur.execute("""
    SELECT d.sub_id, s.name, d.phase, d.cleaned_text 
    FROM dialogues d 
    JOIN subtasks s ON d.sub_id = s.sub_id 
    WHERE d.cleaned_text LIKE '%Thu Di%' OR d.cleaned_text LIKE '%Bạch Thu Lâm%' 
    LIMIT 20
""")
for r in cur.fetchall():
    print(f"\n[Subtask {r[0]}: {r[1]} - Phase {r[2]}]")
    print(r[3][:400])

conn.close()
