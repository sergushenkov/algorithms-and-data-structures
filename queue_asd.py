class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Queue_ASD:
    GET_OK = 1  # последний get_*() отработал нормально
    GET_ERR = 2  # список пуст

    REMOVE_OK = 1  # последний remove_*() отработал нормально
    REMOVE_ERR = 2  # список пуст

    def __init__(self):
        """
        конструктор
        постусловие:
        1) создана новая пустая очередь
        2) статусы операций указывают что очередь пуста"""
        self._head = None
        self._tail = None
        self._size = 0
        self._remove_status = Queue.REMOVE_ERR
        self._get_status = Queue.GET_ERR

    def add_tail(self, value):
        """
        Постусловие - в хвост очереди добавлено новое значение"""
        node = Node(value)
        if self._head is None:
            self._head = node
            self._tail = node
            self._size = 1
            return
        self._tail.next = node
        node.prev = self._tail
        self._tail = node
        self._size += 1

    def remove_front(self):
        """
        Предусловие - очередь не пуста
        Постусловие - удалено значение из головы, сместив очередь влево"""
        if self._head is None:
            self._remove_status = Queue.REMOVE_ERR
            return
        self._remove_status = Queue.REMOVE_OK
        self._size -= 1
        if self._head.next is None:
            self._head = None
            self._tail = None
            return
        self._head.next.prev = None
        self._head = self._head.next

    def get_head(self):
        """
        выдача из головы"""
        if self._head is None:
            self._get_status = Queue.GET_ERR
            return None
        self._get_status = Queue.GET_OK
        return self._head.value

    def size(self):
        return self._size

    def get_get_status(self):
        return self._get_status

    def get_remove_status(self):
        return self._remove_status


class Queue(Queue_ASD):
    pass


class Dequeue(Queue_ASD):
    def add_front(self, value):
        """
        Постусловие - в голову очереди добавлено новое значение"""
        node = Node(value)
        if self._head is None:
            self._head = node
            self._tail = node
            self._size = 1
            return
        self._head.prev = node
        node.next = self._head
        self._head = node
        self._size += 1

    def remove_tail(self):
        """
        Предусловие - очередь не пуста
        Постусловие - удалено значение из хвоста"""
        if self._head is None:
            self._remove_status = Queue.REMOVE_ERR
            return
        self._remove_status = Queue.REMOVE_OK
        self._size -= 1
        if self._head.next is None:
            self._head = None
            self._tail = None
            return
        self._tail.prev.next = None
        self._tail = self._tail.prev

    def get_tail(self):
        """
        выдача из головы"""
        if self._head is None:
            self._get_status = Queue.GET_ERR
            return None
        self._get_status = Queue.GET_OK
        return self._tail.value
