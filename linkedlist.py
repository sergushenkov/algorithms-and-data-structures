class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        finded = []
        node = self.head
        while node is not None:
            if node.value == val:
                finded.append(node)
            node = node.next
        return finded
    
    def delete(self, val, all=False):
        prev_node = None
        node = self.head
        while node is not None:
            if node.value == val:
                if prev_node is None:
                    self.head = node.next
                else:
                    prev_node.next = node.next
                if node.next is None:
                    self.tail = prev_node
                if not all:
                    break
                node = node.next
            else:
                prev_node = node
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
            newNode.next = self.head
            if self.head is None:
                self.tail = newNode
            self.head = newNode
        else:
            node = self.head
            while node is not None:
                if node.value == afterNode.value:
                    newNode.next = node.next
                    if node.next is None:
                        self.tail = newNode
                    node.next = newNode
                    break
                node = node.next
