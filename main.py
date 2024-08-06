import argparse
from pathlib import Path
import re


def find_pattern_by_line(file: Path, pattern, ignore_case=False):
    try:
        lines = file.read_text(encoding="UTF-8").splitlines()
    except UnicodeDecodeError:
        return
    for index, line in enumerate(lines):
        if not ignore_case:
            match = re.search(pattern, line)
            if match:
                print(index, line)
        else:
            match = re.search(pattern.lower(), line.lower())
            if match:
                print(index, line)


path_pattern = "*.txt"
current_path = Path()
pattern = "Simple"
recursive = True
ignore_case = True

search_func = current_path.glob("*")
if recursive:
    search_func = current_path.rglob("*")

if current_path.is_dir():
    for item in search_func:
        if item.is_file():
            find_pattern_by_line(item, pattern, ignore_case)

elif current_path.is_file():
    find_pattern_by_line(current_path, pattern, ignore_case)
else:
    print(f"We dont know what it is, better dont touch.")


def search_for_pattern(arg: argparse.Namespace):
    current_path = arg.file_path
    pattern = arg.pattern
    count = 0

    search_func = current_path.glob("*")
    if args.recursive:
        search_func = current_path.rglob("*")

    if args.extended_re:
        pattern = args.extended_re

    if current_path.is_dir():
        for item in search_func:
            if item.is_file():
                find_pattern_by_line(item, pattern, arg.ignore_case)

    elif current_path.is_file():
        find_pattern_by_line(current_path, pattern, arg.ignore_case)

    else:
        print(f"We dont know what it is, better dont touch.")
        return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find pattern in files")
    parser.add_argument('file_path', type=Path, )  # positional argument
    parser.add_argument('pattern', type=str)  # positional argument
    # on/off flag action='store_true'
    parser.add_argument('-E', '--extended_re', type=str)
    parser.add_argument('-A', '--after_context', type=int)
    parser.add_argument('-B', '--before_context', type=int)
    parser.add_argument('-C', '--context', type=int)
    parser.add_argument('-i', '--ignore_case', action='store_true')
    parser.add_argument('-c', '--count', action='store_true')
    parser.add_argument('-n', '--line_number', action='store_true')
    parser.add_argument('-r', '--recursive', action='store_true')

    args = parser.parse_args()
    print(args.file_path, args.pattern)
    search_for_pattern(args)
