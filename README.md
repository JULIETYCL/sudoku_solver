# Sudoku Solver

This program is an implementation of a Sudoku solver using the Backtracking algorithm. It takes a Sudoku puzzle as input and returns the solved puzzle.

## Getting Started

To use the Sudoku solver, first import the necessary libraries:
import numpy as np

Next, define your Sudoku puzzle as a numpy array:
```
sudoku = np.array([
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9],
])
```

Then, call the `sudoku_solver` function with the sudoku puzzle as its argument:

`print(sudoku_solver(sudoku))`

## Algorithm
The Sudoku solver uses the Backtracking algorithm to find a solution for the given Sudoku puzzle. The algorithm starts at the first empty cell and tries to fill it with numbers from 1 to 9. If a valid number is found for the current cell, the algorithm moves to the next empty cell and repeats the process. If no valid number is found for a cell, the algorithm backtracks to the previous cell and tries a different number.

The program includes the following functions:

`sudoku_solver(sudoku)`: This function solves the Sudoku puzzle and returns the solution. If no solution is found, it returns a grid filled with -1 values.
`solver_agent(sudoku)`: This function is the main backtracking algorithm. It finds an empty cell and tries to fill it with a valid number. If successful, it calls itself recursively until the puzzle is solved.
`get_emptycell(sudoku)`: This function returns the row and column indices of the first empty cell in the grid. If there are no empty cells, it returns None.
`check_validnumber(sudoku, number, position)`: This function checks if the given number is a valid candidate for the specified position in the grid. It checks the row, column, and 3x3 box constraints and returns True if the number is valid, False otherwise.
`check_allcell(sudoku)`: This function checks the solution's validity by ensuring that there are no duplicate numbers in any row, column, or 3x3 box. It returns True if the solution is valid, False otherwise.

## Example

Here's an example of how to use the Sudoku solver:
```
import numpy as np

sudoku = np.array([
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9],
])
```
Call the sudoku_solver function and print the solution

```
solution = sudoku_solver(sudoku)
print(solution)
```

The output will be the solved Sudoku puzzle:
```
	[[5 3 4 6 7 8 9 1 2]
	[6 7 2 1 9 5 3 4 8]
	[1 9 8 3 4 2 5 6 7]
	[8 5 9 7 6 1 4 2 3]
	[4 2 6 8 5 3 7 9 1]
	[7 1 3 9 2 4 8 5 6]
	[9 6 1 5 3 7 2 8 4]
	[2 8 7 4 1 9 6 3 5]
	[3 4 5 2 8 6 1 7 9]]
```
This output represents the completed Sudoku puzzle with all the constraints satisfied.

