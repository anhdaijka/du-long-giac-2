import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('chapters/chapter_04b.md', 'r', encoding='utf-8') as f:
    for i, l in enumerate(f):
        if 'bà' in l.lower():
            print(f'{i+1}: {l.strip()}')
