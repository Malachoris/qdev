import argparse
from pathlib import Path
import re

# current_file = Path("C:\git_repos\qdev\config\input.txt")
# lines = current_file.read_text(encoding="UTF-8").splitlines()
# for index, line in enumerate(lines):
#     print(index, line)

current = Path(__file__)  # C:\git_repos\qdev\main.py
current = Path.home()  # C:\Users\lukas.smicys
current = Path.cwd()  # C:\git_repos\qdev
current = Path.cwd().parent  # C:\git_repos
current = Path.cwd().parents[1]  # C:\
print(f"# {current}")


def search_for_pattern(arg: argparse.Namespace):
    current_path = arg.file_path
    pattern = arg.pattern

    with open(current_path, mode="r", encoding="UTF-8") as file:
        for index, line in enumerate(file):
            if pattern in line:
                print(index, line)

    if arg.ignore_case:
        print("ignore case")

    if arg.recursive:
        print("recursive")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find pattern in files")
    parser.add_argument('file_path', type=Path, )  # positional argument
    parser.add_argument('pattern', type=str)  # positional argument
    # parser.add_argument('-E', '--extended_regex')
    # parser.add_argument('-A', '--after_context')
    # parser.add_argument('-B', '--before_context')
    # parser.add_argument('-C', '--context')
    parser.add_argument('-i', '--ignore_case',
                        action='store_true')  # on/off flag
    # parser.add_argument('-c', '--count',
    #                     action='store_true')  # on/off flag
    # parser.add_argument('-n', '--line_number',
    #                     action='store_true')  # on/off flag
    parser.add_argument('-r', '--recursive',
                        action='store_true')  # on/off flag

    args = parser.parse_args()
    print(args.file_path, args.pattern)
    search_for_pattern(args)
