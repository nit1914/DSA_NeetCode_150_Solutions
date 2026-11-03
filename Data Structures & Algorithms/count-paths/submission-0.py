
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # Create DP table
        dp = [[1] * n for _ in range(m)]

        # Calculate number of paths
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]


# Example 1
m = 3
n = 6
obj = Solution()
print(obj.uniquePaths(m, n))

# Example 2
m = 3
n = 3
print(obj.uniquePaths(m, n))
