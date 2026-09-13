class Solution:
    def subsets(self, nums):
        res = []
        subset = []

        def dfs(i):
            # We processed all numbers
            if i == len(nums):
                res.append(subset.copy())
                return

            # Choice 1: include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Backtrack
            subset.pop()

            # Choice 2: don't include nums[i]
            dfs(i + 1)

        dfs(0)
        return res