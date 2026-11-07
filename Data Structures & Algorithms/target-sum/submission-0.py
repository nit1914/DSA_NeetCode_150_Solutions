class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:

        dp = {}

        def solve(index, total):

            # Base case
            if index == len(nums):
                return 1 if total == target else 0

            # Check memoization
            if (index, total) in dp:
                return dp[(index, total)]

            # Choose + or -
            add = solve(index + 1, total + nums[index])
            subtract = solve(index + 1, total - nums[index])

            dp[(index, total)] = add + subtract

            return dp[(index, total)]

        return solve(0, 0)