import numpy as np
from typing import Union, Tuple

sudoku = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
])


def sudoku_solver(sudoku: np.array) -> np.array:
    """
    Solves a given Sudoku puzzle using the Backtracking algorithm.

    Args:
        sudoku(np.array): A 9x9 NumPy array representing the Sudoku puzzle.

    Returns:
        np.array: The solved Sudoku puzzle. If no solution is found, returns a grid filled with -1 values.
    """
    if solver_agent(sudoku):
        finalcheck = check_allcell(sudoku)
        if finalcheck:
            return sudoku
        else:
            for i in range(len(sudoku)):
                for j in range(len(sudoku[0])):
                    sudoku[i][j] = -1
            return sudoku
    else:
        for i in range(len(sudoku)):
            for j in range(len(sudoku[0])):
                sudoku[i][j] = -1
        return sudoku


def solver_agent(sudoku: np.array) -> bool:
    """
    Recursive function that solves the Sudoku puzzle using backtracking.

    Args:
        sudoku (np.array): A 9x9 NumPy array representing the Sudoku puzzle.

    Returns:
        bool: True if the Sudoku is solved, False otherwise.
    """
    emptycell = get_emptycell(sudoku)
    if emptycell is None:
        return True
    else:
        row, column = emptycell
        for num in range(1, 10):
            if check_validnumber(sudoku, num, (row, column)):
                sudoku[row][column] = num

                if solver_agent(sudoku):
                    return True
                sudoku[row][column] = 0
    return False


def get_emptycell(sudoku: np.array) -> Union[Tuple[int, int], None]:
    """
    Finds the first empty cell in the Sudoku grid.

    Args:
        sudoku (np.array): A 9x9 NumPy array representing the Sudoku puzzle.

    Returns:
        Tuple[int, int]: The row and column of the empty cell.
        None: If no empty cell is found.
    """
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return (i, j)
    return None


def check_validnumber(sudoku: np.array, number: int, position: Tuple[int, int]) -> bool:
    """
    Checks if the given number is valid at the specified position.

    Args:
        sudoku (np.array): A 9x9 NumPy array representing the Sudoku puzzle.
        number (int): The number to check for validity.
        position (Tuple[int, int]): A tuple containing the row and column of the cell to check.

    Returns:
        bool: True if the number is valid, False otherwise.
    """
    for i in range(len(sudoku[0])):
        if sudoku[position[0]][i] == number:
            return False

    for i in range(len(sudoku)):
        if sudoku[i][position[1]] == number:
            return False

    box_row = position[0]//3
    box_column = position[1]//3

    for i in range(box_row*3, box_row*3+3):
        for j in range(box_column*3, box_column*3+3):
            if sudoku[i][j] == number:
                return False
    return True


def check_allcell(sudoku: np.array) -> bool:
    """
    Validates if the solved Sudoku grid has unique numbers in each row, column, and 3x3 box.

    Args:
        sudoku (np.array): A 9x9 NumPy array representing the solved Sudoku puzzle.

    Returns:
        bool: True if the Sudoku grid is valid, False otherwise.
    """
    existrow = []
    row = 0
    while row < 9:
        for i in range(len(sudoku[0])):
            number = sudoku[row][i]
            if number in existrow:
                return False
            else:
                existrow.append(number)
        existrow.clear()
        row += 1

    existcolumn = []
    column = 0
    while column < 9:
        for i in range(len(sudoku)):
            number = sudoku[i][column]
            if number in existcolumn:
                return False
            else:
                existcolumn.append(number)
        existcolumn.clear()
        column += 1

    existbox = []
    rowbox = len(sudoku)//3
    columnbox = len(sudoku[0])//3
    for r in range(rowbox):
        for c in range(columnbox):
            for i in range(r*3, r*3+3):
                for j in range(c*3, c*3+3):
                    number = sudoku[i][j]
                    if number in existbox:
                        return False
                    else:
                        existbox.append(number)
            existbox.clear()
    return True


print(sudoku_solver(sudoku))
