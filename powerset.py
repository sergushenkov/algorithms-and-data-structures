# наследуйте этот класс от HashTable
# или расширьте его методами из HashTable
class PowerSet:

    def __init__(self):
        self.max_len = 100_000
        self.slots = [None] * self.max_len

    def size(self):
        cnt = 0
        for i in range(self.max_len):
            if self.slots[i] is not None:
                cnt += 1
        return cnt

    def put(self, value):
        self.slots[sum(value.encode()) % self.max_len] = value

    def get(self, value):
        return self.slots[sum(value.encode()) % self.max_len] == value

    def remove(self, value):
        if self.slots[sum(value.encode()) % self.max_len] == value:
            self.slots[sum(value.encode()) % self.max_len] = None
            return True
        return False

    def intersection(self, set2):
        result = PowerSet()
        for i in range(self.max_len):
            if self.slots[i] is not None and set2.get(self.slots[i]):
                result.slots[i] = self.slots[i]
        return result

    def union(self, set2):
        result = PowerSet()
        for i in range(self.max_len):
            if self.slots[i] is not None:
                result.slots[i] = self.slots[i]
                continue
            result.slots[i] = set2.slots[i]
        return result

    def difference(self, set2):
        result = PowerSet()
        for i in range(self.max_len):
            if self.slots[i] is not None and not(set2.get(self.slots[i])):
                result.slots[i] = self.slots[i]
        return result

    def issubset(self, set2):
        for i in range(self.max_len):
            if set2.slots[i] is not None and not(self.get(set2.slots[i])):
                return False
        return True
