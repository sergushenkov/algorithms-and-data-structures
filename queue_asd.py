class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Queue:

    DEQUEUE_OK = 1  # последний dequeue() отработал нормально
    DEQUEUE_ERR = 2  # список пуст

    POP_OK = 1  # последний pop() отработал нормально
    POP_ERR = 2  # список пуст

    def __init__(self):
        """
        конструктор
        постусловие:
        1) создана новая пустая очередь
        2) статусы операций указывают что очередь пуста"""
        self._head = None
        self._tail = None
        self._size = 0
        self._pop_status = Queue.POP_ERR
        self._dequeue_status = Queue.DEQUEUE_ERR


    def enqueue(self, value):
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

    def pop(self):
        """
        Предусловие - очередь не пуста
        Постусловие - удалено значение из головы, сместив очередь влево"""
        if self._head is None:
            self._pop_status = Queue.POP_ERR
            return
        self._pop_status = Queue.POP_OK
        self._size -= 1
        if self._head.next is None:
            self._head = None
            self._tail = None
            return
        self._head.next.prev = None
        self._head = self._head.next

    def clear(self):
        """
        Постусловие:
        1) очередь пуста"""
        self._head = None
        self._tail = None
        self._size = 0

    def dequeue(self):
        """
        выдача из головы"""
        if self._head is None:
            self._dequeue_status = Queue.DEQUEUE_ERR
            return None
        self._dequeue_status = Queue.DEQUEUE_OK
        return self._head.value
    
    def size(self):
        return self._size
    
    def get_dequeue_status(self):
        return self._dequeue_status
    
    def get_pop_status(self):
        return self._pop_status    
    
