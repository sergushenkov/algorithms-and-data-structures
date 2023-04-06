class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, item):
        node = Node(item)
        self.length += 1
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def dequeue(self):
        if self.head is None:
            return None
        node = self.head
        self.length -= 1
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return node.value

    def size(self):
        return self.length
