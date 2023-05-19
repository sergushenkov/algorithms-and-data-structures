class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.full_mask = 2 ** f_len - 1
        self.array = 0

    def hash1(self, str1):
        mult = 17
        mask = 0
        for c in str1:
            mask = (mask * mult + ord(c)) % self.filter_len
        return mask

    def hash2(self, str1):
        mult = 223
        mask = 0
        for c in str1:
            mask = (mask * mult + ord(c)) % self.filter_len
        return mask

    def add(self, str1):
        self.array = self.array | self.hash1(str1) | self.hash2(str1)

    def is_value(self, str1):
        mask = self.full_mask ^ (self.hash1(str1) | self.hash2(str1))
        return (self.array | mask) == self.full_mask
