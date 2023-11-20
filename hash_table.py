class HashTable:
    PUT_STATUS_OK = 0
    PUT_STATUS_NOT_HASH = 1
    PUT_STATUS_NOT_FREE_SLOT = 2
    PUT_STATUS_TOO_MANY_COLLISIONS = 2
    REMOVE_STATUS_OK = 0
    REMOVE_STATUS_NOT_HASH = 1
    REMOVE_STATUS_VALUE_NOT_FOUND = 2

    def __init__(self, capacity):
        self._capacity = capacity
        self._slots = [None] * self._capacity
        self._step = 3  # количество попыток обойти коллизию, >= 1
        self._shift = 7  # смещение ячейки в случае коллизии
        self._put_status = self.PUT_STATUS_OK
        self._remove_status = self.REMOVE_STATUS_OK

    def _hash_fun(self, value):
        """
        Возвращает корректный индекс или -1 (если в качестве value - не хэшируемое значение)"""
        try:
            return abs(hash(value)) % self._capacity
        except Exception:
            return -1

    def _seek_slot(self, value):
        """
        Проверяется наличие свободного слота с подходящим индексом (по хэш-функции, +_step или +2*_step)"""
        index = self._hash_fun(value)
        if index == -1:
            return -1
        for _ in range(self._step):
            if self._slots[index] is None or self._slots[index] == value:
                return index
            index = (index + self._shift) % self._capacity
        return -2

    def put(self, value):
        """
        Предусловие:
        1) в качестве value поступает хэшируемое значение
        2) есть свободный слот с подходящим индексом
        Постусловие - value записано в слот с подходящим индексом"""
        index = self._seek_slot(value)
        if index == -1:
            self._put_status = self.PUT_STATUS_NOT_HASH
            return
        if index == -2:
            self._put_status = self.PUT_STATUS_NOT_FREE_SLOT
            return
        self._slots[index] = value
        self._put_status = self.PUT_STATUS_OK

    def remove(self, value):
        """
        Предусловие:
        1) в качестве value поступает хэшируемое значение
        2) value содержится в хэш-таблице
        Постусловие - value удалено из хэш-таблицы"""
        index = self._seek_slot(value)
        if index == -1:
            self._remove_status = self.REMOVE_STATUS_NOT_HASH
            return
        if index is not None and self._slots[index] == value:
            self._slots[index] = None
            self._remove_status = self.REMOVE_STATUS_OK
            return
        self._remove_status = self.REMOVE_STATUS_VALUE_NOT_FOUND

    def __contains__(self, value):
        """
        Проверяет принадлежность значения value хэш-таблице"""
        index = self._seek_slot(value)
        if index is not None and self._slots[index] == value:
            return True
        return False

    def get_put_status(self):
        return self._put_status

    def get_remove_status(self):
        return self._remove_status

    def capacity(self):
        return self._capacity
