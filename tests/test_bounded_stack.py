from bounded_stack import BoundedStack


def test_class_vars():
    assert BoundedStack.POP_NIL == 0
    assert BoundedStack.POP_OK == 1
    assert BoundedStack.POP_ERR == 2
    assert BoundedStack.PEEK_NIL == 0
    assert BoundedStack.PEEK_OK == 1
    assert BoundedStack.PEEK_ERR == 2
    assert BoundedStack.PUSH_NIL == 0
    assert BoundedStack.PUSH_OK == 1
    assert BoundedStack.PUSH_ERR == 2


def test_init():
    stack = BoundedStack(10)
    assert stack.size() == 0
    assert stack.get_pop_status() == BoundedStack.POP_NIL
    assert stack.get_push_status() == BoundedStack.PUSH_NIL
    assert stack.get_peek_status() == BoundedStack.PEEK_NIL


def test_push():
    stack = BoundedStack(2)

    assert stack.pop() is None
    assert stack.size() == 0
    assert stack.get_pop_status() == BoundedStack.POP_ERR
    assert stack.get_push_status() == BoundedStack.PUSH_NIL
    assert stack.get_peek_status() == BoundedStack.PEEK_NIL

    stack.push(1)
    assert stack.size() == 1
    assert stack.get_pop_status() == BoundedStack.POP_ERR
    assert stack.get_push_status() == BoundedStack.PUSH_OK
    assert stack.get_peek_status() == BoundedStack.PEEK_NIL

    stack.push(0)
    assert stack.size() == 2
    assert stack.get_pop_status() == BoundedStack.POP_ERR
    assert stack.get_push_status() == BoundedStack.PUSH_OK
    assert stack.get_peek_status() == BoundedStack.PEEK_NIL

    stack.push(2)
    assert stack.size() == 2
    assert stack.get_pop_status() == BoundedStack.POP_ERR
    assert stack.get_push_status() == BoundedStack.PUSH_ERR
    assert stack.get_peek_status() == BoundedStack.PEEK_NIL

def test_peek():
    stack = BoundedStack(2)
    assert stack.peek() == 0
    assert stack.size() == 0
    assert stack.get_pop_status() == BoundedStack.POP_NIL
    assert stack.get_push_status() == BoundedStack.PUSH_NIL
    assert stack.get_peek_status() == BoundedStack.PEEK_ERR

    stack.push(1)
    assert stack.peek() == 1
    assert stack.size() == 1
    assert stack.get_pop_status() == BoundedStack.POP_NIL
    assert stack.get_push_status() == BoundedStack.PUSH_OK
    assert stack.get_peek_status() == BoundedStack.PEEK_OK

    assert stack.pop() is None
    assert stack.size() == 0
    assert stack.get_pop_status() == BoundedStack.POP_OK
    assert stack.get_push_status() == BoundedStack.PUSH_OK
    assert stack.get_peek_status() == BoundedStack.PEEK_OK

def test_clear():
    stack = BoundedStack(2)
    stack.pop()
    stack.push(1)
    stack.peek()
    stack.clear()
    assert stack.size() == 0
    assert stack.get_pop_status() == BoundedStack.POP_NIL
    assert stack.get_push_status() == BoundedStack.PUSH_NIL
    assert stack.get_peek_status() == BoundedStack.PEEK_NIL