import ctypes
from typing import Any


class DynArray:

    def __init__(self) -> None:
        self.count: int = 0
        self.capacity: int = 16
        self.array: ctypes.Array[ctypes.py_object] = self.make_array(
            self.capacity)

    def __len__(self) -> int:
        return self.count

    def make_array(self, new_capacity) -> ctypes.Array[ctypes.py_object]:
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i: int):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity: int) -> None:
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm: Any) -> None:
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i: int, itm) -> None:
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        if i == self.count:
            self.array[i] = itm
            self.count += 1
            return
        for j in range(self.count, i, -1):
            self.array[j] = self.array[j - 1]
        self.array[i] = itm
        self.count += 1

    def delete(self, i: int) -> None:
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        for j in range(i, self.count - 1):
            self.array[j] = self.array[j + 1]
        self.count -= 1
        if self.count < self.capacity / 2 and self.capacity >= 16:
            self.resize(max(int(self.capacity / 1.5), 16))
