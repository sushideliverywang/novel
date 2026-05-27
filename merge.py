import os
from pathlib import Path
from datetime import date

OUTPUT_FILE = 'manuscript.md'

today = date.today().strftime('%Y%m%d')
OUTPUT_EPUB = f'manuscript_{today}.epub'

def process_content(text):
    """每行独立成段，原始空行替换为分隔线"""
    lines = text.splitlines()
    new_lines = []
    for i, line in enumerate(lines):
        current = line.strip()
        next_line = lines[i + 1].strip() if i + 1 < len(lines) else ''

        if not current:
            new_lines.append('')
            new_lines.append('---')
            new_lines.append('')
        else:
            new_lines.append(line)
            if next_line and next_line != '---':
                new_lines.append('')

    return '\n'.join(new_lines)

def merge_md_files():
    files = sorted(
        [f for f in Path('.').glob('*.md') if f.stem.isdigit()],
        key=lambda f: int(f.stem)
    )

    if not files:
        print("当前目录没有找到任何md文件")
        return

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as out:
        for f in files:
            n = int(f.stem)
            print(f"合并：{f.name} → 第{n}章")
            out.write(f"# 第{n}章\n\n")
            content = f.read_text(encoding='utf-8')
            out.write(process_content(content))
            out.write('\n\n')

    print(f"\n完成，已输出到：{OUTPUT_FILE}")

def build_epub():
    cmd = (
        f'pandoc {OUTPUT_FILE} '
        f'-o {OUTPUT_EPUB} '
        f'--metadata title="走线阿拉斯加" '
        f'--metadata author="王轶群" '
        f'--metadata lang="zh-CN" '
        f'--toc '
        f'--toc-depth=1 '
        f'--css=style.css'
    )
    print("\n正在生成epub...")
    result = os.system(cmd)
    if result == 0:
        print(f"完成，已输出到：{OUTPUT_EPUB}")
    else:
        print("epub生成失败，请检查pandoc命令")

if __name__ == '__main__':
    merge_md_files()
    build_epub()