class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        # Dummy head and tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    # Add node right after head
    def add(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    # Remove node from the list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Mark as recently used
        self.remove(node)
        self.add(node)

        return node.value

    def put(self, key, value):
        # If key already exists
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            # Move to front
            self.remove(node)
            self.add(node)
            return

        # Create new node
        node = Node(key, value)
        self.cache[key] = node
        self.add(node)

        # Exceeded capacity
        if len(self.cache) > self.capacity:
            lru = self.tail.prev

            self.remove(lru)
            del self.cache[lru.key]