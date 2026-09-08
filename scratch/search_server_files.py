import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"d:\Games\Server Client\Server KT\Kiếm Thế 2\Server"

def search_files(search_terms, extensions=['.lua', '.txt', '.xml', '.tab']):
    results = {term: [] for term in search_terms}
    for root, dirs, files in os.walk(base_dir):
        # skip git or repo du-long-giac-2 to search purely in game server
        if "du-long-giac-2" in root:
            continue
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        for term in search_terms:
                            if term in content:
                                results[term].append(filepath)
                except Exception as e:
                    pass
    return results

terms = ["Bạch Thu Lâm", "Bạch Cương", "白秋琳", "白刚", "白罡", "秋姨", "Bạch Di", "Bạch Doanh Doanh", "Bạch Hiên Viên"]
res = search_files(terms)
for term, files in res.items():
    print(f"Term '{term}': found in {len(files)} files")
    for f in files[:5]:
        print(f"  {f}")
