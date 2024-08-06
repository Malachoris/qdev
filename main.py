import argparse
from pathlib import Path
import re

pattern = "Simple"

current = Path(__file__)  # C:\git_repos\qdev\main.py
current = Path.home()  # C:\Users\lukas.smicys
current = Path.cwd()  # C:\git_repos\qdev
current = Path.cwd().parent  # C:\git_repos
current = Path.cwd().parents[1]  # C:\
current = Path()  # .
current = Path(".")  # .
current = Path("C:\\Users\\lukas.smicys\\Desktop\\My first py")  # **\*.py

print(f"# {current}")

current.iterdir()


# for file in current.rglob("*"):
#     print(file)


def find_pattern_by_line(file, pattern, case_sensitive=True):
    with open(file, "r", encoding="UTF-8") as f:
        lines = f.readlines()
        for index, line in enumerate(lines):
            if case_sensitive:
                if pattern in line:
                    print(index, line)
            else:
                if pattern.lower() in line.lower():
                    print(index, line)


path_pattern = "*.txt"
current_path = Path()
pattern = "Simple"

for file in current_path.rglob(
        path_pattern):  # Looking for pattern in files level
    print(file)
    find_pattern_by_line(file, pattern)


def search_for_pattern(arg: argparse.Namespace):
    current_path: Path = arg.file_path
    pattern = arg.pattern

    if current_path.is_dir():
        for item in current_path.iterdir():
            if item.is_file():
                find_pattern_by_line(item, pattern)
            else:
                print(f"We dont go deeper try adding -r flag to cmd")

    elif current_path.is_file():
        find_pattern_by_line(current_path, pattern)

    else:
        print(f"We dont know what it is, better dont touch.")
        return

    if arg.ignore_case:
        print("ignore case")

    if arg.recursive:
        for file in current_path.rglob("*"):
            find_pattern_by_line(file, pattern)


# Path can be dir. Then we search in dir, how to apply case_sensitive.

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
