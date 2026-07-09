#!/usr/bin/python3


def island_perimeter(grid):
    """Calculate the perimeter of an island in a grid.

    Args:
        grid: A 2D list where 1 represents land and 0 represents water.

    Returns:
        The perimeter of the island.
    """
    perimeter = 0
    for row in range(1, len(grid)):
        for col in range(1, len(grid[row])):
            if grid[row][col] == 1:
                if grid[row - 1][col] == 0:
                    perimeter += 1
                if grid[row + 1][col] == 0:
                    perimeter += 1
                if grid[row][col + 1] == 0:
                    perimeter += 1
                if grid[row][col - 1] == 0:
                    perimeter += 1
    return perimeter
