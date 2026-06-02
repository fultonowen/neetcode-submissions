"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None: return head
        mapNodes = {}
        curr = head
        prev = None
        while curr:
            if curr not in mapNodes:
                mapNodes[curr] = Node(curr.val)
            if curr.random and curr.random not in mapNodes:
                mapNodes[curr.random] = Node(curr.random.val)
            
            if curr.random:
                mapNodes[curr].random = mapNodes[curr.random]
            else:
                mapNodes[curr].random = None
            if prev:
                mapNodes[prev].next = mapNodes[curr]

            prev = curr
            curr = curr.next
        

        return mapNodes[head]