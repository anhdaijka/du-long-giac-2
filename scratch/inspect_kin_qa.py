import sys

sys.stdout.reconfigure(encoding='utf-8')

filepath = r"d:\Games\Server Client\Server KT\Kiếm Thế 2\Server\Docker_KT2\Kiemthe2-server\gamecenter\setting\event\kinquestions.txt"

with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

print(f"Total lines in kinquestions.txt: {len(lines)}")
for i, line in enumerate(lines):
    if any(k in line for k in ["Bạch Thu Lâm", "Thu Di", "Bạch Cương", "Tiêu", "Dương Anh"]):
        print(f"Line {i+1}: {line.strip()}")
