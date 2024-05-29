# Here what we did is, first we converted the binary number to decimal
# Now we itreate over it and inc the count, while making the chnages in question

class Solution:
    def numSteps(self, s: str) -> int:
        n = int(s, 2)
        count = 0

        while n != 1:
            if n % 2 == 0:
                n = n//2
            else:
                n += 1
            count += 1
        return count
