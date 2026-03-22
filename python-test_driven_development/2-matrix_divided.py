#!/usr/bin/python3
"""Module for dividing all elements of a matrix.

This module provides a function to divide all elements of a matrix
by a given divisor, rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div, rounded to 2 decimal places.

    Returns a new matrix with all elements divided by div.
    Raises TypeError if matrix is not a list of lists of integers/floats,
    if rows have different sizes, or if div is not a number.
    Raises ZeroDivisionError if div is 0.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError(msg)
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(el / div, 2) for el in row] for row in matrix]
