class Node:
    def __init__(self, key: int, value: int, next_node=None, prev=None):
        self.next = next_node
        self.prev = prev
        self.key = key
        self.val = value

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {} # typing.Dict[int, Node]

    def get(self, key: int) -> int:
        # if list is empty
        if key not in self.map:
            return -1
        
        # get node
        node = self.map[key]
        self._remove(node)
        self._add(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self._remove(node)
        
        node = Node(key, value)
        self._add(node)
        self.map[key] = node

        if len(self.map) > self.capacity:
            node_to_remove = self.tail.prev
            self._remove(node_to_remove)
            del self.map[node_to_remove.key]

    def _add(self, node):
        # we want to put the node at the head of the list
        next_to_head = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_to_head
        next_to_head.prev = node
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
