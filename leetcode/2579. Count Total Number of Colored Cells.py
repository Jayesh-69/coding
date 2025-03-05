class Solution:
    # Are kuch nhi hai yrr achhe se dekh ek pyramid bn raha hai odd numbers ka.
    def coloredCells(self, n: int) -> int:
        return (2*(n*n))+1-(2*n)