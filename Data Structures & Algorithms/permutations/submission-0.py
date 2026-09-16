class Solution:
    def permute(self, nums):
        result = []
        used = [False] * len(nums)

        def backtrack(path):
            # We have used every number
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # Choose
                used[i] = True
                path.append(nums[i])

                # Explore
                backtrack(path)

                # Undo choice (backtrack)
                path.pop()
                used[i] = False

        backtrack([])
        return result