class Node:
    def __init__(self, key: int, val: int, next: Optional[Node]=None, prev: Optional[Node]=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1, None, self.head)
        self.head.next = self.tail
        self.capacity = capacity
        self.node_map = {}

    def _remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert(self, node: Node):
        self.head.next.prev = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node

    def get(self, key: int) -> int:
        if not key in self.node_map: return -1

        node = self.node_map[key]
        self._remove(node)
        self._insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            self._remove(self.node_map[key])

        self.node_map[key] = Node(key, value)
        node = self.node_map[key]
        self._insert(node)

        if len(self.node_map) > self.capacity:
            node_to_delete = self.tail.prev
            self._remove(node_to_delete)
            del self.node_map[node_to_delete.key]


