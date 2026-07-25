from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()      # stores indices
        ans = []

        for i in range(len(nums)):

            # Remove indices outside the current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Record maximum once first window is formed
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans