from queue_asd import Queue

def test_init():
    tq = Queue()
    assert tq.size() == 0
    assert tq.get_dequeue_status() == Queue.DEQUEUE_ERR
    assert tq.get_pop_status() == Queue.POP_ERR

def test_enqueue():
    tq = Queue()
    assert tq.size() == 0
    tq.enqueue(0)
    assert tq.size() == 1
    tq.enqueue(1)
    assert tq.size() == 2

def test_dequeue():
    tq = Queue()
    assert tq.dequeue() is None
    assert tq.get_dequeue_status() == Queue.DEQUEUE_ERR
    tq.enqueue(0)
    assert tq.dequeue() == 0
    assert tq.get_dequeue_status() == Queue.DEQUEUE_OK
    tq.enqueue(1)
    assert tq.dequeue() == 0

def test_pop():
    tq = Queue()
    for i in range(3):
        tq.enqueue(i)
    assert tq.dequeue() == 0
    tq.pop()
    assert tq.size() == 2
    assert tq.dequeue() == 1
    assert tq.get_dequeue_status() == Queue.DEQUEUE_OK
    tq.pop()
    tq.pop()
    assert tq.dequeue() is None
    assert tq.get_dequeue_status() == Queue.DEQUEUE_ERR
    assert tq.get_pop_status() == Queue.POP_OK
    assert tq.size() == 0
    tq.pop()
    assert tq.get_pop_status() == Queue.POP_ERR
    assert tq.size() == 0