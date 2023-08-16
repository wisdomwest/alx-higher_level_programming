#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nmatrix = []
    for row in matrix:
        nrow = []
        for value in row:
            nrow.append(value ** 2)
        nmatrix.append(nrow)
    return nmatrix
