class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pT = [[1],[1,1],[1,2,1]] # setting the pascal triangle upto 3 level by default
        if(numRows < 4):
            return pT[:numRows]
        
        numRows -= 3 # as upto 3 is already been calculated
        n = 4
        for i in range(numRows):
            newRow = [1]*n
            if(n % 2 == 0):
                # even
                midPoint = n // 2
                for j in range(1,midPoint):
                    newRow[j] = pT[n-2][j] + pT[n-2][j-1]
                    newRow[-(j+1)] = newRow[j]
            else:
                # odd
                midPoint = (n // 2) + 1
                for j in range(1,midPoint):
                    if j == midPoint - 1:
                        newRow[j] = pT[n-2][j] + pT[n-2][j-1]
                    else:    
                        newRow[j] = pT[n-2][j] + pT[n-2][j-1]
                        newRow[-(j+1)] = newRow[j]
            pT.append(newRow)
            n += 1
        return pT