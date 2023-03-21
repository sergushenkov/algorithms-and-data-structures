import unittest
from reversiblelinkedlist import Node, LinkedList2


class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.rlist = LinkedList2()

    def test_find(self):
        for value in [1, 1, 2, 2]:
            node = Node(value)
            self.rlist.add_in_tail(node)
        self.assertIsNone(self.rlist.find(
            3), 'must return None if nothig found')
        self.assertEqual(self.rlist.find(1), self.rlist.head,
                         'value in head not found')
        self.assertEqual(self.rlist.find(2), self.rlist.tail.prev,
                         'value in prev tail not found')
        node = Node(3)
        self.rlist.add_in_tail(node)
        self.assertEqual(self.rlist.find(
            3), self.rlist.tail, 'value in tail not found')

    def test_find_all(self):
        for value in [1, 1, 1]:
            node = Node(value)
            self.rlist.add_in_tail(node)
        self.assertEqual(self.rlist.find_all(
            2), [], 'must return empty list if nothig found')
        self.assertEqual(self.rlist.find_all(1),
                         [self.rlist.head, self.rlist.head.next, self.rlist.tail],
                         'must return list of all nodes')
        node = Node(3)
        self.rlist.add_in_tail(node)
        self.assertEqual(self.rlist.find_all(3), [self.rlist.tail],
                         'must return only tail in list')

    def test_delete(self):
        self.rlist.delete(1)
        self.assertIsNone(self.rlist.head, 'rlist must be empty')
        self.assertIsNone(self.rlist.tail, 'rlist must be empty')
        node = Node(1)
        self.rlist.add_in_tail(node)
        self.rlist.delete(1)
        self.assertIsNone(self.rlist.head, 'rlist must be empty')
        self.assertIsNone(self.rlist.tail, 'rlist must be empty')
        for value in [1, 2, 3, 4]:
            node = Node(value)
            self.rlist.add_in_tail(node)
        self.rlist.delete(1)
        self.assertEqual(self.rlist.head.value, 2, 'head.value must be 2')
        self.assertIsNone(self.rlist.head.prev, 'head.prev must be None')
        self.assertEqual(self.rlist.head.next.value, 3,
                         'second node.value must be 3')
        self.rlist.delete(3)
        self.assertEqual(self.rlist.head.value, 2, 'head.value must be 2')
        self.assertEqual(self.rlist.head.next.value, 4,
                         'second node.value must be 4')
        self.assertEqual(self.rlist.tail.prev.value, 2,
                         'prev tail value must be 2')
        self.rlist.delete(4)
        self.assertEqual(self.rlist.head.value, 2, 'head.value must be 2')
        self.assertIsNone(self.rlist.head.prev, 'head.prev must be None')
        self.assertIsNone(self.rlist.head.next, 'head.next must be None')
        for value in [2, 1, 2, 3, 2]:
            node = Node(value)
            self.rlist.add_in_tail(node)
        self.rlist.delete(1, True)
        self.assertEqual(self.rlist.head.next.value, 2,
                         'second node.value must be 2')
        self.assertEqual(self.rlist.head.next.prev, self.rlist.head,
                         'second node.prev must be head')
        self.rlist.delete(2, True)
        self.assertEqual(self.rlist.head.value, 3, 'head.value must be 3')
        self.assertIsNone(self.rlist.head.next, 'head.next must be None')
        self.assertIsNone(self.rlist.head.prev, 'head.prev must be None')
        self.assertEqual(self.rlist.tail.value, 3, 'tail.value must be 3')
        self.assertIsNone(self.rlist.tail.next, 'tail.next must be None')
        self.assertIsNone(self.rlist.tail.prev, 'tail.prev must be None')
        self.rlist.delete(3, True)
        self.assertIsNone(self.rlist.head, 'head must be None')
        self.assertIsNone(self.rlist.tail, 'tail must be None')

    def test_clean(self):
        for value in [1, 2, 3]:
            node = Node(value)
            self.rlist.add_in_tail(node)
        self.rlist.clean()
        self.assertIsNone(self.rlist.head, 'head must be None')
        self.assertIsNone(self.rlist.tail, 'tail must be None')

    def test_len(self):
        self.assertEqual(self.rlist.len(), 0, 'length must be 0')
        for value in [1, 2, 3]:
            node = Node(value)
            self.rlist.add_in_tail(node)
            self.assertEqual(self.rlist.len(), value, 'length is not correct')

    def test_insert(self):
        node = Node(1)
        self.rlist.insert(None, node)
        self.assertEqual(self.rlist.head.value, 1, 'head.value must be 1')
        self.assertIsNone(self.rlist.head.next, 'head.next must be None')
        self.assertIsNone(self.rlist.head.prev, 'head.prev must be None')
        self.assertEqual(self.rlist.tail.value, 1, 'tail.value must be 1')
        self.assertIsNone(self.rlist.tail.next, 'tail.next must be None')
        self.assertIsNone(self.rlist.tail.prev, 'tail.prev must be None')
        node = Node(3)
        self.rlist.insert(None, node)
        self.assertEqual(self.rlist.head.value, 1, 'head.value must be 1')
        self.assertEqual(self.rlist.head.next, self.rlist.tail,
                         'head.next must be tail')
        self.assertEqual(self.rlist.tail.prev, self.rlist.head,
                         'tail.prev must be head')
        self.assertEqual(self.rlist.tail.value, 3, 'tail.value must be 3')
        self.assertIsNone(self.rlist.tail.next, 'tail.next must be None')
        node = Node(2)
        self.rlist.insert(self.rlist.head, node)
        self.assertEqual(self.rlist.head.value, 1, 'head.value must be 1')
        self.assertEqual(self.rlist.head.next.value, 2, 'head.value must be 2')
        self.assertEqual(self.rlist.head.next.next.value,
                         3, 'head.value must be 3')
        self.assertEqual(self.rlist.head.next.next, self.rlist.tail,
                         'head.next.next must be tail')
        self.assertEqual(self.rlist.tail.prev.prev, self.rlist.head,
                         'tail.prev.prev must be head')
        
    def test_add_in_head(self):
        node = Node(1)
        self.rlist.add_in_head(node)
        self.assertEqual(self.rlist.head.value, 1, 'head.value must be 1')
        self.assertIsNone(self.rlist.head.next, 'head.next must be None')
        self.assertIsNone(self.rlist.head.prev, 'head.prev must be None')
        self.assertEqual(self.rlist.tail.value, 1, 'tail.value must be 1')
        self.assertIsNone(self.rlist.tail.next, 'tail.next must be None')
        self.assertIsNone(self.rlist.tail.prev, 'tail.prev must be None')
        node = Node(3)
        self.rlist.add_in_head(node)
        self.assertEqual(self.rlist.head.value, 3, 'head.value must be 3')
        self.assertEqual(self.rlist.head.next, self.rlist.tail,
                         'head.next must be tail')
        self.assertEqual(self.rlist.tail.prev, self.rlist.head,
                         'tail.prev must be head')
        self.assertEqual(self.rlist.tail.value, 1, 'tail.value must be 1')
        self.assertIsNone(self.rlist.tail.next, 'tail.next must be None')


if __name__ == '__main__':
    unittest.main()
