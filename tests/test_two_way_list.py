from two_way_list import LinkedList, TwoWayList


def test_class_vars():
    assert LinkedList.RIGHT_OK == 1
    assert LinkedList.RIGHT_ERR == 2
    assert LinkedList.LEFT_OK == 1
    assert LinkedList.LEFT_ERR == 2
    assert LinkedList.FIND_R == 1
    assert LinkedList.FIND_L == 2
    assert LinkedList.FIND_CUR == 3
    assert LinkedList.FIND_ERR == 4
    assert LinkedList.GET_OK == 1
    assert LinkedList.GET_ERR == 2


def test_init():
    linked_list = LinkedList()
    assert linked_list.size() == 0
    assert linked_list.get_right_status() == LinkedList.RIGHT_OK
    assert linked_list.get_left_status() == LinkedList.LEFT_OK
    assert linked_list.get_find_status() == LinkedList.FIND_R
    assert linked_list.get_get_status() == LinkedList.GET_OK


def test_add_tail():
    linked_list = LinkedList()
    linked_list.add_tail(1)
    value = linked_list.get()
    assert value == 1
    assert linked_list.get_get_status() == LinkedList.GET_OK
    linked_list.add_tail(2)
    value = linked_list.get()
    assert value == 1
    assert linked_list.get_get_status() == LinkedList.GET_OK
    linked_list.add_tail(3)
    value = linked_list.get()
    assert value == 1
    assert linked_list.get_get_status() == LinkedList.GET_OK


def test_get():
    linked_list = LinkedList()
    value = linked_list.get()
    assert value == 0
    assert linked_list.get_get_status() == LinkedList.GET_ERR
    linked_list.add_tail(0)
    value = linked_list.get()
    assert value == 0
    assert linked_list.get_get_status() == LinkedList.GET_OK


def test_size():
    linked_list = LinkedList()
    assert linked_list.size() == 0
    linked_list.add_tail(1)
    assert linked_list.size() == 1
    linked_list.add_tail(2)
    assert linked_list.size() == 2


def test_is_head():
    linked_list = LinkedList()
    assert linked_list.is_head()
    linked_list.add_tail(1)
    assert linked_list.is_head()
    linked_list.add_tail(2)
    assert linked_list.is_head()
    linked_list.right()
    assert not linked_list.is_head()


def test_right():
    linked_list = LinkedList()
    linked_list.right()
    assert linked_list.get_right_status() == LinkedList.RIGHT_ERR
    linked_list.add_tail(1)
    linked_list.right()
    assert linked_list.get_right_status() == LinkedList.RIGHT_ERR
    value = linked_list.get()
    assert value == 1
    linked_list.add_tail(2)
    linked_list.right()
    assert linked_list.get_right_status() == LinkedList.RIGHT_OK
    value = linked_list.get()
    assert value == 2
    linked_list.right()
    assert linked_list.get_right_status() == LinkedList.RIGHT_ERR
    value = linked_list.get()
    assert value == 2


def test_is_tail():
    linked_list = LinkedList()
    assert linked_list.is_tail()
    linked_list.add_tail(1)
    assert linked_list.is_tail()
    linked_list.add_tail(2)
    assert not linked_list.is_tail()
    linked_list.right()
    assert linked_list.is_tail()


def test_is_value():
    linked_list = LinkedList()
    assert not linked_list.is_value()
    linked_list.add_tail(1)
    assert linked_list.is_value()


def test_head():
    linked_list = LinkedList()
    linked_list.add_tail(1)
    linked_list.add_tail(2)
    linked_list.right()
    linked_list.head()
    assert linked_list.is_head()


def test_tail():
    linked_list = LinkedList()
    linked_list.add_tail(1)
    linked_list.add_tail(2)
    linked_list.tail()
    assert linked_list.is_tail()


def test_put_right():
    linked_list = LinkedList()
    linked_list.put_right(1)
    assert linked_list.size() == 1
    assert linked_list.get() == 1
    linked_list.put_right(2)
    assert linked_list.size() == 2
    assert linked_list.get() == 1
    linked_list.right()
    assert linked_list.is_tail()


