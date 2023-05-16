# powerset over dictionary
class PowerSet:

    def __init__(self):
        self.dict = {}


    def size(self):
        return len(self.dict)


    def put(self, value):
        self.dict[value] = True


    def get(self, value):
        return self.dict.get(value, False)

    def remove(self, value):
        if value in self.dict:
            del self.dict[value]
            return True
        return False

    def intersection(self, set2):
        result = PowerSet()
        for key in self.dict:
            if key in set2.dict:
                result.put(key)
        return result 

    def union(self, set2):
        result = PowerSet()
        for key in self.dict:
            result.put(key)
        for key in set2.dict:
            result.put(key)
        return result

    def difference(self, set2):
        result = PowerSet()
        for key in self.dict:
            if key not in set2.dict:
                result.put(key)
        return result

    def issubset(self, set2):
        for key in set2.dict:
            if key not in self.dict:
                return False
        return True