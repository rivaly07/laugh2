#!/usr/bin/env python3
import os
import tempfile
import subprocess
import sys

def run_main(output_dir):
    env = os.environ.copy()
    env['MAKEFUN_OUTPUT_DIR'] = output_dir
    result = subprocess.run([sys.executable, 'main.py'], capture_output=True, text=True, env=env, cwd=os.path.dirname(os.path.abspath(__file__)))
    if result.returncode != 0:
        print(f"main.py failed: {result.stderr}")
        sys.exit(1)
    output_path = os.path.join(output_dir, 'entry.txt')
    with open(output_path, 'rb') as f:
        content = f.read()
    return content, result.stdout.strip()

def main():
    with tempfile.TemporaryDirectory() as dir1, tempfile.TemporaryDirectory() as dir2:
        content1, out1 = run_main(dir1)
        content2, out2 = run_main(dir2)

        if content1 != content2:
            print("FAIL: outputs are not byte-identical")
            sys.exit(1)

        text = content1.decode('utf-8')
        char_count = len(text)

        if not (1 <= char_count <= 200):
            print(f"FAIL: character count {char_count} not in 1..200")
            sys.exit(1)

        if text.strip() == '':
            print("FAIL: output is only whitespace")
            sys.exit(1)

        if '\n' in text:
            print("FAIL: output contains newline")
            sys.exit(1)

        print("PASS: byte-identical")
        print(f"PASS: character count {char_count} in 1..200")
        print("PASS: not only whitespace")
        print("PASS: single line (no newline)")
        print(out1)

if __name__ == '__main__':
    main()