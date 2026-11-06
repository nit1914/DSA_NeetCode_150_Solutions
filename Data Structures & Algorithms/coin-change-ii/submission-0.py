
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        # dp[i] = number of ways to make amount i
        dp = [0] * (amount + 1)

        # There is one way to make amount 0: choose no coins
        dp[0] = 1

        # Process each coin
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]
