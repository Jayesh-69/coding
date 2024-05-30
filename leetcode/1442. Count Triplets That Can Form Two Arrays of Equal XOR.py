# What we did is as we know XOR of same element is zero
# so we are looping over each element by keeping the first one fix and 
# finding the XOR if 0 means we have got the sub array where the question condition may fit
# so we add up all such values and return it

class Solution:
    def countTriplets(self, arr: List[int]) -> int: # type: ignore
        count = 0

        for i in range(len(arr)-1):
            curr = arr[i]
            for j in range(i+1,len(arr)):
                curr ^= arr[j]
                if curr == 0:
                    count += j-i
        
        return count