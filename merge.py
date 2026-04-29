from pathlib import Path

OUTPUT_FILE = 'manuscript.md'

def merge_md_files():
    # 收集当前目录所有md文件，排除输出文件本身
    files = sorted(
        [f for f in Path('.').glob('*.md') if f.stem.isdigit()],
        key=lambda f: f.name
    )

    if not files:
        print("当前目录没有找到任何md文件")
        return

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as out:
        for f in files:
            print(f"合并：{f.name}")
            out.write(f"# {int(f.stem)}\n\n")
            out.write(f.read_text(encoding='utf-8'))
            out.write('\n\n')

    print(f"\n完成，已输出到：{OUTPUT_FILE}")

if __name__ == '__main__':
    merge_md_files()