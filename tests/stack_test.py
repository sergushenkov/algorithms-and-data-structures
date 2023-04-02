import sys
import unittest

sys.path.insert(0, "..")

from stack import Stack


class TestFunction(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack()

    def test_size(self):
        self.assertEqual(self.stack.size(), 0, "empty stack size is not zero")
        for i in range(10):
            self.stack.push(i)

    def test_push_peek_pop(self):
        self.assertIsNone(self.stack.peek(), "empty stack.peek() is not None")
        self.assertIsNone(self.stack.pop(), "empty stack.pop() is not None")
        for i in range(10):
            self.assertEqual(self.stack.size(), i, "size stack is not correct")
            self.stack.push(i)
            self.assertEqual(self.stack.peek(), i, "stack.peek() is not correct")
        for i in range(9, -1, -1):
            self.assertEqual(self.stack.peek(), i, "stack.peek() is not correct")
            self.assertEqual(self.stack.pop(), i, "stack.pop() is not correct")
            self.assertEqual(self.stack.size(), i, "size stack is not correct")
        self.assertIsNone(self.stack.peek(), "empty stack.peek() is not None")
        self.assertIsNone(self.stack.pop(), "empty stack.pop() is not None")
        self.assertIsNone(self.stack.peek(), "empty stack.peek() is not None")
        self.assertIsNone(self.stack.pop(), "empty stack.pop() is not None")


if __name__ == "__main__":
    unittest.main()
