class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        result = []

        def backtrack(start, subset):
            # Every current subset is a valid answer
            result.append(subset.copy())

            for i in range(start, len(nums)):

                # Skip duplicate choices at the same level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # Choose
                subset.append(nums[i])

                # Explore
                backtrack(i + 1, subset)

                # Undo choice
                subset.pop()

        backtrack(0, [])
        return result