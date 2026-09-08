import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"d:\Games\Server Client\Server KT\Kiếm Thế 2\Server\Docker_KT2\Kiemthe2-server\gameserver\script"

print("=== SCANNING ALL SCRIPTS FOR STORY / LORE ===")

for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".lua"):
            fpath = os.path.join(root, f)
            try:
                with open(fpath, "r", encoding="utf-8", errors="ignore") as file:
                    content = file.read()
                    if any(k in content for k in ["chủ nhân", "chu nhan", "Hán Thủy", "Han Thuy", "Đức Khoái", "Duc Khoai", "Tiêu Lăng Phong", "Tieu Lang Phong", "Bạch Cương", "Bach Cuong"]):
                        print(f"File: {fpath}")
                        # print snippets
                        lines = content.splitlines()
                        for i, l in enumerate(lines):
                            if any(k in l for k in ["chủ nhân", "Hán Thủy", "Đức Khoái", "Bạch Cương", "Thu Lâm"]):
                                print(f"  L{i+1}: {l.strip()}")
            except Exception as e:
                pass
