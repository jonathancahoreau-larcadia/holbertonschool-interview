#!/usr/bin/python3
"""
Minimum operations lab.

Compute the minimum number of Copy All and Paste operations required
to reach exactly `n` characters starting from a single `H`.
"""


def minOperations(n):
    """
    Return the fewest number of operations needed to produce exactly n
    H characters.

    A single file initially contains "H".
    Allowed operations:
    - Copy All: copies the current file contents into the clipboard.
    - Paste: appends clipboard contents to the file.

    The optimal result is obtained by decomposing n into its prime factors
    and summing those factors.

    If n is 1 or less, no operations are required.
    """
    if n <= 1:
        return 0

    op = 0
    div = 2

    while n != 1:
        if n % div == 0:
            n = n // div
            op += div
        else:
            div += 1

    return op
