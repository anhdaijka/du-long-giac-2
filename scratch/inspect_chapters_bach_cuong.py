import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

chapters_dir = r"d:\Games\Server Client\Server KT\Kiếm Thế 2\Server\du-long-giac-2\chapters"

for f in sorted(os.listdir(chapters_dir)):
    if f.endswith(".md") and not f.startswith("archive"):
        fpath = os.path.join(chapters_dir, f)
        with open(fpath, "r", encoding="utf-8") as file:
            lines = file.readlines()
        
        matches = []
        for i, line in enumerate(lines):
            if any(k in line for k in ["Bạch Cương", "bức thư máu", "Đức Khoái", "Hán Thủy Cổ Độ"]):
                matches.append(i)
        
        if matches:
            print(f"\n{'='*30} {f} ({len(matches)} matches) {'='*30}")
            for m in matches:
                start = max(0, m - 2)
                end = min(len(lines), m + 3)
                print(f"--- Line {m+1} ---")
                for j in range(start, end):
                    print(f"  {j+1}: {lines[j].strip()}")
