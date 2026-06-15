#!/usr/bin/python3
"""N-Queens solver using backtracking algorithm.

This module solves the N-Queens problem by finding all valid placements
of N queens on an N×N chessboard such that no two queens attack each other.
"""

import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)


def check_placement(row, col, positions):
    """Check if a queen can be safely placed at the given position.

    Args:
        row: The row index where the queen would be placed.
        col: The column index where the queen would be placed.
        positions: List of [row, col] positions of already placed queens.

    Returns:
        True if the queen can be placed safely, False otherwise.
    """
    for position in positions:
        if col == (position[1]):
            return False

        if abs(row - position[0]) == abs(col - position[1]):
            return False
    return True


def search_placement(positions):
    """Recursively search for valid queen placements using backtracking.

    Args:
        positions: List of [row, col] positions of already placed queens.

    When a valid complete solution is found (N queens placed), it prints
    the positions and continues searching for other solutions.
    """
    if len(positions) == N:
        print(positions)
        return
    row = len(positions)
    for col in range(N):
        if check_placement(row, col, positions):
            positions.append([row, col])
            search_placement(positions)
            positions.pop()


positions = []
search_placement(positions)
