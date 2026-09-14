class Solution:
    def combinationSum(self, nums, target):
        nums.sort()
        result = []
        path = []

        def backtrack(start, remaining):
            # Found a valid combination
            if remaining == 0:
                result.append(path.copy())
                return

            for i in range(start, len(nums)):
                # Since nums is sorted, no later number can work
                if nums[i] > remaining:
                    break

                # Choose nums[i]
                path.append(nums[i])

                # Use i again because unlimited reuse is allowed
                backtrack(i, remaining - nums[i])

                # Undo choice
                path.pop()

        backtrack(0, target)
        return result