class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    # Remove from anywhere in the dl list
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    # Insert at the end (between right dummy node and its prev)
    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        self.right.prev = node

        node.next = self.right
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        # If we have that node, first remove it from the dl list
        if key in self.cache:
            self.remove(self.cache[key])
        #update the cache
        self.cache[key] = Node(key, value)
      #add it to the end of dl list
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # if over capacity then remove the left most thing in the dl list
            lru = self.left.next
            self.remove(lru)
            # remove from the cache
            self.cache.pop(lru.key)