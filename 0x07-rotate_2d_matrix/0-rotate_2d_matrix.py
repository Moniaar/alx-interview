#!/usr/bin/python3
"""
0-rotate_2d_matrix.py module
Contains the function to rotate a 2D matrix 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the given n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): 2D matrix to rotate.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()


if __name__ == "__main__":
    """
    Test 0x07 - Rotate 2D Matrix
    """
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
