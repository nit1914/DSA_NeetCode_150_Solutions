# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root, subRoot):
        
        # Check if two trees are identical
        def sameTree(p, q):
            if p is None and q is None:
                return True
            
            if p is None or q is None:
                return False
            
            if p.val != q.val:
                return False
            
            return (sameTree(p.left, q.left) and
                    sameTree(p.right, q.right))

        # If root becomes empty, subtree cannot be found
        if root is None:
            return False

        # Check current tree
        if sameTree(root, subRoot):
            return True

        # Search in left and right subtrees
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))