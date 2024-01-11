#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    suared = list(map(lambda ro: list(map(lambda x: x**2, ro)), matrix))
    return suared
