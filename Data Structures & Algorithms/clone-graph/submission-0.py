"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None: return node

        seen_nodes = {}
        seen = set()
        seen_nodes[node] = Node(node.val)
        bfs_q = collections.deque([node])
        while bfs_q:
            curr_node = bfs_q.popleft()
            if curr_node in seen:
                continue
            seen.add(curr_node)
            if not curr_node in seen_nodes:
                seen_nodes[curr_node] = Node(curr_node.val)
            new_node = seen_nodes[curr_node]

            for neighbor in curr_node.neighbors:
                if neighbor not in seen_nodes:
                    seen_nodes[neighbor] = Node(neighbor.val)
                if neighbor not in seen:
                    bfs_q.append(neighbor)
                
                new_node.neighbors.append(seen_nodes[neighbor])



        return seen_nodes[node]