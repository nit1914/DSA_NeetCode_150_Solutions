class Solution:
    def rob(self, nums):
        # Only one house
        if len(nums) == 1:
            return nums[0]

        def rob_linear(arr):
            prev2 = 0
            prev1 = 0

            for money in arr:
                current = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = current

            return prev1

        # Case 1: Exclude the last house
        case1 = rob_linear(nums[:-1])

        # Case 2: Exclude the first house
        case2 = rob_linear(nums[1:])

        return max(case1, case2)