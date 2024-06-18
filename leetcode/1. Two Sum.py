class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p1 = 0        
        while True:
            if target - nums[p1] in nums[p1+1:]:
                return [p1,p1+1+nums[p1+1:].index(target-nums[p1])]
            p1 += 1