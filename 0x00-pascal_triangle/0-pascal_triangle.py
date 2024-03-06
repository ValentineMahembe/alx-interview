#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    a functon that returnsa list of integers reperesenting
    the Pascals triangle of n. Returns empty list if n <= 0
    and n will always be an integer
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = triangle[-1]
        for j in range(1, i):
            row.append(last_row[j-1] + last_row[j])
            row.append(1)
            triangle.append(row)

        return triangle
