from hash_table import HashTable


def test_init():
    capacity = 10
    hash_table = HashTable(capacity)
    assert hash_table.capacity() == capacity
    assert hash_table.get_put_status() == HashTable.PUT_STATUS_OK
    assert hash_table.get_remove_status() == HashTable.REMOVE_STATUS_OK


def test_put_str():
    hash_table = HashTable(3)
    assert "b" not in hash_table
    hash_table.put("b")
    assert hash_table.get_put_status() == HashTable.PUT_STATUS_OK
    assert "b" in hash_table


def test_put_double():
    hash_table = HashTable(3)
    hash_table.put([])
    assert hash_table.get_put_status() == HashTable.PUT_STATUS_NOT_HASH
    hash_table.put("a")
    hash_table.put("a")
    assert hash_table.get_put_status() == HashTable.PUT_STATUS_OK
    hash_table.put("a")
    hash_table.put("a")
    assert hash_table.get_put_status() == HashTable.PUT_STATUS_OK
    hash_table.put("b")
    hash_table.put("c")
    assert hash_table.get_put_status() == HashTable.PUT_STATUS_OK
    hash_table.put("d")
    assert hash_table.get_put_status() == HashTable.PUT_STATUS_NOT_FREE_SLOT
    assert "a" in hash_table
    assert "b" in hash_table
    assert "c" in hash_table
    assert "d" not in hash_table
    assert [] not in hash_table


def test_put_double_hash():
    hash_table = HashTable(4)
    hash_table.put(1)
    assert hash_table.get_put_status() == HashTable.PUT_STATUS_OK
    hash_table.put(5)
    assert hash_table.get_put_status() == HashTable.PUT_STATUS_OK
    hash_table.put(9)
    assert hash_table.get_put_status() == HashTable.PUT_STATUS_OK
    hash_table.put(13)
    assert hash_table.get_put_status() == HashTable.PUT_STATUS_TOO_MANY_COLLISIONS
    hash_table.put(12)
    assert hash_table.get_put_status() == HashTable.PUT_STATUS_OK
    assert 1 in hash_table
    assert 5 in hash_table
    assert 9 in hash_table
    assert 12 in hash_table
    assert 13 not in hash_table


def test_remove():
    hash_table = HashTable(4)
    hash_table.remove(5)
    assert hash_table.get_remove_status() == HashTable.REMOVE_STATUS_VALUE_NOT_FOUND
    for i in (1, 5, 9, 12):
        hash_table.put(i)
        assert i in hash_table
    hash_table.remove(5)
    assert hash_table.get_remove_status() == HashTable.REMOVE_STATUS_OK
    assert 5 not in hash_table
    hash_table.put(13)
    assert hash_table.get_put_status() == HashTable.PUT_STATUS_OK
    assert 13 in hash_table
