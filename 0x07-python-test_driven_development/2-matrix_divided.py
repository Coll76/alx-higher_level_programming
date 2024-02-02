#!/usr/bin/python3
"""
function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Parameters:
        matrix: matrix its elements to be divided
        dix: number to be used in the division
    Returns:
        list: a new matrix hose elements have been divided by div
    Example:
        >>> matrix = [[[1, 2, 3], [4, 5, 6]]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """
    first = matrix[0]
    for ro in matrix[1:]:
        if len(ro) != len(first):
            raise TypeError('Each row of the matrix must have the same size')
    for ro in matrix:
        for j in ro:
            if not isinstance(j, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            if not isinstance(div, (int, float)):
                raise TypeError('div must be a number')
            if div == 0:
                raise ZeroDivisionError('division by zero')
            ne_matrix = list(map(lambda ro: list(map(lambda j: round((j / div), 2), ro)), matrix))
        return ne_matrix
