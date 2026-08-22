# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = 0

        def dfs(node):
            nonlocal diameter

            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # Longest path passing through this node
            diameter = max(diameter, left + right)

            # Return height of this subtree
            return 1 + max(left, right)

        dfs(root)
        return diameter