import argparse
from pathlib import Path
import re


class Grep:
    def __init__(self, args: argparse.Namespace):
        self.file_path: Path = args.file_path
        self.pattern: str = args.pattern
        self.regex: str = args.regex
        self.ignore_case: bool = args.ignore_case
        self.count: bool = args.count
        self.line_nr: bool = args.line_number
        self.recursive: bool = args.recursive
        self.after_context: int = args.after_context
        self.before_context: int = args.before_context
        self.context: int = args.context
        self.exclude: str = args.exclude
        self.include: str = args.include
        self.patt_count = 0
        self.glob_pattern = "*"

    def read_file_by_line(self, file):
        lines = None
        try:
            lines = file.read_text(encoding="UTF-8").splitlines()
        except UnicodeDecodeError:
            return lines

    def find_pattern_in_line(self, pattern: str, lines: list):
        for index, line in enumerate(lines):

            match = self.use_pure_str(self.ignore_case, pattern, line)

            if self.regex:
                match = self.use_regex(self.ignore_case, pattern, line)

            if match:
                self.patt_count += 1 if self.count else self.patt_count
                print((index, line) if self.line_nr else line)

    def use_regex(self, ignore_case: bool, pattern: str, line: str):
        match = re.search(pattern, line)
        if ignore_case:
            match = re.search(pattern, line, flags=re.IGNORECASE)
        if match:
            return line
        return

    def use_pure_str(self, ignore_case: bool, pattern: str, line: str):
        match = pattern in line
        if ignore_case:
            match = pattern.lower() in line.lower()
        if match:
            return line
        return None

    # def get_all_files(self):
    #     searched_files = self.file_path.glob
    #     if self.recursive:
    #         searched_files = self.file_path.rglob
    #     return searched_files

    def context_thingies(self, lines_to_contxt: int):
        if self.after_context:
            # TODO: args.before.extend(lines[max(index+3, len(lines):index])
            pass
        elif self.before_context:
            # TODO: args.before.extend(lines[max(index-3, 0):index])
            pass
        elif self.context:
            pass

    def exclude_glob_pattern(self, path_dir: Path, pattern: str) -> list:
        dir_content = [path for path in path_dir.parent.glob('*') if
                      pattern not in path.stem]
        return dir_content

    def process_directory(self):
        if not self.file_path.exists():
            raise Exception("Bad dir")

        searched_files = self.file_path.glob
        if self.recursive:
            searched_files = self.file_path.rglob

        if self.include:
            self.glob_pattern = self.include

        elif self.exclude:
            self.glob_pattern = "!"+self.exclude

        for item in searched_files(self.glob_pattern):
            line_lst = self.read_file_by_line(item)
            self.find_pattern_in_line(self.pattern, line_lst)

        if self.count:
            print(self.patt_count)
