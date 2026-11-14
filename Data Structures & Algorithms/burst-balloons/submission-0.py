from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add boundary balloons with value 1 on both ends
        arr = [1] + nums + [1]
        n = len(arr)
        
        # dp[left][right] = max coins from bursting balloons strictly between left and right
        dp = [[0] * n for _ in range(n)]
        
        # length is the distance between left and right boundaries
        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length
                # Try bursting each balloon k last within (left, right)
                for k in range(left + 1, right):
                    coins = arr[left] * arr[k] * arr[right]
                    total = coins + dp[left][k] + dp[k][right]
                    if total > dp[left][right]:
                        dp[left][right] = total
                        
        return dp[0][n - 1]
        