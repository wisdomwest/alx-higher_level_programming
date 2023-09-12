#!/usr/bin/python3
"""Module contains Pascal's Triangle function"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n"""
    if n <= 0:
        return []

    triangles = [[1]]

     for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
