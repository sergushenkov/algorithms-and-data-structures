class BloomFilter:
    ADD_STATUS_OK = 0
    ADD_STATUS_NOT_CHANGE = 1

    def __init__(self, f_len):
        self._filter_len = f_len
        self._full_mask = 2**f_len - 1
        self._array = 0
        self._add_status = self.ADD_STATUS_NOT_CHANGE

    ##### КОМАНДЫ
    def add(self, str1):
        if self.is_value(str1):
            self._add_status = self.ADD_STATUS_NOT_CHANGE
            return
        self._array = self._array | self._hash1(str1) | self._hash2(str1)  # битовое ИЛИ
        self._add_status = self.ADD_STATUS_OK

    ##### ЗАПРОСЫ
    def _hash1(self, str1):
        mult = 17
        mask = 0
        for c in str1:
            mask = (mask * mult + ord(c)) % self._filter_len
        return mask

    def _hash2(self, str1):
        mult = 223
        mask = 0
        for c in str1:
            mask = (mask * mult + ord(c)) % self._filter_len
        return mask

    def is_value(self, str1):
        mask = self._full_mask ^ (
            self._hash1(str1) | self._hash2(str1)
        )  # битовое исключающее ИЛИ
        return (self._array | mask) == self._full_mask

    def get_filter_len(self):
        return self._filter_len

    def get_add_status(self):
        return self._add_status
