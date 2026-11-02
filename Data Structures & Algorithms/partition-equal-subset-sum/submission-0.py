class Solution:
    def canPartition(self, nums):
        total = sum(nums)

        # Equal partition is impossible if total is odd
        if total % 2 != 0:
            return False

        target = total // 2

        # dp[i] = True if sum i can be formed
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # Traverse backwards so each number is used once
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]