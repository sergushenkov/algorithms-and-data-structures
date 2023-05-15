'''Некорректный размер множества после добавления элементов'''


class PowerSet:

    def __init__(self):
        self.max_len = 100_000
        self.step = 17
        self.slots = [None] * self.max_len

    def size(self):
        cnt = 0
        for i in range(self.max_len):
            if self.slots[i] is not None:
                cnt += 1
        return cnt

    def put(self, value):
        cnt = 0
        i = sum(value.encode()) % self.max_len
        while cnt < self.max_len:
            if self.slots[i] is None:
                self.slots[i] = value
                return
            if self.slots[i] == value:
                return
            i = (i + self.step) % self.max_len
            cnt += 1

    def get(self, value):
        i = sum(value.encode()) % self.max_len
        cnt = 0
        while cnt < self.max_len:
            if self.slots[i] is None:
                return False
            if self.slots[i] == value:
                return True
            i = (i + self.step) % self.max_len
            cnt += 1

    def remove(self, value):
        i = sum(value.encode()) % self.max_len
        cnt = 0
        while cnt < self.max_len:
            if self.slots[i] is None:
                return False
            if self.slots[i] == value:
                self.slots[i] = None
                return True
            i = (i + self.step) % self.max_len
            cnt += 1        

    def intersection(self, set2):
        result = PowerSet()
        for i in range(self.max_len):
            if self.slots[i] is not None and set2.get(self.slots[i]):
                result.put(self.slots[i])
        return result

    def union(self, set2):
        result = PowerSet()
        for i in range(self.max_len):
            if self.slots[i] is not None:
                result.put(self.slots[i])
            if set2.slots[i] is not None:
                result.put(set2.slots[i])
        return result

    def difference(self, set2):
        result = PowerSet()
        for i in range(self.max_len):
            if self.slots[i] is not None and not(set2.get(self.slots[i])):
                result.put(self.slots[i])
        return result

    def issubset(self, set2):
        for i in range(self.max_len):
            if set2.slots[i] is not None and not(self.get(set2.slots[i])):
                return False
        return True
