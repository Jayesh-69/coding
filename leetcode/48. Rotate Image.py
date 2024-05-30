# What we did is first we took a deep copy of the matrix
# now we have seen a pattern that every row can be converted into coloum by placing
# one element in each coloum

from copy import deepcopy


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:  # type: ignore
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = deepcopy(matrix)
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                matrix[j][i] = temp[n-i-1][j]
