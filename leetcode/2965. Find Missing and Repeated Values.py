class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        tempSet = []
        totalSum = 0

        sumOfNNaturalNumber = ((n*n)*((n*n)+1))//2

        for i in grid:
            totalSum += sum(i)
            tempSet.extend(i)
        
        tempSet = set(tempSet)
        
        missingNumber = sumOfNNaturalNumber - sum(tempSet)
        repeatNumber = (totalSum + missingNumber) - sumOfNNaturalNumber
        return [repeatNumber, missingNumber]