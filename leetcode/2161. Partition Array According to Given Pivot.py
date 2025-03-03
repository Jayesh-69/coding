class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessArr = []
        sameArr = []
        moreArr = []

        for i in nums:
            if i < pivot:
                lessArr.append(i)
            elif i > pivot:
                moreArr.append(i)
            else:
                sameArr.append(i)
        
        return lessArr + sameArr + moreArr