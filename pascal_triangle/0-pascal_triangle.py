#!/usr/bin/python3
"""
Module for generating Pascal's Triangle.

This module provides a function to generate Pascal's Triangle
up to a given number of rows.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Args:
        n (int): The number of rows of Pascal's Triangle
        to generate.

    Returns:
        list of lists: A list of lists of integers
        representing Pascal's Triangle.
    """
    result = []

    for i in range(n):
        row = [1]

        for j in range(1, i):
            row.append(result[i - 1][j - 1] + result[i - 1][j])

        if i > 0:
            row.append(1)

        result.append(row)

    return result
