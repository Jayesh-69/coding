class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        start = 0
        current_cost = 0
        max_length = 0

        for end in range(n):
            # finding the current cost
            current_cost += abs(ord(s[end]) - ord(t[end]))

            # when our current cost if more then the maxCost we destroy the window
            while current_cost > maxCost:
                current_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1

            # we keep a record of max length
            max_length = max(max_length, end - start + 1)
        
        return max_length