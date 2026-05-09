# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None: return True

        def helper(root: Optional[TreeNode], min_value, max_value):
            if not root: return True
            if not (min_value < root.val < max_value):
                return False
            return helper(root.left, min_value, root.val) and helper(root.right, root.val, max_value)
        
        return helper(root, float("-inf"), float("inf"))
