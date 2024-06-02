class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums
        
        nums.sort()
        toReturn = []
        n = len(nums)
        i = 0

        while i < n-1:
            if nums[i] == nums[i+1]:
                i += 2
            else:
                toReturn.append(nums[i])
                i += 1

        if i == n-1:
            toReturn.append(nums[i])        
        return toReturn