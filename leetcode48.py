from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        margin = len(matrix)
        matrix.reverse()
        for i in range(margin):
            for j in range(margin):
                if j > i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
