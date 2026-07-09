#!/usr/bin/python3
"""Module that computes the perimeter of an island."""


def island_perimeter(grid):
    """Calculate the perimeter of an island in a grid.

    Args:
        grid: A 2D list where 1 represents land and 0 represents water.

    Returns:
        The perimeter of the island.
    """
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                if row == len(grid) - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                if col == len(grid[row]) - 1 or grid[row][col + 1] == 0:
                    perimeter += 1
    return perimeter
