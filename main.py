#!/usr/bin/env python3
import os
import hashlib

LINE = "I asked my smart speaker to help me fall asleep, so it read me my unread emails."

def main():
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'entry.txt')

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(LINE)

    char_count = len(LINE)
    sha256 = hashlib.sha256(LINE.encode('utf-8')).hexdigest()
    print(f"chars: {char_count}")
    print(f"sha256: {sha256}")

if __name__ == '__main__':
    main()