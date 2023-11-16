from queue_asd import Queue, Dequeue


def test_queue_init():
    tq = Queue()
    assert tq.size() == 0
    assert tq.get_get_status() == Queue.GET_ERR
    assert tq.get_remove_status() == Queue.REMOVE_ERR


def test_queue_add_tail():
    tq = Queue()
    assert tq.size() == 0
    tq.add_tail(0)
    assert tq.size() == 1
    tq.add_tail(1)
    assert tq.size() == 2


def test_queue_get():
    tq = Queue()
    assert tq.get_head() is None
    assert tq.get_get_status() == Queue.GET_ERR
    tq.add_tail(0)
    assert tq.get_head() == 0
    assert tq.get_get_status() == Queue.GET_OK
    tq.add_tail(1)
    assert tq.get_head() == 0


def test_queue_remove_front():
    tq = Queue()
    for i in range(3):
        tq.add_tail(i)
    assert tq.get_head() == 0
    tq.remove_front()
    assert tq.size() == 2
    assert tq.get_head() == 1
    assert tq.get_get_status() == Queue.GET_OK
    tq.remove_front()
    tq.remove_front()
    assert tq.get_head() is None
    assert tq.get_get_status() == Queue.GET_ERR
    assert tq.get_remove_status() == Queue.REMOVE_OK
    assert tq.size() == 0
    tq.remove_front()
    assert tq.get_remove_status() == Queue.REMOVE_ERR
    assert tq.size() == 0


def test_dequeue_init():
    dq = Dequeue()
    assert dq.size() == 0
    assert dq.get_get_status() == Dequeue.GET_ERR
    assert dq.get_remove_status() == Dequeue.REMOVE_ERR


def test_dequeue_add_front():
    dq = Dequeue()
    dq.add_front(1)
    assert dq.size() == 1
    dq.add_front(2)
    assert dq.size() == 2
    dq.add_front(3)
    assert dq.size() == 3
    assert dq.get_head() == 3
    assert dq.get_get_status() == Dequeue.GET_OK
    dq.remove_front()
    assert dq.get_remove_status() == Dequeue.REMOVE_OK
    assert dq.size() == 2
    assert dq.get_head() == 2
    assert dq.get_get_status() == Dequeue.GET_OK
    dq.remove_front()
    assert dq.get_head() == 1
    assert dq.size() == 1


def test_dequeue_remove_tail():
    dq = Dequeue()
    dq.remove_tail()
    assert dq.size() == 0
    assert dq.get_remove_status() == Dequeue.REMOVE_ERR
    dq.add_front(1)
    dq.add_front(2)
    assert dq.get_tail() == 1
    dq.remove_tail()
    assert dq.get_remove_status() == Dequeue.REMOVE_OK
    assert dq.size() == 1
    assert dq.get_tail() == 2
    dq.remove_tail()
    assert dq.get_remove_status() == Dequeue.REMOVE_OK
    assert dq.size() == 0
    assert dq.get_tail() is None
    dq.remove_tail()
    assert dq.get_remove_status() == Dequeue.REMOVE_ERR
    assert dq.size() == 0
