from typing import List

__all__ = ["import_puzzle_file"]


def parse_line(line: str) -> List[int]:
    """Split a line of text into a list of integers."""
    line = line.strip()
    if len(line) == 9:
        return [int(c) for c in line]
    else:
        for split_char in [" ", "\t", ",", ".", ";", ":"]:
            ret = [int(c) for c in line.split(split_char)]
            if len(ret) == 9:
                return ret
    raise ValueError("Invalid puzzle file")


def import_puzzle_file(puzzle_file: str):
    """Import a puzzle from a file."""
    with open(puzzle_file, "r") as f:
        puzzle = [[int(c) for c in parse_line(line)] for line in f]
    return puzzle
