from hash_table import HashTable

class PowerSet(HashTable):

    def __init__(self):
        """
        Создано множество на 20_000 значений строкового типа"""
        self._capacity = 20_000
        super().__init__(self._capacity)

    # КОМАНДЫ
    # закомментированные методы - наследуются из HashTable

    # def put(self, value):
    #     """
    #     Предусловие - есть свободный слот с подходящим индексом
    #     Постусловие - value записано в слот с подходящим индексом"""
    #     pass

    # def remove(self, value):
    #     """
    #     Предусловие - value содержится в хэш-таблице
    #     Постусловие - value удалено из хэш-таблицы"""
    #     pass

    ##### ЗАПРОСЫ
    # закомментированные методы - наследуются из HashTable

    # def _hash_fun(self, value):  
    #     """
    #     Возвращает корректный индекс"""
    #     return 0

    # def _seek_slot(self, value):
    #     """
    #     Проверяется наличие свободного слота с подходящим индексом (по хэш-функции, +_step или +2*_step)
    #     Возвращает индекс или -2 (TOO_MANY_COLLISIONS)"""
    #     return 0

    # def __contains__(self, value):
    #     """
    #     Проверяет принадлежность значения value хэш-таблице
    #     реализует value in self"""
    #     return 0
    
    # def get(self, value):
    #     """
    #     Проверяет принадлежность значения value хэш-таблице"""
    #     return 0        

    # def get_put_status(self):
    #     return 0

    # def get_remove_status(self):
    #     return 0

    # def size(self):
    #     return 0

    def intersection(self, set2):
        """
        пересечение текущего множества и set2"""
        result = PowerSet()
        for x in self:
            if x in set2:
                result.put(x)
        return result 

    def union(self, set2):
        """
        объединение текущего множества и set2"""
        result = PowerSet()
        for x in self:
            result.put(x)
        for x in set2:
            result.put(x)
        return result 

    def difference(self, set2):
        """
        разница текущего множества и set2"""
        result = PowerSet()
        for x in self:
            if x not in set2:
                result.put(x)
        return result 

    def issubset(self, set2):
        len_set_2 = set2.size()
        if self.size() < len_set_2:
            return False
        for x in set2:
            if x not in self:
                return False
        return True
    
    def __iter__(self):
        i = 0
        while i < self._capacity:
            if self._slots[i] is not None:
                yield self._slots[i]
            i += 1
    