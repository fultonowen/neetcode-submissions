# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # testing that a pattern exists
    # testing that the values are equivalent
    def check(self, base: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
        if not base and not sub: return True
        if not base or not sub: return False

        return base.val == sub.val and self.check(base.left, sub.left) and self.check(base.right, sub.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        return self.check(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

