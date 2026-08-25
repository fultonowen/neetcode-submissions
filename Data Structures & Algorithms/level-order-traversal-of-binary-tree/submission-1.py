# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root: return ans
        bfs_q = collections.deque([root])
        while bfs_q:
            qs = len(bfs_q)
            curr = []
            for _ in range(qs):
                node = bfs_q.popleft()
                curr.append(node.val)
                if node.left: bfs_q.append(node.left)
                if node.right: bfs_q.append(node.right)
            ans.append(list(curr))
        return ans