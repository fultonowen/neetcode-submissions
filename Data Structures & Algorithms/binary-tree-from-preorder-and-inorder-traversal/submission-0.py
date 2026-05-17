# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder is node, left, right
        # inorder is left, node, right
        if not preorder: return None
        self.preorder = preorder
        self.inorder_map = {}
        for idx, value in enumerate(inorder):
            self.inorder_map[value] = idx
        
        self.p_idx = 0
        root = self.preorder_walk(0, 0, len(preorder)-1)
        return root
    
    def preorder_walk(self, p_idx: int, l: int, r: int) -> Optional[TreeNode]:
        if l > r: return None
        root_val = self.preorder[p_idx]
        self.p_idx += 1
        node = TreeNode(root_val)
        node.left = self.preorder_walk(self.p_idx, l, self.inorder_map[root_val] -1)
        node.right = self.preorder_walk(self.p_idx, self.inorder_map[root_val] + 1, r)
        return node
