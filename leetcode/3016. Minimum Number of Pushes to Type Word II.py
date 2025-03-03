class Solution:
    def minimumPushes(self, word: str) -> int:
        tempSet = set(list(word))
        if len(tempSet) <= 8:
            return len(word)
        
        tempDict = {}
        for i in word:
            if i in tempDict:
                tempDict[i] += 1
            else:
                tempDict[i] = 1
        
        tempDict = {k: v for k, v in sorted(tempDict.items(), key=lambda item: item[1], reverse=True)}
        pushes = 0
        count = 0
        multipier = 1
        for i in tempDict:
            if count < 8:
                pushes += (multipier*tempDict[i])
                count += 1
            else:
                count = 1
                multipier += 1
                pushes += (multipier*tempDict[i])
        return pushes