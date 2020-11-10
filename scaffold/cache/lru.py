import collections

# First implementation: OrderedDict hashmap
# OrderedDict keeps track of the order in which elements were inserted, 1 -> 2 -> 3, and has popitem() [3] or popitem(False) [1]
# as well as move_to_end(key, True/False)
# The simple idea is, we use the OrderedDict order, least recently used on the left.
from typing import Optional, Dict


class LRU:
    def __init__(self, capacity):
        self.hash = collections.OrderedDict()
        self.capacity = capacity

    # Return -1 if it doesn't exist
    def get(self, key):
        if key not in self.hash:
            return -1
        else:
            self.hash.move_to_end(key)
            return self.hash[key]

    def put(self, key, value):
        self.hash[key] = value
        self.hash.move_to_end(key)
        if len(self.hash) > self.capacity:
            self.hash.popitem(last=False)

# Second implementation: from scratch!
# The key trick is twofold:
# 1. when you add an item, you need to add (or move) it to the top of a stack,
#   and if you're at capacity and it's a *new* item, then evict the last item
# 2. when you get an item, you need to move it to the top of the stack.
# So you want to start with a hashmap from key to value.
# In order to get the evictions correct, you'll need to make value a Node with a couple pointers.
# one to the previous node in the stack, and one to the next node in the stack.
# You'll also need to keep a pointer to the head, to the tail, and keep track of the stack size.
# When you get an item, look to see if it's present in the map.  If it is, do the pointer arithmetic to move it to the front of the list.
# When you add an item, check to see if it's present in the map (Does this refresh the key?  Depends on definition.. assume no)
# If not, evict.
class LRUNode:
    def __init__(self, key: int, value: int):
        self.previous: Optional[LRUNode] = None
        self.next: Optional[LRUNode] = None
        self.value = value
        self.key = key


class LRU2:
    def __init__(self, capacity: int):
        self.head: Optional[LRUNode] = None  # Most recent
        self.tail: Optional[LRUNode] = None  # Least recent
        self.count = 0
        self.capacity = capacity
        self.hash: Dict[int, LRUNode] = {}

    def _move_to_head(self, candidate_node: LRUNode):
        assert candidate_node.previous is not None
        assert self.head is not None
        candidate_node.previous.next = candidate_node.next
        # We don't want to swap if the candidate_node is already at the head of the list.
        if candidate_node.next:
            candidate_node.next.previous = candidate_node.previous
        else:  # this means candidate_node is the tail
            self.tail = candidate_node.previous
        # Finally, we must move the candidate to the head.
        candidate_node.next = self.head
        candidate_node.previous = None
        self.head.previous = candidate_node
        self.head = candidate_node

    # Return -1 if it doesn't exist
    def get(self, key):
        if key not in self.hash:
            return -1
        else:
            candidate_node = self.hash[key]
            if candidate_node.previous:
                self._move_to_head(candidate_node)
            return candidate_node.value

    def put(self, key, value):
        # First check to see if it already exists in the stack
        if key in self.hash:
            # Means a key is in the dict, which means head and tail will both be set.
            # Do the swapping pointer arithmetic.
            candidate_node = self.hash[key]
            candidate_node.value = value
            # If there is a prior node, then swapping must occur
            if candidate_node.previous:
                self._move_to_head(candidate_node)
        else:  # This is a new key
            self.count += 1
            candidate_node = LRUNode(key, value)
            self.hash[key] = candidate_node
            if self.head:  # The cache has some element
                candidate_node.next = self.head
                self.head.previous = candidate_node
                self.head = candidate_node
            else:  # The cache is currently empty
                self.head = candidate_node
                self.tail = candidate_node
            if self.count > self.capacity:
                assert self.tail is not None
                end = self.tail
                assert end.previous is not None  # This would mean that capacity == 0.
                end.previous.next = None
                self.tail = end.previous
                del self.hash[end.key]


if __name__ == "__main__":
    lru = LRU2(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))
    lru.put(3, 3)
    print(lru.get(2))
    lru.put(4, 4)
    print(lru.get(1))
    print(lru.get(3))
    print(lru.get(4))
