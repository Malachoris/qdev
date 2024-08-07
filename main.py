import argparse
from pathlib import Path
import re


def find_pattern_by_line_re(file: Path, pattern, ignore_case=False,
                            line_nr=False):
    count = 0
    try:
        lines = file.read_text(encoding="UTF-8").splitlines()
    except UnicodeDecodeError:
        return count
    for index, line in enumerate(lines):
        if not ignore_case:
            match = re.search(pattern, line) # "<re.Match object; span=(11, 17), match='simple'>"
            if match and not line_nr:
                count += 1
                print(line)
            elif match and line_nr:
                count += 1
                print(index, line)
        else:
            match = re.search(pattern, line, flags=re.IGNORECASE)
            if match and not line_nr:
                count += 1
                print(line)
            elif match and line_nr:
                count += 1
                print(index, line)
    return count


def find_pattern_by_line(file: Path, pattern, ignore_case=False,
                         line_nr=False):
    count = 0
    try:
        lines = file.read_text(encoding="UTF-8").splitlines()
    except UnicodeDecodeError:
        return count
    for index, line in enumerate(lines):
        if not ignore_case:
            if pattern in line and not line_nr:
                count += 1
                print(line)
            elif pattern in line and line_nr:
                count += 1
                print(index, line)
        else:
            if pattern.lower() in line.lower() and not line_nr:
                count += 1
                print(line)
            elif pattern.lower() in line.lower() and line_nr:
                count += 1
                print(index, line)
    return count


# current_path = Path(".")
# pattern = "^def\s"  # "^def\s" "simple"
# recursive = False
# ignore_case = False
# line_number = False
# extended_re = True
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
#         if item.is_file() and extended_re:
#             count += find_pattern_by_line_re(item, pattern, ignore_case,
#                                              line_number)
#         elif item.is_file() and not extended_re:
#             count += find_pattern_by_line(item, pattern, ignore_case,
#                                           line_number)
#
# elif current_path.is_file() and extended_re:
#     count += find_pattern_by_line_re(current_path, pattern, ignore_case,
#                                      line_number)
# elif current_path.is_file() and not extended_re:
#     count += find_pattern_by_line(current_path, pattern, ignore_case,
#                                   line_number)
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

    searched_files = current_path.glob("*")
    if args.recursive:
        searched_files = current_path.rglob("*")

    # if args.extended_re:
    #     pattern = args.extended_re

    if current_path.is_dir():
        for item in searched_files:
            if item.is_file() and args.extended_re:
                count += find_pattern_by_line_re(item, pattern,
                                                 args.ignore_case,
                                                 args.line_number)
            elif item.is_file() and not args.extended_re:
                count += find_pattern_by_line(item, pattern, args.ignore_case,
                                              args.line_number)

    elif current_path.is_file() and args.extended_re:
        count += find_pattern_by_line_re(current_path, pattern,
                                         args.ignore_case, args.line_number)
    elif current_path.is_file() and not args.extended_re:
        count += find_pattern_by_line(current_path, pattern, args.ignore_case,
                                      args.line_number)

    else:
        print(f"We dont know what it is, better dont touch.")
        return

    if args.count:
        print(f"Number of rows where pattern repeats is {count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find pattern in files")
    parser.add_argument('file_path', type=Path, )  # positional argument
    parser.add_argument('pattern', type=str)  # positional argument
    # on/off flag action='store_true'
    parser.add_argument('-E', '--extended_re', action='store_true')
    parser.add_argument('-i', '--ignore_case', action='store_true')
    parser.add_argument('-c', '--count', action='store_true')
    parser.add_argument('-n', '--line_number', action='store_true')
    parser.add_argument('-r', '--recursive', action='store_true')
    # parser.add_argument('-A', '--after_context', type=int)
    # parser.add_argument('-B', '--before_context', type=int)
    # parser.add_argument('-C', '--context', type=int)
    # parser.add_argument('--exclude')
    # parser.add_argument('--include')

    args = parser.parse_args()
    # print(args.file_path, args.pattern)
    search_for_pattern(args)
