import argparse
import time
from pathlib import Path
import re
from typing import Generator


def find_pattern_by_line(file: Path, pattern: str, ignore_case=False,
                         line_nr=False, extend_re=False):
    count = 0
    try:
        lines = file.read_text(encoding="UTF-8").splitlines()
    except UnicodeDecodeError:
        return count

    for index, line in enumerate(lines):
        match = pattern in line

        if ignore_case:
            match = pattern.lower() in line.lower()

        if extend_re:
            match = re.search(pattern, line)

            if ignore_case:
                match = re.search(pattern, line, flags=re.IGNORECASE)

        if match:
            count += 1
            print((index, line) if line_nr else line)

    return count


# current_path = Path(".")
# pattern = "simple"  # "^def\s" "simple"
# recursive = True
# ignore_case = True
# line_number = False
# regex = True
# count_arg = True
#
# count = 0
#
# search_level = current_path.glob("*")
# if recursive:
#     search_level = current_path.rglob("*")
#
# if ignore_case:
#     pattern = pattern.lower()
#
# if current_path.is_dir():
#     for item in search_level:
#         if item.is_file():
#             count += find_pattern_by_line(item, pattern, ignore_case,
#                                           line_number, regex)
#
# elif current_path.is_file():
#     count += find_pattern_by_line(current_path, pattern, ignore_case,
#                                   line_number, regex)
#
# else:
#     print(f"We dont know what it is, better dont touch.")
#
# if count_arg:
#     print(f"Number of rows where pattern repeats is {count}")


def search_for_pattern(args: argparse.Namespace):
    current_path = args.file_path
    pattern = args.pattern
    count = 0

    # TODO: this bellow
    if not current_path.exists():
        raise Exception("Bad dir")

    # TODO: when finished actual operation exit -> return
    # TODO: add more defs and a class.
    # TODO: args.before.extend(lines[max(index-3, 0):index])
    # TODO: args.before.extend(lines[max(index+3, len(lines):index])

    searched_files = current_path.glob
    if args.recursive:
        searched_files = current_path.rglob

    if current_path.is_dir():
        for item in searched_files("*"):
            if item.is_file():
                count += find_pattern_by_line(item, pattern,
                                              args.ignore_case,
                                              args.line_number,
                                              args.regex)
                return

    elif current_path.is_file():
        count += find_pattern_by_line(current_path, pattern,
                                      args.ignore_case,
                                      args.line_number,
                                      args.regex)
        return

    else:
        print(f"We dont know what it is, better dont touch.")
        return

    if args.count:
        print(f"Number of rows where pattern repeats is {count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find pattern in files")
    parser.add_argument('file_path', type=Path, )  # positional argument
    parser.add_argument('pattern', type=str)  # positional argument
    parser.add_argument('-E', '--regex', action='store_true')
    parser.add_argument('-i', '--ignore_case', action='store_true')
    parser.add_argument('-c', '--count', action='store_true')
    parser.add_argument('-n', '--line_number', action='store_true')
    parser.add_argument('-r', '--recursive', action='store_true')
    parser.add_argument('-A', '--after_context', type=int, default=3)
    parser.add_argument('-B', '--before_context', type=int, default=3)
    parser.add_argument('-C', '--context', type=int, default=3)
    parser.add_argument('-exclude', type=str)
    parser.add_argument('-include', type=str)

    args = parser.parse_args()
    # print(args.file_path, args.pattern, args.exclude)
    search_for_pattern(args)
