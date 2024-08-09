from dataclasses import dataclass


@dataclass
class SearchResult:
    line_num: int
    matched_line: str
    before_context: list[str]
    after_context: list[str]
