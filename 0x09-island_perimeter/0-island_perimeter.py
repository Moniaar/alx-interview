#!/usr/bin/python3
""" This model has the answer for the Island
Perimeter interview question"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check above
                if r == 0 or grid[r-1][c] == 0:
                    perimeter += 1
                # Check below
                if r == rows-1 or grid[r+1][c] == 0:
                    perimeter += 1
                # Check left
                if c == 0 or grid[r][c-1] == 0:
                    perimeter += 1
                # Check right
                if c == cols-1 or grid[r][c+1] == 0:
                    perimeter += 1

    return perimeter
