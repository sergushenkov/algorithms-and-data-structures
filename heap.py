class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    def MakeHeap(self, array, depth):
        size = 2 ** (depth + 1) - 1
        self.HeapArray = [None] * size
        if len(array) > size:
            array = array[:size]
        for number in array:
            self.Add(number)

    def GetMax(self):
        last_key_index = len(self.HeapArray) - 1
        while last_key_index >= 0 and self.HeapArray[last_key_index] is None:
            last_key_index -= 1
        if last_key_index == -1:
            return -1
        max_key = self.HeapArray[0]
        if last_key_index == 0:
            self.HeapArray[0] = None
            return max_key
        parent = self.HeapArray[last_key_index]
        self.HeapArray[last_key_index] = None
        self.HeapArray[0] = parent
        parent_index = 0
        while True:
            first_child_index = parent_index * 2 + 1
            first_child = None
            if first_child_index < last_key_index:
                first_child = self.HeapArray[first_child_index]
            if first_child is None:
                first_child = -1
            second_child_index = parent_index * 2 + 2
            second_child = None
            if second_child_index < last_key_index:
                second_child = self.HeapArray[second_child_index]
            if second_child is None:
                second_child = -1
            if parent >= first_child and parent >= second_child:
                return max_key
            if parent < first_child and second_child < first_child:
                self.HeapArray[parent_index] = first_child
                parent_index = first_child_index
            else:
                self.HeapArray[parent_index] = second_child
                parent_index = second_child_index
            self.HeapArray[parent_index] = parent

    def Add(self, key):
        is_zero_size_heap = len(self.HeapArray) == 0
        if is_zero_size_heap:
            return False

        is_complete_heap = self.HeapArray[len(self.HeapArray) - 1] is not None
        if is_complete_heap:
            return False

        last_key_index = len(self.HeapArray) - 1
        while last_key_index >= 0 and self.HeapArray[last_key_index] is None:
            last_key_index -= 1

        key_index = last_key_index + 1
        self.HeapArray[key_index] = key
        while key_index > 0 and key >= self.HeapArray[(key_index - 1) // 2]:
            self.HeapArray[key_index] = self.HeapArray[(key_index - 1) // 2]
            self.HeapArray[(key_index - 1) // 2] = key
            key_index = (key_index - 1) // 2
        return True


'''
При создании пирамиды с нуля с помощью подобной операции вставки сложность в наихудшем случае будет O(log2 N) (количество передвижений узла по дереву не превысит его глубину), а в наилучшем O(1) (элементы сразу встают на свои позиции).
Задание. Реализуйте бинарную пирамиду по аналогии с деревом на базе массива. Создавайте её операцией Make-Heap -- формированием из последовательного набора входных значений.
Добавьте методы удаления максимально приоритетного элемента и вставки нового элемента.
'''
