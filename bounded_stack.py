class BoundedStack:
    # интерфейс класса, реализующий АТД Stack
    POP_NIL = 0
    POP_OK = 1
    POP_ERR = 2
    PEEK_NIL = 0
    PEEK_OK = 1
    PEEK_ERR = 2
    PUSH_NIL = 0
    PUSH_OK = 1
    PUSH_ERR = 2

    def __init__(self, capacity=32):
        # скрытые поля
        self._stack = []  # основное хранилище стека
        self._capacity = capacity  # максимально допустимое количество элементов в стеке
        self._push_status = self.PUSH_NIL  # статус запроса peek()
        self._peek_status = self.PEEK_NIL  # статус запроса peek()
        self._pop_status = self.POP_NIL  # статус команды pop()

    def push(self, value):
        self._push_status = self.PUSH_ERR
        if len(self._stack) < self._capacity:
            self._stack.append(value)
            self._push_status = self.PUSH_OK

    def pop(self):
        self._pop_status = self.POP_ERR
        if len(self._stack) > 0:
            self._stack.pop()
            self._pop_status = self.POP_OK

    def clear(self):
        self._stack = []  # пустой список/стек
        self._push_status = self.PUSH_NIL  # начальный статус запроса peek()
        self._peek_status = self.PEEK_NIL  # начальный статус запроса peek()
        self._pop_status = self.POP_NIL  # начальный статус команды pop()

    def peek(self):
        result = 0
        self._peek_status = self.PEEK_ERR
        if len(self._stack) > 0:
            result = self._stack[-1]
            self._peek_status = self.PEEK_OK
        return result

    def size(self):
        return len(self._stack)

    # запросы статусов
    def get_pop_status(self):
        return self._pop_status

    def get_peek_status(self):
        return self._peek_status

    def get_push_status(self):
        return self._push_status
