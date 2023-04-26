import unittest
from orderedlist import OrderedList


class OrderedListTest(unittest.TestCase):
    def setUp(self):
        self.ol = OrderedList()

    def test_init(self):
        self.assertIsNone(self.ol.head, 'head is not None')
        self.assertIsNone(self.ol.tail, 'tail is not None')
        self.ol_1 = OrderedList(False)
        self.assertIsNone(self.ol_1.head, 'head is not None')
        self.assertIsNone(self.ol_1.tail, 'tail is not None')

    def test_compare(self):
        self.assertEqual(self.ol.compare(1, 1), 0, 'compare(1, 1) should return 0')
        self.assertEqual(self.ol.compare(1, 2), -1, 'compare(1, 2) should return -1')
        self.assertEqual(self.ol.compare(2, 1), 1, 'compare(2, 1) should return 1')
        self.assertEqual(self.ol.compare(1, 0), 1, 'compare(1, 0) should return 1')
        self.assertEqual(self.ol.compare(0, -1), 1, 'compare(0, -1) should return 1')
        self.assertEqual(self.ol.compare(0, 0), 0, 'compare(0, 0) should return 0')
        self.assertEqual(self.ol.compare(-1, 0), -1, 'compare(-1, 0) should return -1')
        self.assertEqual(self.ol.compare(-1, -1), 0, 'compare(-1, -1) should return 0')

    def test_add(self):
        self.ol.add(2)
        self.ol.add(4)
        self.ol.add(1)
        self.ol.add(3)
        self.assertEqual(self.ol.head.value, 1, 'head should be 1')
        self.assertEqual(self.ol.head.next.value, 2, 'head.next should be 2')
        self.assertEqual(self.ol.head.next.next.value, 3, 'head.next should be 3')
        self.assertEqual(self.ol.head.next.next.next.value, 4, 'head.next should be 4')
        self.assertEqual(self.ol.head.value, self.ol.tail.prev.prev.prev.value,
        'head should be tail.prev.prev.prev')
        self.assertEqual(self.ol.head.next.value, self.ol.tail.prev.prev.value,
        'head.next should be tail.prev.prev')
        self.assertEqual(self.ol.head.next.next.value, self.ol.tail.prev.value,
        'head.next.next should be tail.prev')
        self.assertEqual(self.ol.head.next.next.next.value, self.ol.tail.value,
        'head.next.next.next should be tail')
        self.assertIsNone(self.ol.head.prev, 'head.prev should be None')
        self.assertIsNone(self.ol.tail.next, 'tail.next should be None')

    def test_add_desc(self):
        self.ol = OrderedList(False)
        self.ol.add(2)
        self.ol.add(4)
        self.ol.add(1)
        self.ol.add(3)
        self.assertEqual(self.ol.head.value, 4, 'head should be 1')
        self.assertEqual(self.ol.head.next.value, 3, 'head.next should be 2')
        self.assertEqual(self.ol.head.next.next.value, 2, 'head.next should be 3')
        self.assertEqual(self.ol.head.next.next.next.value, 1, 'head.next should be 4')
        self.assertEqual(self.ol.head.value, self.ol.tail.prev.prev.prev.value,
        'head should be tail.prev.prev.prev')
        self.assertEqual(self.ol.head.next.value, self.ol.tail.prev.prev.value,
        'head.next should be tail.prev.prev')
        self.assertEqual(self.ol.head.next.next.value, self.ol.tail.prev.value,
        'head.next.next should be tail.prev')
        self.assertEqual(self.ol.head.next.next.next.value, self.ol.tail.value,
        'head.next.next.next should be tail')
        self.assertIsNone(self.ol.head.prev, 'head.prev should be None')
        self.assertIsNone(self.ol.tail.next, 'tail.next should be None')

    def test_delete(self):
        for value in [1, 2, 3, 4]:
            self.ol.add(value)
        self.ol.delete(1)
        self.assertEqual(self.ol.head.value, 2,
                         'delete first node is not correct')
        self.assertIsNone(self.ol.head.prev, 'head.prev should be None')
        self.ol.delete(3)
        self.assertEqual(self.ol.head.value, 2,
                         'delete node in midlle is not correct')
        self.assertIsNone(self.ol.head.prev, 'head.prev should be None')
        self.assertEqual(self.ol.tail.value, 4,
                         'delete non-existnode is not correct')
        self.assertEqual(self.ol.head.next.value, 4,
                         'delete node in midlle is not correct')
        self.assertEqual(self.ol.tail.prev.value, 2,
                         'delete node in midlle is not correct')
        self.assertIsNone(self.ol.tail.next, 'tail.next should be None')
        self.ol.delete(5)
        self.assertEqual(self.ol.head.value, 2,
                         'delete non-exist node is not correct')
        self.assertIsNone(self.ol.head.prev, 'head.prev should be None')
        self.assertEqual(self.ol.tail.value, 4,
                         'delete non-exist node is not correct')
        self.assertEqual(self.ol.head.next.value, 4,
                         'delete non-exist node is not correct')
        self.assertEqual(self.ol.tail.prev.value, 2,
                         'delete non-exist node is not correct')
        self.assertIsNone(self.ol.tail.next, 'tail.next should be None')
        self.ol.delete(4)
        self.assertEqual(self.ol.head.value, 2,
                         'delete last node is not correct')
        self.assertIsNone(self.ol.head.prev, 'head.prev should be None')
        self.assertEqual(self.ol.tail.value, 2,
                         'delete last node is not correct')
        self.assertIsNone(self.ol.tail.next, 'tail.next should be None')
        self.ol.delete(2)
        self.assertIsNone(self.ol.head, 'head should be None')
        self.assertIsNone(self.ol.tail, 'tail should be None')

    def test_delete_desc(self):
        self.ol = OrderedList(False)
        for value in [1, 2, 3, 4]:
            self.ol.add(value)
        self.ol.delete(4)
        self.assertEqual(self.ol.head.value, 3,
                         'delete first node is not correct')
        self.assertIsNone(self.ol.head.prev, 'head.prev should be None')
        self.ol.delete(2)
        self.assertEqual(self.ol.head.value, 3,
                         'delete node in midlle is not correct')
        self.assertIsNone(self.ol.head.prev, 'head.prev should be None')
        self.assertEqual(self.ol.tail.value, 1,
                         'delete non-existnode is not correct')
        self.assertEqual(self.ol.head.next.value, 1,
                         'delete node in midlle is not correct')
        self.assertEqual(self.ol.tail.prev.value, 3,
                         'delete node in midlle is not correct')
        self.assertIsNone(self.ol.tail.next, 'tail.next should be None')
        self.ol.delete(5)
        self.assertEqual(self.ol.head.value, 3,
                         'delete non-exist node is not correct')
        self.assertIsNone(self.ol.head.prev, 'head.prev should be None')
        self.assertEqual(self.ol.tail.value, 1,
                         'delete non-exist node is not correct')
        self.assertEqual(self.ol.head.next.value, 1,
                         'delete non-exist node is not correct')
        self.assertEqual(self.ol.tail.prev.value, 3,
                         'delete non-exist node is not correct')
        self.assertIsNone(self.ol.tail.next, 'tail.next should be None')
        self.ol.delete(1)
        self.assertEqual(self.ol.head.value, 3,
                         'delete last node is not correct')
        self.assertIsNone(self.ol.head.prev, 'head.prev should be None')
        self.assertEqual(self.ol.tail.value, 3,
                         'delete last node is not correct')
        self.assertIsNone(self.ol.tail.next, 'tail.next should be None')
        self.ol.delete(3)
        self.assertIsNone(self.ol.head, 'head should be None')
        self.assertIsNone(self.ol.tail, 'tail should be None')

    def test_clean(self):
        for value in [1, 2, 3, 4]:
            self.ol.add(value)
        self.ol.clean(False)  
        self.assertIsNone(self.ol.head, 'head should be None')
        self.assertIsNone(self.ol.tail, 'tail should be None')
        for value in [1, 2, 3, 4]:
            self.ol.add(value)
        self.assertEqual(self.ol.head.value, 4, 'head should be 4')
        self.assertEqual(self.ol.tail.value, 1, 'tail should be 1')
        self.ol.clean(True)  
        self.assertIsNone(self.ol.head, 'head should be None')
        self.assertIsNone(self.ol.tail, 'tail should be None')
        for value in [1, 2, 3, 4]:
            self.ol.add(value)
        self.assertEqual(self.ol.head.value, 1, 'head should be 1')
        self.assertEqual(self.ol.tail.value, 4, 'tail should be 4')

    def test_len(self):
        self.assertEqual(self.ol.len(), 0, 'len shoul be 0')
        for value in [1, 2, 3, 4]:
            self.ol.add(value)
            self.assertEqual(self.ol.len(), value, 'len is not correct')


if    __name__ == '__main__':
    unittest.main()
