class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target > matrix[i][-1]:
                # means not in this row
                continue
            if target < matrix[i][0]:
                # since the row are sorted we can check via first element
                return False
            if target in matrix[i]:
                return True
        return False