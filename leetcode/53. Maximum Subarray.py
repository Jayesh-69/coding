# Here we first took a max as -infinty and sum as 0
# Now we add all the number one by one and record the max we got till now
# and making the sum 0 if we encounter negative sum

import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int: # type: ignore
        maxm = -math.inf

        sum = 0

        for i in nums:
            sum += i
            maxm = max(sum, maxm)
            if sum < 0:
                sum = 0

        return maxm
