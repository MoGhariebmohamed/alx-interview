#!/usr/bin/python3
"""
to rotatate the mterix n*m
"""


def rotate_2d_matrix(matrix):
    """
    the method to rotate 2d matrix
    """
    length_mat = len(matrix)
    for any in range(length_mat):
        for nex in range(any, length_mat):
            matrix[any][nex], matrix[nex][any] = matrix[nex][any], matrix[any][nex]
    for initial in matrix:
        initial.reverse()
