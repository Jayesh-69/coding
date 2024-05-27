class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort() # sort the array for getting the min number always
        
        returnValue = -1 # incase we dont find anything

        count = 0

        # running loop in reverse with the length as we can't get more then the length
        for x in range(len(nums),0,-1):
            if x <= nums[count] and x == len(nums) - count: # this was asked
                if x > nums[count-1] and count > 0: # this is to handle a corner case were 
                    # if a number if present smaller then current in previously visited element
                    returnValue = max(x,returnValue)
                elif count == 0:
                    returnValue = max(x,returnValue)
            count += 1
        return returnValue
