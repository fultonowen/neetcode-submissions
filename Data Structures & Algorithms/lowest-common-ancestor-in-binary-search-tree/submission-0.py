# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        child_to_parent = {}
        child_to_parent[root] = None
        def build(root: TreeNode):
            if not root: return

            if root.left:
                child_to_parent[root.left] = root
                build(root.left)
            if root.right:
                child_to_parent[root.right] = root
                build(root.right)
        build(root)
        seen = set([])
        curr = p
        while curr:
            seen.add(curr)
            curr = child_to_parent[curr]
        
        while q:
            if q in seen:
                return q
            q = child_to_parent[q]
        
        return None