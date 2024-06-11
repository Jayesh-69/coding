class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        remaning = sorted(list(set(arr1) - set(arr2)))
        arr2.extend(remaning)
        newArr1 = []

        for i in arr2:
            newArr1.extend([i]*arr1.count(i))
        
        return newArr1