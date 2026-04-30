import re
import sys
from pathlib import Path

def count_chinese(text):
    return len(re.findall(r'[\u4e00-\u9fff]', text))

def count_files(paths):
    cumulative = 0
    for path in paths:
        p = Path(path)
        if p.is_dir():
            files = list(p.glob('**/*.md'))
        else:
            files = [p]

        files = sorted(
            [f for f in files if f.stem.isdigit()],
            key=lambda f: int(f.stem)
        )

        for f in files:
            text = f.read_text(encoding='utf-8')
            count = count_chinese(text)
            cumulative += count
            print(f"{f}: {count:,} 字，累计：{cumulative:,} 字")


if __name__ == '__main__':
    paths = sys.argv[1:] or ['.']
    count_files(paths)
