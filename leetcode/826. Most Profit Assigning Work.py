# The logic here is to sort in reverse order and take the max profit job and return the final profit

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort(reverse=True)

        sorted_indices = sorted(range(len(profit)), key=lambda k: profit[k], reverse=True)

        # Use the sorted indices to rearrange list2 in the same way
        profit = [profit[i] for i in sorted_indices]
        difficulty = [difficulty[i] for i in sorted_indices]

        refd = 0
        refw = 0
        finalAns = 0
        while refw != len(worker) and refd != len(difficulty):
            if difficulty[refd] > worker[refw]:
                refd += 1
                continue
            finalAns += profit[refd]
            refw += 1
        return finalAns