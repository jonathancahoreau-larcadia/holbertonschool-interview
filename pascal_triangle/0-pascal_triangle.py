#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(n - 1):
        prev_list = triangle[-1]
        new_list = [1]
        for j in range(len(prev_list) - 1):
            new_list.append(prev_list[j] + prev_list[j+1])
        new_list.append(1)
        triangle.append(new_list)
    return triangle
