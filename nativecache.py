class NativeCache:
    def __init__(self, sz, stp=7):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        return sum(key.encode()) % self.size

    def seek_slot(self, key):
        cnt = 1
        i = self.hash_fun(key)
        if self.slots[i] is None or self.slots[i] == key:
            return i
        while cnt < self.size:
            i = (i + self.step) % self.size
            if self.slots[i] is None:
                return i
            cnt += 1
        min_hit = self.hits[0]
        min_hit_idx = 0
        for k in range(1, self.size):
            if min_hit > self.hits[k]:
                min_hit = self.hits[k]
                min_hit_idx = k
        return min_hit_idx

    def is_key(self, key):
        i = self.hash_fun(key)
        cnt = 1
        while cnt <= self.size:
            if self.slots[i] == key:
                self.hits[i] += 1
                return True
            i = (i + self.step) % self.size
            cnt += 1
        return False

    def put(self, key, value):
        i = self.seek_slot(key)
        self.slots[i] = key
        self.values[i] = value
        self.hits[i] = 0

    def get(self, key):
        i = self.hash_fun(key)
        cnt = 1
        while cnt <= self.size:
            if self.slots[i] == key:
                self.hits[i] += 1
                return self.values[i]
            i = (i + self.step) % self.size
            cnt += 1
        return None
