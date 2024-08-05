class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        newArr = []
        occured = []

        for i in arr:
            if i in occured:
                try:
                    newArr.remove(i)
                except:
                    pass
            else:
                newArr.append(i)
                occured.append(i)
        
        if len(newArr) < k:
            return ""
        return newArr[k-1]