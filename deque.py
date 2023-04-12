class Node:
    def __init__(self, val=None):
        self.value = val
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def addFront(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def addTail(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def removeFront(self):
        if self.head is None:
            return None
        node = self.head
        if self.tail is self.head:
            self.head = None
            self.tail = None
        else:
            self.head = node.next
            self.head.prev = None
        return node.value

    def removeTail(self):
        if self.tail is None:
            return None
        node = self.tail
        if self.tail is self.head:
            self.head = None
            self.tail = None
        else:
            self.tail = node.prev
            self.tail.next = None
        return node.value

    def size(self):
        cnt = 0
        node = self.head
        while node is not None:
            cnt += 1
            node = node.next
        return cnt
