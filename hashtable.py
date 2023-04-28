class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        return sum(value.encode()) % self.size

    def seek_slot(self, value):
        cnt = 1
        i = sum(value.encode()) % self.size
        if self.slots[i] is None:
            return i
        while cnt < self.size:
            i = (i + self.step) % self.size
            if self.slots[i] is None:
                return i
            cnt += 1
        return None

    def put(self, value):
        i = self.seek_slot(value)
        if i is not None:
            self.slots[i] = value
        return i

    def find(self, value):
        i = self.hash_fun(value)
        cnt = 1
        while cnt <= self.size:
            if self.slots[i] == value:
                return i
            i = (i + self.step) % self.size
            cnt += 1
        return None
