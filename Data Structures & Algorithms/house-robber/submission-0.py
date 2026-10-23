class Solution:
    def rob(self, nums):
        prev2 = 0  # Maximum money up to two houses before
        prev1 = 0  # Maximum money up to previous house

        for money in nums:
            # Either skip this house or rob it
            current = max(prev1, prev2 + money)

            prev2 = prev1
            prev1 = current

        return prev1