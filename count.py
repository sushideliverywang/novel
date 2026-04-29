import re
import sys
from pathlib import Path

def count_chinese(text):
    return len(re.findall(r'[\u4e00-\u9fff]', text))

def count_files(paths):
    total = 0
    for path in paths:
        p = Path(path)
        if p.is_dir():
            files = list(p.glob('**/*.md'))
        else:
            files = [p]

        files = sorted(
            [f for f in files if f.stem.isdigit()],
            key=lambda f: f.name
        )

        for f in files:
            text = f.read_text(encoding='utf-8')
            count = count_chinese(text)
            print(f"{f}: {count:,} 字")
            total += count

    print(f"\n合计：{total:,} 字")

if __name__ == '__main__':
    paths = sys.argv[1:] or ['.']
    count_files(paths)
