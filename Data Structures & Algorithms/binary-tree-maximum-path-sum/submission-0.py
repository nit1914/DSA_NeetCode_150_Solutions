# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root):
        self.result = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # Best contribution from left and right
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Path passing through current node
            current_path = node.val + left + right

            # Update global maximum
            self.result = max(self.result, current_path)

            # Return best single-side path to parent
            return node.val + max(left, right)

        dfs(root)
        return self.result