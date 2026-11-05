
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        hold = -prices[0]
        sold = 0
        cooldown = 0

        for price in prices[1:]:
            prev_hold = hold
            prev_sold = sold
            prev_cooldown = cooldown

            # Buy or continue holding
            hold = max(prev_hold, prev_cooldown - price)

            # Sell the stock today
            sold = prev_hold + price

            # Stay in cooldown or rest
            cooldown = max(prev_cooldown, prev_sold)

        return max(sold, cooldown)
