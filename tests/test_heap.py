from heap import Heap


def test_get_max():
    heap = Heap()
    assert heap.GetMax() == -1

    heap.HeapArray.append(11)
    assert heap.GetMax() == 11
    assert heap.HeapArray[0] is None
    len(heap.HeapArray) == 0

    heap.HeapArray = list((11, 9, 4, 7, 8, 3, 1, 2, 5, 6,
                          None, None, None, None, None))
    len_heap_array = 10
    len(heap.HeapArray) == len_heap_array
    for number in (11, 9, 8, 7, 6, 5, 4, 3, 2, 1):
        assert heap.GetMax() == number
        len_heap_array -= 1
        len(heap.HeapArray) == len_heap_array


def test_add():
    heap = Heap()
    assert len(heap.HeapArray) == 0
    assert heap.Add(5) is False
    assert len(heap.HeapArray) == 0

    heap.HeapArray = list((None,))
    assert len(heap.HeapArray) == 1
    assert heap.Add(5) is True
    assert len(heap.HeapArray) == 1

    heap.HeapArray = list((11, 9, 4, 7, 8, 3, 1, 2, 5, 6,
                          None, None, None, None, None))
    assert len(heap.HeapArray) == 15
    for number, index in zip((13, 12, 10, 14, 15), (0, 2, 5, 0, 0)):
        assert heap.Add(number) is True
        assert heap.HeapArray[index] == number
    assert len(heap.HeapArray) == 15
    assert heap.Add(16) is False
    assert len(heap.HeapArray) == 15
    for i, number in enumerate((15, 11, 14, 7, 9, 10, 13, 2, 5, 6, 8, 3, 4, 1, 12)):
        assert heap.HeapArray[i] == number


def test_make_heap():
    heap = Heap()
    heap.MakeHeap((1, 2), 0)
    assert len(heap.HeapArray) == 1
    assert heap.HeapArray[0] == 1

    heap.MakeHeap((), 1)
    assert len(heap.HeapArray) == 3
    for key in heap.HeapArray:
        assert key is None

    heap.MakeHeap((1, 2, 3), 1)
    for i, number in enumerate((3, 1, 2)):
        assert heap.HeapArray[i] == number
