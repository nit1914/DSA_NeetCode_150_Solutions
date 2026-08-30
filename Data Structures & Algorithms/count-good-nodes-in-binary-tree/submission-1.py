# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_value):
            if not node:
                return 0
            
            # Check if current node is good
            good = 1 if node.val >= max_value else 0
            
            # Update maximum value for this path
            max_value = max(max_value, node.val)
            
            # Visit left and right subtrees
            good += dfs(node.left, max_value)
            good += dfs(node.right, max_value)
            
            return good
        
        return dfs(root, root.val)