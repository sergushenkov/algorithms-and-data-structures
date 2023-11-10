class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class ParentLinkedList:
    RIGHT_OK = 1  # последняя right() отработал нормально
    RIGHT_ERR = 2  # справа от курсора нет элементов

    LEFT_OK = 1  # последняя left() отработал нормально
    LEFT_ERR = 2  # слева от курсора нет элементов

    FIND_R = 1  # последний find() нашёл искомое значение справа
    FIND_L = 2  # последний find() нашёл искомое значение слева
    FIND_CUR = 3  # последний find() нашёл искомое значение только в курсоре
    FIND_ERR = 4  # последний find() не нашёл искомое значение

    GET_OK = 1  # последний get() отработал нормально
    GET_ERR = 2  # список пуст

    def __init__(self):
        """
        конструктор
        постусловие:
        1) создан новый пустой связанный список
        2) курсор указывает на head
        3) статусы операций не указывают на ошибки"""
        self._head = None
        self._tail = None
        self._cursor = None
        self._right_status = ParentLinkedList.RIGHT_OK
        self._left_status = ParentLinkedList.LEFT_OK
        self._find_status = ParentLinkedList.FIND_R
        self._get_status = ParentLinkedList.GET_OK

    # КОМАНДЫ

    def head(self):
        """
        постусловие: курсор указывает на head"""
        self._cursor = self._head

    def tail(self):
        """
        постусловие: курсор указывает на tail"""
        self._cursor = self._tail

    def right(self):
        """
        предусловие: справа от курсора есть элементы
        постусловие: курсор указывает на следующий узел за текущим"""
        if self._cursor is None or self._cursor.next is None:
            self._right_status = ParentLinkedList.RIGHT_ERR
            return
        self._right_status = ParentLinkedList.RIGHT_OK
        self._cursor = self._cursor.next

    def put_right(self, value):
        """
        постусловие:
        1) справа от текущего узла вставлен новый узел с указанным значением
        2) курсор указывает на текущий узел или на head() (если список был пуст)"""
        node = Node(value)
        if self._tail is None:
            self._head = node
            self._tail = node
            self._cursor = node
            return
        node.prev = self._cursor
        node.next = self._cursor.next
        self._cursor.next = node
        if node.next is None:
            self._tail = node
            return
        node.next.prev = node

    def put_left(self, value):
        """
        постусловие:
        1) слева от текущего узла вставлен новый узел с указанным значением
        2) курсор указывает на текущий узел или на head() (если список был пуст)"""
        node = Node(value)
        if self._tail is None:
            self._head = node
            self._tail = node
            self._cursor = node
            return
        node.prev = self._cursor.prev
        node.next = self._cursor
        self._cursor.prev = node
        if node.prev is None:
            self._head = node
            return
        node.prev.next = node

    def add_tail(self, value):
        """
        постусловие:
        1) в конец списка добавлен новый узел с указанным значением
        2) курсор указывает - на текущий узел, на head (если список был пуст)"""
        node = Node(value)
        if self._tail is None:
            self._head = node
            self._tail = node
            self._cursor = node
            return
        node.prev = self._tail
        self._tail.next = node
        self._tail = node

    def replace(self, value):
        """
        постусловие:
        1) текущий элемент имеет заданное значение
        2) курсор указывает - на текущий узел, на head (если список был пуст)"""
        if self._tail is None:
            node = Node(value)
            self._head = node
            self._tail = node
            self._cursor = node
            return
        self._cursor.value = value

    def find(self, value):
        """
        предусловие - в списке есть искомое значение
        постусловие - курсор указывает (первый из имеющихся) - искомый элемент справа, искомый элемент слева, текущий узел"""
        if self._tail is None:
            self._find_status = ParentLinkedList.FIND_ERR
            return
        node = self._cursor
        while node.next is not None:
            node = node.next
            if node.value == value:
                self._cursor = node
                self._find_status = ParentLinkedList.FIND_R
                return
        node = self._head
        while node is not self._cursor:
            if node.value == value:
                self._cursor = node
                self._find_status = ParentLinkedList.FIND_L
                return
            node = node.next
        if node.value == value:
            self._find_status = ParentLinkedList.FIND_CUR
            return
        self._find_status = ParentLinkedList.FIND_ERR

    def remove(self):
        """
        постусловие:
        1) текущий элемент удалён
        2) курсор указывает (первый из имеющихся) - на правого соседа, на левого соседа, на head"""
        if self._cursor is None:
            return
        if self._cursor is self._head and self._cursor is self._tail:
            self._head = None
            self._tail = None
            self._cursor = None
            return
        if self._cursor is self._head:
            self._head = self._head.next
            self._head.prev = None
            self._cursor = self._head
            return
        if self._cursor is self._tail:
            self._tail = self._tail.prev
            self._tail.next = None
            self._cursor = self._tail
            return
        self._cursor.prev.next = self._cursor.next
        self._cursor.next.prev = self._cursor.prev
        self._cursor = self._cursor.next

    def remove_all(self, value):
        """
        постусловие:
        1) в списке нет заданных значений
        2) курсор указывает (первый из имеющихся) - на текущий узел, на правого соседа, на левого соседа, на head"""
        self.find(value)
        while self.get_find_status() != ParentLinkedList.FIND_ERR:
            self.remove()
            self.find(value)

    def clear(self):
        """
        постусловие:
        1) список пуст
        2) курсор указывает на head
        3) статусы операций не указывают на ошибки"""
        self._head = None
        self._tail = None
        self._cursor = None
        self._right_status = ParentLinkedList.RIGHT_OK
        self._left_status = ParentLinkedList.LEFT_OK
        self._find_status = ParentLinkedList.FIND_R
        self._get_status = ParentLinkedList.GET_OK

    # ЗАПРОСЫ
    def get(self):
        """
        предусловие - список не пуст"""
        if self._cursor is None:
            self._get_status = ParentLinkedList.GET_ERR
            return 0
        self._get_status = ParentLinkedList.GET_OK
        return self._cursor.value

    def size(self):
        if self._head is None:
            return 0
        cnt = 1
        node = self._head
        while node.next is not None:
            cnt += 1
            node = node.next
        return cnt

    def is_head(self):
        return self._cursor is self._head

    def is_tail(self):
        return self._cursor is self._tail

    def is_value(self):
        return self._cursor is not None

    # ЗАПРОСЫ СТАТУСОВ
    def get_right_status(self):
        return self._right_status

    def get_left_status(self):
        return self._left_status

    def get_find_status(self):
        return self._find_status

    def get_get_status(self):
        return self._get_status


class LinkedList(ParentLinkedList):
    pass


class TwoWayList(ParentLinkedList):
    def left(self):
        """
        предусловие: слева от курсора есть элементы
        постусловие: курсор указывает на узел перед текущим"""
        if self._cursor is None or self._cursor.prev is None:
            self._left_status = ParentLinkedList.LEFT_ERR
            return
        self._left_status = ParentLinkedList.LEFT_OK
        self._cursor = self._cursor.prev
