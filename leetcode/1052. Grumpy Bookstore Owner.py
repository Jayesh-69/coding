class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        # first will create a new array with only customers that are affected
        newArr = []
        for i in range(len(customers)):
            newArr.append(customers[i]*grumpy[i])

        # now find the highest sum in this newArr of minutes consecutive lengths
        def max_sum_indices(arr, n):
            max_sum = 0
            current_sum = 0
            max_start_index = 0

            for i in range(n):
                current_sum += arr[i]

            max_sum = current_sum

            for i in range(n, len(arr)):
                current_sum = current_sum - arr[i - n] + arr[i]

                if current_sum > max_sum:
                    max_sum = current_sum
                    max_start_index = i - n + 1

            return max_start_index, max_start_index+n


        sIndex, eIndex = max_sum_indices(newArr, minutes)
        finalAns = 0

        for i in range(len(customers)):
            if sIndex <= i and i < eIndex:
                finalAns += customers[i]
            elif grumpy[i] == 0:
                finalAns += customers[i]

        return finalAns
