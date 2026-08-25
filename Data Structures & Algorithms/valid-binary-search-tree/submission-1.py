# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        max_seen, min_seen = float("-inf"), float("inf")

        def helper(root: Optional[TreeNode], left, right):
            if not root: return True
            if not (left < root.val < right):
                return False
            return helper(root.left, left, root.val) and helper(root.right, root.val, right)
        return helper(root, max_seen, min_seen)
            
