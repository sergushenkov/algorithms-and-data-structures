class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        found_nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                found_nodes.append(node)
            node = node.next
        return found_nodes

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value == val:
                if node is self.head and node is self.tail:
                    self.head = None
                    self.tail = None
                elif node is self.head:
                    self.head = node.next
                    self.head.prev = None
                elif node is self.tail:
                    self.tail = node.prev
                    self.tail.next = None
                else:
                    node.next.prev = node.prev
                    node.prev.next = node.next
                if not all:
                    return
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        cnt = 0
        node = self.head
        while node is not None:
            cnt += 1
            node = node.next
        return cnt

    def insert(self, afterNode, newNode):
        if afterNode is None:
            if self.head is None:
                self.head = newNode
                self.tail = newNode
                self.head.prev = None
                self.head.next = None
                self.tail.prev = None
                self.tail.next = None
            else:
                self.tail.next = newNode
                newNode.prev = self.tail
                newNode.next = None
                self.tail = newNode
        else:
            node = self.head
            while node is not None:
                if node.value == afterNode.value:
                    newNode.prev = node
                    newNode.next = node.next
                    node.next = newNode
                    if newNode.next is not None:
                        newNode.next.prev = newNode
                    else:
                        self.tail = newNode
                    return
                node = node.next



    def add_in_head(self, newNode):
        newNode.next = self.head
        newNode.prev = None
        if self.head is None:
            self.tail = newNode
        else:
            self.head.prev = newNode
        self.head = newNode
