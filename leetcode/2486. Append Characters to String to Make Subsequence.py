class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        lenS = len(s)
        lenT = len(t)

        flag1 = 0
        flag2 = 0

        while flag1 < lenS and flag2 < lenT:
            if s[flag1] == t[flag2]:
                flag1 += 1
                flag2 += 1
            else:
                flag1 += 1

        return lenT - flag2