from typing import List, Optional
import rich
import rich.console

__all__ = ["is_entry_valid", "is_valid_solution", "print_solution"]


def is_entry_valid(
    sudoku: List[List[int]], i: int, j: int, val: Optional[int] = None
) -> bool:
    """
    Check if a given value is valid for a given position in a Sudoku puzzle.

    Args:
        sudoku (List[List[int]]): A 9x9 Sudoku puzzle represented as a list of lists.
        i (int): The row index of the position to check.
        j (int): The column index of the position to check.
        val (Optional[int]): The value to check. If None, the value at the given position is used.

    Returns:
        bool: True if the value is valid for the given position, False otherwise.
    """
    if val is None:
        val = sudoku[i][j]

    if val < 1 or val > 9:
        return False

    # Check row
    if val in [sudoku[i][k] for k in range(9) if k != j]:
        return False

    # Check column
    if val in [sudoku[k][j] for k in range(9) if k != i]:
        return False

    # Check 3x3 box
    box_i = (i // 3) * 3
    box_j = (j // 3) * 3
    if val in [
        sudoku[box_i + m][box_j + n]
        for m in range(3)
        for n in range(3)
        if box_i + m != i and box_j + n != j
    ]:
        return False

    return True


def is_valid_solution(sudoku: List[List[int]]) -> bool:
    """
    Check if a given sudoku solution is valid.

    Args:
        sudoku: A 9x9 matrix representing the sudoku solution.

    Returns:
        True if the solution is valid, False otherwise.
    """
    # Check rows
    for row in sudoku:
        if sorted(row) != list(range(1, 10)):
            return False

    # Check columns
    for column in zip(*sudoku):
        if sorted(column) != list(range(1, 10)):
            return False

    # Check boxes
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = [sudoku[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if sorted(box) != list(range(1, 10)):
                return False

    return True


def print_solution(sudoku: List[List[int]]) -> None:
    """
    Print a sudoku solution in colored text.
    print contradiction values in red, else print the number in green.

    Args:
        sudoku: A 9x9 matrix representing the sudoku solution.

    Returns:
        None
    """
    console = rich.console.Console()
    for i, row in enumerate(sudoku):
        if i % 3 == 0 and i != 0:
            console.print("-" * 21)
        for j, val in enumerate(row):
            if j % 3 == 0 and j != 0:
                console.print("| ", end="")
            if val == 0:
                console.print(f"[blue]{val}[/blue] ", end="")
            elif not is_entry_valid(sudoku, i, j):
                console.print(f"[red]{val}[/red] ", end="")
            else:
                console.print(f"[green]{val}[/green] ", end="")
        console.print()


if __name__ == "__main__":
    # Example usage

    # invalid solution
    puzzle = [
        [9, 8, 7, 3, 6, 1, 2, 5, 4],
        [3, 5, 1, 9, 2, 4, 8, 6, 7],
        [4, 2, 6, 8, 7, 5, 3, 9, 1],
        [8, 7, 3, 2, 1, 6, 4, 1, 5],
        [1, 6, 2, 7, 5, 9, 6, 4, 3],
        [5, 9, 6, 4, 8, 3, 7, 1, 2],
        [7, 4, 5, 1, 9, 8, 6, 3, 2],
        [2, 3, 9, 6, 4, 7, 1, 8, 5],
        [6, 1, 8, 5, 3, 2, 9, 7, 4],
    ]
    result = is_valid_solution(puzzle)
    print(result)  # will print True
    print_solution(puzzle)

    print()

    # valid solution
    puzzle = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ]
    result = is_valid_solution(puzzle)
    print(result)
    print_solution(puzzle)
