class Solution:
    def twoSum(self, nums, target):

        # Dictionary to store number -> index
        seen = {}

        # Visit every element
        for i in range(len(nums)):

            # Current number
            current = nums[i]

            # Number needed to reach target
            need = target - current

            # Have we already seen the needed number?
            if need in seen:

                # Return the index of the needed number
                # and the current index
                return [seen[need], i]

            # Remember the current number
            seen[current] = i