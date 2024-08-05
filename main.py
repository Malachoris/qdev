import argparse

from grep_actions.count import Count


def find_pattern_in_file(file_path, pattern=None):
    with open(file_path, mode="r", encoding="UTF-8") as file:
        lines = file.readlines()
        for line in lines:
            if pattern in line:
                print(line)


if __name__ == "__main__":

    file_path = "C:\git_repos\qdev\config\input.txt"
    find_pattern_in_file(file_path, "Simple")

    parser = argparse.ArgumentParser()

    # parser.add_argument('-f', '--foo', action=Count)
    # parser.add_argument('bar', action=Count)

    parser.add_argument('file_path')  # positional argument
    parser.add_argument('pattern')  # positional argument
    parser.add_argument('-c', '--count')  # option that takes a value
    parser.add_argument('-v', '--verbose',
                        action='store_true')  # on/off flag

    args = parser.parse_args()
    print(args.file_path, args.count, args.verbose)

    find_pattern_in_file(args.file_path, args.pattern)
