import ctypes


class DynamicArray:
    INSERT_OK = 1  # последний insert() отработал нормально
    INSERT_ERR = 2  # insert() обращается к элементу с недопустимым индексом

    DELETE_OK = 1  # последний delete() отработал нормально
    DELETE_ERR = 2  # delete() обращается к элементу с недопустимым индексом

    GET_OK = 1  # последний get() отработал нормально
    GET_ERR = 2  # get() обращается к элементу с недопустимым индексом

    DEFAULT_CAPACITY = 16

    def __init__(self):
        """
        постусловие:
        1) создан пустой динамический массив размера _capacity
        2) статусы операций не указывают на ошибки"""
        self._count = 0
        self._capacity = DynamicArray.DEFAULT_CAPACITY
        self._array = self._make_array(self._capacity)
        self._insert_status = DynamicArray.INSERT_OK
        self._delete_status = DynamicArray.DELETE_OK
        self._get_status = DynamicArray.GET_OK

    def __len__(self):
        return self._count

    def __getitem__(self, i):
        if i < 0 or i >= self._count:
            raise IndexError("Index is out of bounds")
        return self._array[i]

    def _make_array(self, new_capacity):
        """
        приватный метод
        постусловие:
        1) создан пустой динамический массив размера new_capacity"""
        return (new_capacity * ctypes.py_object)()

    def _resize(self, new_capacity):
        """
        приватный метод
        постусловие:
        1) создан пустой динамический массив размера new_capacity
        2) значения из старого массива перенесены в новый
        3) атрибут _capacity = new_capacity"""
        new_array = self._make_array(new_capacity)
        for i in range(self._count):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity

    def append(self, value):
        """
        постусловие:
        1) если массив заполнен, то его размер удваивается
        2) добавляется значение в конец массива
        3) атрибут _count увеличивается на 1"""
        if self._count == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._count] = value
        self._count += 1

    def insert(self, i, value):
        """
        предусловие: значение индекса i >= 0 и i <= self._count
        постусловие:
        1) если массив заполнен, то его размер удваивается
        2) элемент массива с индексом i содержит значение value"""
        if i < 0 or i > self._count:
            self._insert_status = DynamicArray.INSERT_ERR
            return
        if self._count == self._capacity:
            self._resize(2 * self._capacity)
        self._array[i] = value
        self._count += 1
        self._insert_status = DynamicArray.INSERT_OK
        

    def delete(self, i):
        """
        предусловие: значение индекса i >= 0 и i < self._count
        постусловие:
        1) элемент массива с индексом i удаляется
        2) последующие элементы сдвигаются влево
        3) если размер массива меньше 1/2 от его емкости, то его емкость уменьшается в 1.5 раза (но емкость не может быть меньше DEFAULT_CAPACITY = 16)"""
        if i < 0 or i >= self._count:
            self._delete_status = DynamicArray.DELETE_ERR
            return
        for j in range(i, self._count - 1):
            self._array[j] = self._array[j + 1]
        self._array[self._count] = None
        self._count -= 1
        self._delete_status = DynamicArray.DELETE_OK
        if self._capacity > 24 and self._count < self._capacity / 2:
            self._resize(int(2 * self._capacity / 3))

    def clear(self):
        """
        постусловие:
        1) пустой динамический массив, емкость равна текущей _capacity
        2) статусы операций не указывают на ошибки"""
        self._count = 0
        self._array = self._make_array(self._capacity)
        self._insert_status = DynamicArray.INSERT_OK
        self._delete_status = DynamicArray.DELETE_OK
        self._get_status = DynamicArray.GET_OK

    def get_item(self, i):
        """
        предусловие: значение индекса i >= 0 и i < self._count"""
        if i < 0 or i >= self._count:
            self._get_status = DynamicArray.GET_ERR
            return 0
        self._get_status = DynamicArray.GET_OK
        return self._array[i]

    def get_capacity(self):
        return self._capacity
    
    def get_size(self):
        return self._count
    
    def get_insert_status(self):
        return self._insert_status

    def get_delete_status(self):
        return self._delete_status
    
    def get_get_status(self):
        return self._get_status