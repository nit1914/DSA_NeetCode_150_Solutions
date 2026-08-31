# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root, k):
        stack = []
        current = root

        while current or stack:
            # Go as far left as possible
            while current:
                stack.append(current)
                current = current.left

            # Visit the smallest remaining node
            current = stack.pop()
            k -= 1

            # kth smallest found
            if k == 0:
                return current.val

            # Move to right subtree
            current = current.right  