def test_put_left():
    linked_list = LinkedList()
    linked_list.put_left(1)
    assert linked_list.size() == 1
    assert linked_list.get() == 1
    linked_list.put_left(2)
    assert linked_list.size() == 2
    assert linked_list.get() == 1


def test_replace():
    linked_list = LinkedList()
    linked_list.replace(1)
    assert linked_list.size() == 1
    assert linked_list.get() == 1
    linked_list.replace(2)
    assert linked_list.size() == 1
    assert linked_list.get() == 2


def test_find():
    linked_list = LinkedList()
    linked_list.add_tail(1)
    linked_list.add_tail(2)
    linked_list.add_tail(1)
    linked_list.add_tail(1)
    linked_list.find(2)
    assert linked_list.get_find_status() == LinkedList.FIND_R
    assert linked_list.get() == 2
    linked_list.find(2)
    assert linked_list.get_find_status() == LinkedList.FIND_CUR
    assert linked_list.get() == 2
    linked_list.find(1)
    assert linked_list.get_find_status() == LinkedList.FIND_R
    assert linked_list.get() == 1
    assert not linked_list.is_tail()
    assert not linked_list.is_head()
    linked_list.find(1)
    assert linked_list.get_find_status() == LinkedList.FIND_R
    assert linked_list.get() == 1
    assert linked_list.is_tail()
    linked_list.find(1)
    assert linked_list.get_find_status() == LinkedList.FIND_L
    assert linked_list.get() == 1
    assert linked_list.is_head()
    linked_list.find(3)
    assert linked_list.get_find_status() == LinkedList.FIND_ERR
    assert linked_list.get() == 1
    assert linked_list.is_head()


def test_remove():
    linked_list = LinkedList()
    linked_list.remove()
    assert linked_list.size() == 0
    linked_list.add_tail(1)
    linked_list.remove()
    assert linked_list.size() == 0
    linked_list.add_tail(1)
    linked_list.put_left(2)
    linked_list.remove()
    assert linked_list.size() == 1
    assert linked_list.get() == 2
    linked_list.add_tail(3)
    linked_list.remove()
    assert linked_list.size() == 1
    assert linked_list.get() == 3
    linked_list.put_left(2)
    linked_list.add_tail(4)
    linked_list.remove()
    assert linked_list.size() == 2
    assert linked_list.get() == 4


def test_remove_all():
    linked_list = LinkedList()
    linked_list.add_tail(1)
    linked_list.add_tail(2)
    linked_list.add_tail(1)
    linked_list.add_tail(1)
    linked_list.remove_all(1)
    assert linked_list.size() == 1
    assert linked_list.get() == 2
    linked_list.remove_all(2)
    assert linked_list.size() == 0


def test_clear():
    linked_list = LinkedList()
    linked_list.right()
    linked_list.find(3)
    linked_list.add_tail(1)
    linked_list.add_tail(2)
    linked_list.clear()
    assert linked_list.size() == 0
    assert linked_list.get_right_status() == LinkedList.RIGHT_OK
    assert linked_list.get_left_status() == LinkedList.LEFT_OK
    assert linked_list.get_find_status() == LinkedList.FIND_R
    assert linked_list.get_get_status() == LinkedList.GET_OK


def test_TwoWayList_left():
    linked_list = TwoWayList()
    linked_list.left()
    assert linked_list.get_left_status() == LinkedList.LEFT_ERR
    linked_list.add_tail(1)
    linked_list.left()
    assert linked_list.get_left_status() == LinkedList.LEFT_ERR
    value = linked_list.get()
    assert value == 1
    linked_list.put_left(2)
    linked_list.left()
    assert linked_list.get_left_status() == LinkedList.LEFT_OK
    value = linked_list.get()
    assert value == 2
    linked_list.left()
    assert linked_list.get_left_status() == LinkedList.LEFT_ERR
    value = linked_list.get()
    assert value == 2
