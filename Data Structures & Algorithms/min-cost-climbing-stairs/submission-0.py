
class Solution:
    def minCostClimbingStairs(self, cost):
        prev2 = 0
        prev1 = 0

        for i in range(2, len(cost) + 1):
            current = min(
                prev1 + cost[i - 1],
                prev2 + cost[i - 2]
            )

            prev2 = prev1
            prev1 = current

        return prev1