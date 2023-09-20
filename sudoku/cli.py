import argparse
from sudoku import solve_sudoku, print_solution

USAGE = R"""%(prog)s [options] <puzzle_file>

The sudoku command takes a single positional argument, which is the path to a file containing a Sudoku puzzle. The puzzle file should be a text file containing 9 lines, each with 9 digits separated by spaces. Empty cells should be represented by zeros. Here's an example puzzle file:
        
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

"""


def split_line(line: str):
    for split_char in [" ", "\t", ",", "."]:
        ret = [int(c) for c in line.strip().split(" ")]
        if len(ret) == 9:
            return ret
    raise ValueError("Invalid puzzle file")


def main():
    parser = argparse.ArgumentParser(
        description="Solve a Sudoku puzzle",
        usage=USAGE,
    )
    parser.add_argument("puzzle_file", type=str, help="Path to the puzzle file")
    args = parser.parse_args()

    with open(args.puzzle_file, "r") as f:
        puzzle = [[int(c) for c in split_line(line)] for line in f]

    if solve_sudoku(puzzle):
        print_solution(puzzle)
    else:
        print("Unable to solve puzzle")


if __name__ == "__main__":
    main()
