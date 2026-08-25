# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0
        bfs_q = collections.deque([(root, -100)])
        while bfs_q:
            node, prev_max = bfs_q.popleft()
            if node.val >= prev_max:
                count += 1
            if node.left:
                bfs_q.append((node.left, max(node.val, prev_max)))
            if node.right:
                bfs_q.append((node.right, max(node.val, prev_max)))
        
        

        return count