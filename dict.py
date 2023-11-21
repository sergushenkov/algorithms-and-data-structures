class Dictionary:
    GET_STATUS_OK = 0
    GET_STATUS_ERR = 1  # not key
    REMOVE_STATUS_OK = 0
    REMOVE_STATUS_ERR = 1  # not key

    def __init__(self, capacity=1000):
        self._capacity = capacity
        self._slots = [None] * self._capacity
        self._values = [None] * self._capacity
        for i in range(self._capacity):
            self._slots[i] = []
            self._values[i] = []
        self._get_status = self.GET_STATUS_OK
        self._remove_status = self.REMOVE_STATUS_OK

    def _hash_fun(self, key):
        """
        в качестве key поступают строки!
        возвращает корректный индекс слота"""
        return abs(hash(key)) % self._capacity

    def is_key(self, key):
        """
        возвращает True если ключ имеется, иначе False"""
        if key in self._slots[self._hash_fun(key)]:
            return True
        return False

    def put(self, key, value):
        """
        Постусловие - сохранена переданная пара ключ-значение"""
        i = self._hash_fun(key)
        if key in self._slots[i]:
            self._values[i][self._slots[i].index(key)] = value
            return
        self._slots[i].append(key)
        self._values[i].append(value)

    def get(self, key):
        """
        Предусловие - key есть в данных
        возвращает value для key или None если ключ не найден"""
        i = self._hash_fun(key)
        if key in self._slots[i]:
            self._get_status = self.GET_STATUS_OK
            return self._values[i][self._slots[i].index(key)]
        self._get_status = self.GET_STATUS_ERR
        return None

    def remove(self, key):
        """
        Предусловие - key есть в данных
        Постусловие - пара key-value удалена из данных"""
        i = self._hash_fun(key)
        if key in self._slots[i]:
            self._remove_status = self.REMOVE_STATUS_OK
            self._values[i].pop(self._slots[i].index(key))
            self._slots[i].remove(key)
            return
        self._remove_status = self.REMOVE_STATUS_ERR
        return

    def get_get_status(self):
        return self._get_status

    def get_remove_status(self):
        return self._remove_status
