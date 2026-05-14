#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]

        if triangle:
            last = triangle[-1]

            for j in range(len(last) - 1):
                row.append(last[j] + last[j + 1])

            row.append(1)

        triangle.append(row)

    return triangle
