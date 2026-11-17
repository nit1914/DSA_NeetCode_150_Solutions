
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0

        for i in range(len(nums)):

            # Check if current index is reachable
            if i > maxReach:
                return False

            # Update farthest reachable index
            maxReach = max(maxReach, i + nums[i])

            # Check if last index is reachable
            if maxReach >= len(nums) - 1:
                return True

        return True
