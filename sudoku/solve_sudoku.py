from typing import List

__all__ = ["solve_sudoku"]


def solve_sudoku(puzzle: List[List[int]]) -> bool:
    """
    Solves a sudoku puzzle using backtracking.

    Args:
    - puzzle (List[List[int]]): a 9x9 matrix representing the sudoku puzzle, where 0 represents an empty cell.

    Returns:
    - bool: True if the puzzle is solved, False otherwise.
    """
    # Find an empty cell in the puzzle
    row, col = find_empty_cell(puzzle)

    # If there are no empty cells, the puzzle is solved
    if row is None:
        return True

    # Try each number from 1 to 9 in the empty cell
    for num in range(1, 10):
        if is_valid(puzzle, row, col, num):
            # If the number is valid, set it in the puzzle
            puzzle[row][col] = num

            # Move to the next empty cell and repeat
            if solve_sudoku(puzzle):
                return True

            # If we reach this point, the current number didn't work
            # Backtrack by resetting the cell to 0 and trying the next number
            puzzle[row][col] = 0

    # If we've tried all numbers and none worked, backtrack further
    return False


def find_empty_cell(puzzle):
    """
    Finds the next empty cell in the puzzle.
    Returns a tuple (row, col) representing the cell, or (None, None) if there are no empty cells.
    """
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                return row, col
    return None, None


def is_valid(puzzle, row, col, num):
    """
    Checks if a number is valid in a given cell.
    Returns True if the number is valid, False otherwise.
    """
    # Check row
    if num in puzzle[row]:
        return False

    # Check column
    if num in [puzzle[i][col] for i in range(9)]:
        return False

    # Check 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    if num in [
        puzzle[i][j]
        for i in range(box_row, box_row + 3)
        for j in range(box_col, box_col + 3)
    ]:
        return False

    # If we've passed all checks, the number is valid
    return True


if __name__ == "__main__":
    from check_solution import is_valid_solution, print_solution

    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    solve_sudoku(puzzle)
    print(is_valid_solution(puzzle))
    print_solution(puzzle)

    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 8],  # Invalid entry in last row
    ]
    solve_sudoku(puzzle)
    print(is_valid_solution(puzzle))
    print_solution(puzzle)
