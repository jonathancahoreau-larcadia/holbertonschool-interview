#!/usr/bin/python3
"""Module for rotating a square 2D matrix."""


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list[list[int]]): An n x n 2D matrix to be rotated.

    Returns:
        None: The matrix is modified in-place.
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in matrix:
        i.reverse()
