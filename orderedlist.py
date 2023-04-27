class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc=True):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        return 0

    def add(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        if self.__ascending:
            if OrderedList.compare(self, value, self.head.value) < 1:
                self.head.prev = node
                node.next = self.head
                self.head = node
                return
            if OrderedList.compare(self, value, self.tail.value) > -1:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
                return
            left = self.head.next
            while OrderedList.compare(self, left.value, value) == -1:
                left = left.next
            left.prev.next = node
            node.prev = left.prev
            node.next = left
            left.prev = node
            return
        # self.__ascending == False
        if OrderedList.compare(self, value, self.head.value) > -1:
            self.head.prev = node
            node.next = self.head
            self.head = node
            return
        if OrderedList.compare(self, value, self.tail.value) < 1:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            return
        left = self.head.next
        while OrderedList.compare(self, left.value, value) == 1:
            left = left.next
        left.prev.next = node
        node.prev = left.prev
        node.next = left
        left.prev = node
        return

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node.value
            if (self.__ascending and node.value > val
                    ) or (not self.__ascending and node.value < val):
                return None
            node = node.next
        return None

    def delete(self, val):
        prev_node = None
        node = self.head
        while node is not None:
            if OrderedList.compare(self, node.value, val) == 0:
                if prev_node is None:
                    self.head = node.next
                    if self.head is None:
                        self.tail = None
                    else:
                        self.head.prev = None
                else:
                    prev_node.next = node.next
                if node.next is None:
                    self.tail = prev_node
                else:
                    node.next.prev = prev_node
                break
                node = node.next
            elif (OrderedList.compare(self, node.value, val) > 0 and self.__ascending
                  ) or (OrderedList.compare(self, node.value, val) < 0
                        and not self.__ascending):
                return
            else:
                prev_node = node
                node = node.next

    def clean(self, asc=True):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        cnt = 0
        node = self.head
        while node is not None:
            cnt += 1
            node = node.next
        return cnt

    def get_all(self):
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc=True):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1 = v1.strip()
        v2 = v2.strip()
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        return 0
