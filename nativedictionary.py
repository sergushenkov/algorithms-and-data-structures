class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        return sum(key.encode()) % self.size

    def is_key(self, key):
        return self.slots[self.hash_fun(key)] == key

    def put(self, key, value):
        self.slots[self.hash_fun(key)] = key
        self.values[self.hash_fun(key)] = value

    def get(self, key):
        if self.is_key(key):
            return self.values[self.hash_fun(key)]
        return None
