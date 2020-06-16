# June 4 2020

# 1: Linked List + hashmap
from collections import OrderedDict


class DNode:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.PN = None
        self.NN = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = dict()
        self.head = DNode()
        self.tail = DNode()    # head = tail
        self.head.NN = self.tail
        self.tail.PN = self.head

    def _move_to_head(self, node: DNode):
        self._remove_node(node)
        self._add_node(node)

    def _remove_node(self, node: DNode):
        prev = node.PN
        next = node.NN

        prev.NN = next
        next.PN = prev

    def _add_node(self, node: DNode):  # add to head
        old_head = self.head.NN

        self.head.NN = node
        node.PN = self.head

        node.NN = old_head
        old_head.PN = node

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        node = self.store[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            node = self.store[key]
            node.value = value
            self._move_to_head(node)
        else:
            node = DNode()
            node.key = key
            node.value = value
            self._add_node(node)
            self.store[key] = node
            if len(self.store) > self.capacity:
                node_to_del = self.tail.PN
                self._remove_node(node_to_del)
                del(self.store[node_to_del.key])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class LRUCache1:

    def __init__(self, capacity: int):
        self.d = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        self.d.move_to_end(key)
        return self.d[key]

    def put(self, key: int, value: int) -> None:
        self.d[key] = value
        self.d.move_to_end(key)
        if len(self.d) > self.capacity:
            self.d.popitem(last=False)  # pop first
