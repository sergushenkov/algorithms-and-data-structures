from dynamic_array import DynamicArray
import pytest

def test_init():
    d = DynamicArray()
    assert len(d) == 0
    with pytest.raises(IndexError):
        d[0]
    assert d.get_capacity() == 16
    assert d.get_insert_status() == DynamicArray.INSERT_OK
    assert d.get_delete_status() == DynamicArray.DELETE_OK
    assert d.get_get_status() == DynamicArray.GET_OK

def test_append():
    d = DynamicArray()
    for i in range(16):
        d.append(i)
    assert len(d) == 16
    assert d.get_capacity() == 16
    d.append(16)
    assert len(d) == 17
    assert d.get_capacity() == 32

def test_insert():
    d = DynamicArray()
    d.insert(1, 1)
    assert d.get_insert_status() == DynamicArray.INSERT_ERR
    assert len(d) == 0
    d.insert(0, 1)
    assert d.get_insert_status() == DynamicArray.INSERT_OK
    assert len(d) == 1
    for i in range(1, 17):
        d.insert(i, str(i))
    assert len(d) == 17
    assert d.get_capacity() == 32
    assert d[10] == '10'
    d.insert(10, 10)
    assert d[10] == 10

def test_delete():
    d = DynamicArray()
    d.insert(0, 0)
    d.delete(1)
    assert d.get_delete_status() == DynamicArray.DELETE_ERR
    assert d.get_size() == 1
    d.delete(0)
    assert d.get_delete_status() == DynamicArray.DELETE_OK
    assert d.get_size() == 0
    d.delete(0)
    assert d.get_delete_status() == DynamicArray.DELETE_ERR
    assert d.get_size() == 0
    for i in range(17):
        d.insert(i, str(i))
    d.delete(3)
    assert d[3] == '4'
    assert d.get_delete_status() == DynamicArray.DELETE_OK
    assert d.get_size() == 16
    d.delete(0)
    assert d[0] == '1'
    assert d.get_size() == 15
    assert d.get_capacity() == 21
    for _ in range(5):
        d.delete(0)
    assert d.get_size() == 10
    assert d.get_capacity() == 21

def test_clear():
    d = DynamicArray()    
    for i in range(17):
        d.insert(i, str(i))
    d.clear()
    assert len(d) == 0
    with pytest.raises(IndexError):
        d[0]
    assert d.get_capacity() == 32
    assert d.get_insert_status() == DynamicArray.INSERT_OK
    assert d.get_delete_status() == DynamicArray.DELETE_OK
    assert d.get_get_status() == DynamicArray.GET_OK

def test_get():
    d = DynamicArray()
    d.insert(0, 1)
    assert d.get_item(1) == 0
    assert d.get_get_status() == DynamicArray.GET_ERR
    assert d.get_item(0) == 1
    assert d.get_get_status() == DynamicArray.GET_OK