class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for j in range(n)] for i in range(m)] 
        grid[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                temp1 = 0
                temp2 = 0
                if i-1 >= 0:
                    temp1 = grid[i-1][j]
                if j-1 >= 0:
                    temp2 = grid[i][j-1]
                grid[i][j] = temp1 + temp2
        return grid[-1][-1]