# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root: TreeNode, max_seen: int) -> int:
            if not root: return 0
            val = 1 if root.val >= max_seen else 0
            return val + helper(root.left, max(root.val, max_seen)) + helper(root.right, max(root.val, max_seen))
        
        return helper(root, -101)