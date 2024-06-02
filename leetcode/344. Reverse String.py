# Here what we are doing is we are itreating upto middle element
# and swapping the elements
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n//2):
            s[i],s[-(i+1)] = s[-(i+1)],s[i]