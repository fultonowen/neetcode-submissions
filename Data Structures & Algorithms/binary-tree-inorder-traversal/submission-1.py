# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def inorder(root: Optional[TreeNode]):
            nonlocal ans
            if not root: return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
            return
        inorder(root)
        return ans