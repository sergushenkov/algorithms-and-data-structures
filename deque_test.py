import unittest
from deque import Deque


class TestFunction(unittest.TestCase):
    def setUp(self):
        self.deque = Deque()

    def test_addFront_removeTail(self):
        self.assertIsNone(self.deque.removeTail(),
                          'empty deque return not None')
        self.assertIsNone(self.deque.head, 'head is not None')
        self.assertIsNone(self.deque.tail, 'tail is not None')
        for i in range(5):
            self.assertEqual(self.deque.size(), i, 'length is not correct')
            self.deque.addFront(i)
            self.assertIsNone(self.deque.head.prev, 'head.prev is not None')
            self.assertIsNone(self.deque.tail.next, 'tail.next is not None')
        self.assertEqual(self.deque.head.value, 4, 'tail.value is not correct')
        self.assertEqual(self.deque.head.next.value, 3,
                         'tail.value is not correct')
        self.assertEqual(self.deque.head.next.next.value,
                         2, 'tail.value is not correct')
        self.assertEqual(self.deque.head.next.next.next.value,
                         1, 'tail.value is not correct')
        self.assertEqual(self.deque.head.next.next.next.next.value,
                         0, 'tail.value is not correct')
        self.assertEqual(self.deque.head, self.deque.tail.prev.prev.prev.prev,
                         'deque is not correct')
        self.assertEqual(self.deque.head.next, self.deque.tail.prev.prev.prev,
                         'deque is not correct')
        self.assertEqual(self.deque.head.next.next, self.deque.tail.prev.prev,
                         'deque is not correct')
        self.assertEqual(self.deque.head.next.next.next, self.deque.tail.prev,
                         'deque is not correct')
        self.assertEqual(self.deque.head.next.next.next.next, self.deque.tail,
                         'deque is not correct')
        for i in range(5):
            self.assertEqual(self.deque.size(), 5 - i, 'length is not correct')
            self.assertIsNone(self.deque.head.prev, 'head.prev is not None')
            self.assertIsNone(self.deque.tail.next, 'tail.next is not None')
            self.assertEqual(self.deque.removeTail(), i, 'tail is not correct')
        self.assertIsNone(self.deque.removeTail(),
                          'empty deque return not None')
        self.assertIsNone(self.deque.head, 'head is not None')
        self.assertIsNone(self.deque.tail, 'tail is not None')

    def test_addTail_removeFront(self):
        self.assertIsNone(self.deque.removeFront(),
                          'empty deque return not None')
        self.assertIsNone(self.deque.head, 'head is not None')
        self.assertIsNone(self.deque.tail, 'tail is not None')
        for i in range(5):
            self.assertEqual(self.deque.size(), i, 'length is not correct')
            self.deque.addTail(i)
            self.assertIsNone(self.deque.head.prev, 'head.prev is not None')
            self.assertIsNone(self.deque.tail.next, 'tail.next is not None')
        self.assertEqual(self.deque.head.value, 0, 'tail.value is not correct')
        self.assertEqual(self.deque.head.next.value, 1,
                         'tail.value is not correct')
        self.assertEqual(self.deque.head.next.next.value,
                         2, 'tail.value is not correct')
        self.assertEqual(self.deque.head.next.next.next.value,
                         3, 'tail.value is not correct')
        self.assertEqual(self.deque.head.next.next.next.next.value,
                         4, 'tail.value is not correct')
        self.assertEqual(self.deque.head, self.deque.tail.prev.prev.prev.prev,
                         'deque is not correct')
        self.assertEqual(self.deque.head.next, self.deque.tail.prev.prev.prev,
                         'deque is not correct')
        self.assertEqual(self.deque.head.next.next, self.deque.tail.prev.prev,
                         'deque is not correct')
        self.assertEqual(self.deque.head.next.next.next, self.deque.tail.prev,
                         'deque is not correct')
        self.assertEqual(self.deque.head.next.next.next.next, self.deque.tail,
                         'deque is not correct')
        for i in range(5):
            self.assertEqual(self.deque.size(), 5 - i, 'length is not correct')
            self.assertIsNone(self.deque.head.prev, 'head.prev is not None')
            self.assertIsNone(self.deque.tail.next, 'tail.next is not None')
            self.assertEqual(self.deque.removeFront(),
                             i, 'tail is not correct')
        self.assertIsNone(self.deque.removeFront(),
                          'empty deque return not None')
        self.assertIsNone(self.deque.head, 'head is not None')
        self.assertIsNone(self.deque.tail, 'tail is not None')


if __name__ == '__main__':
    unittest.main()
