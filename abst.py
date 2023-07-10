class aBST:

    def __init__(self, depth):
        self.size = 2 ** (depth + 1) - 1
        self.Tree = [None] * self.size

    def FindKeyIndex(self, key):
        i = 0
        while i < self.size:
            current_key = self.Tree[i]
            if current_key is None:
                return -i
            if current_key == key:
                return i
            if key < current_key:
                i = i * 2 + 1
            else:
                i = i * 2 + 2
        return None

    def AddKey(self, key):
        index = self.FindKeyIndex(key)
        if index is None:
            return -1
        if index <= 0:
            self.Tree[-index] = key
        return abs(index)
