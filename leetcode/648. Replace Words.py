class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        s = sentence.split(" ")
        newS = ""

        for i in s:
            isFlag = False
            trimed = i
            for j in dictionary:
                if j == trimed[:len(j)]:
                    trimed = j+" "
                    isFlag = True
            if not isFlag:
                newS += i+" "
            else:
                newS += trimed
        
        return newS.strip()