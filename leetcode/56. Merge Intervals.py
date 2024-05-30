from operator import itemgetter
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: # type: ignore
        sorted_list= sorted(intervals, key=itemgetter(0))
        newInterval = [sorted_list[0]]

        for i in range(1,len(sorted_list)):
            if newInterval[-1][1] >= sorted_list[i][0]:
                newInterval[-1][1] = max(newInterval[-1][1],sorted_list[i][1])
                newInterval[-1][0] = min(newInterval[-1][0],sorted_list[i][0])
            else:
                newInterval.append(sorted_list[i])
        
        return newInterval