class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        totalWaitTime = customers[0][1]
        startFrom = sum(customers[0])

        for i in customers[1:]:
            if startFrom < i[0]:
                startFrom = i[0]
            totalWaitTime += (startFrom - i[0] + i[1])
            startFrom += i[1]
        return float("{:.5f}".format(totalWaitTime / len(customers)))