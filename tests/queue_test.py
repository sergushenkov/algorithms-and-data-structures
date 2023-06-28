import unittest
from queue_1 import Queue


class TestFunction(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = Queue()

    def test_all_in_one(self) -> None:
        self.assertIsNone(self.queue.dequeue(),
                          'empty queue.dequeue is not None')
        for i in range(10):
            self.assertEqual(self.queue.size(), i, 'queue.size is not correct')
            self.queue.enqueue(i)
        for i in range(10):
            self.assertEqual(self.queue.size(), 10 - i,
                             'queue.size is not correct')
            self.assertEqual(self.queue.dequeue(), i,
                             'queue.dequeue is not correct')
        self.assertIsNone(self.queue.dequeue(),
                          'empty queue.dequeue is not None')
        for i in range(10):
            self.assertEqual(self.queue.size(), 0, 'queue.size is not correct')
            self.queue.enqueue(i)
            self.assertEqual(self.queue.dequeue(), i,
                             'queue.dequeue is not correct')
        self.queue.enqueue(-1)
        for i in range(10):
            self.assertEqual(self.queue.size(), 1, 'queue.size is not correct')
            self.queue.enqueue(i)
            self.assertEqual(self.queue.dequeue(), i - 1,
                             'queue.dequeue is not correct')
        self.assertEqual(self.queue.dequeue(), 9,
                         'queue.dequeue is not correct')
        self.assertIsNone(self.queue.dequeue(),
                          'empty queue.dequeue is not None')
        self.assertEqual(self.queue.size(), 0, 'empty queue.size is not zero')


if __name__ == '__main__':
    unittest.main()
