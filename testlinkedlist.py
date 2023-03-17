import unittest
from linkedlist import Node, LinkedList


class TestNode(unittest.TestCase):
    def setUp(self):
        self.node_a = Node(0)
        self.node_b = Node(2)
        self.node_a.next = self.node_b
        self.node_c = Node(4)
        self.node_b.next = self.node_c

    def test_init(self):
        self.assertIsNotNone(self.node_b.next, 'node_b.next is None')
        self.assertIsNone(self.node_c.next, 'node_c.next is not None')
        self.assertEqual(self.node_a.next, self.node_b,
                         'node_a.next is not node_b')
        self.assertNotEqual(self.node_a.next, self.node_c,
                            'node_a.next is node_c')
        self.assertEqual(self.node_a.value, 0, 'node_a.value is not 0')
        self.assertEqual(self.node_b.value, 2, 'node_b.value is not 2')
        self.assertEqual(self.node_c.value, 4, 'node_c.value is not 4')

    def test_change(self):
        self.node_a.next = self.node_c
        self.node_c.value = 1
        self.node_a.value = 7
        self.assertIsNone(self.node_c.next, 'node_c.next is not None')
        self.assertNotEqual(self.node_a.next, self.node_b,
                            'node_a.next is node_b')
        self.assertEqual(self.node_a.next, self.node_c,
                         'node_a.next is not node_c')
        self.assertEqual(self.node_a.value, 7, 'node_a.value is not 7')
        self.assertEqual(self.node_c.value, 1, 'node_c.value is not 1')


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

    def test_init(self):
        self.assertIsNone(self.linked_list.head, 'linked_list.head is None')
        self.assertIsNone(self.linked_list.tail, 'linked_list.tail is None')

    def test_add_in_tail_first(self):
        node_a = Node(0)
        self.linked_list.add_in_tail(node_a)
        self.assertIsNotNone(self.linked_list.head, 'linked_list.head is None')
        self.assertEqual(self.linked_list.head, node_a,
                         'linked_list.head is not node_a')
        self.assertEqual(self.linked_list.tail, node_a,
                         'linked_list.tail is not node_a')
        node_b = self.linked_list.head
        self.assertEqual(node_b.value, 0, 'node_b.value is not 0')
        self.assertIsNone(node_b.next, 'node_b.next is not None')

    def test_add_in_tail_second(self):
        node_a = Node(0)
        self.linked_list.add_in_tail(node_a)
        node_b = Node(10)
        self.linked_list.add_in_tail(node_b)
        self.assertEqual(self.linked_list.head, node_a,
                         'linked_list.head is not node_a')
        self.assertEqual(self.linked_list.tail, node_b,
                         'linked_list.tail is not node_b')
        self.assertEqual(node_a.next, node_b, 'node_a.next is not node_b')
        self.assertIsNone(node_b.next, 'node_b.next is not None')

    def test_find_all(self):
        for value in [0, 2, 2, 2, 0]:
            node = Node(value)
            self.linked_list.add_in_tail(node)
        self.assertEqual(len(self.linked_list.find_all(0)), 2, 'find 0 is not correct')
        self.assertEqual(len(self.linked_list.find_all(2)), 3, 'find 2 is not correct') 
        self.assertEqual(self.linked_list.find_all(0)[0].value, 0, 'not correct node in list')
        self.assertEqual(self.linked_list.find_all(1), [], 'for 1 must be empty list')

    def test_delete_one(self):
        for value in [0, 1, 2, 2, 3, 0]:
            node = Node(value)
            self.linked_list.add_in_tail(node)
        self.linked_list.delete(0)
        self.assertEqual(self.linked_list.head.value, 1,
                         'delete first node is not correct')
        self.linked_list.delete(2)
        self.assertEqual(self.linked_list.head.next.next.value, 3,
                         'delete node in midlle is not correct')
        self.linked_list.delete(0)
        self.assertEqual(self.linked_list.tail.value, 3,
                         'delete last node is not correct')
        self.linked_list.delete(0)
        self.assertEqual(self.linked_list.head.value, 1,
                         'delete non-existent node is not correct')
        self.assertEqual(self.linked_list.head.next.value, 2,
                         'delete non-existent node is not correct')
        self.assertEqual(self.linked_list.head.next.next.value, 3,
                         'delete non-existent node is not correct')
        self.assertIsNone(self.linked_list.head.next.next.next,
                          'delete non-existent node is not correct')
        self.assertEqual(self.linked_list.tail.value, 3,
                         'delete non-existent node is not correct')
        self.assertIsNone(self.linked_list.tail.next,
                          'delete non-existent node is not correct')

    def test_delete_only(self):
        node = Node(0)
        self.linked_list.add_in_tail(node)
        self.linked_list.delete(0)
        self.assertIsNone(self.linked_list.head,
                          'delete only node is not correct')
        self.assertIsNone(self.linked_list.tail,
                          'delete only node is not correct')

    def test_delete_all(self):
        for value in [0, 1, 0, 0, 1, 1, 0]:
            node = Node(value)
            self.linked_list.add_in_tail(node)
        self.linked_list.delete(0, True)
        self.assertEqual(self.linked_list.head.value, 1,
                         'delete several nodes is not correct')
        self.assertEqual(self.linked_list.head.next.value, 1,
                         'delete several nodes is not correct')
        self.assertEqual(self.linked_list.head.next.next.value, 1,
                         'delete several nodes is not correct')
        self.assertIsNone(self.linked_list.head.next.next.next,
                          'delete several nodes is not correct')
        self.assertEqual(self.linked_list.tail.value, 1,
                         'delete several nodes is not correct')
        self.assertIsNone(self.linked_list.tail.next,
                          'delete several nodes is not correct')
        self.linked_list.delete(1, True)
        self.assertIsNone(self.linked_list.head,
                          'delete all nodes is not correct')
        self.assertIsNone(self.linked_list.tail,
                          'delete all nodes is not correct')

    def test_clean(self):
        for value in [0, 1, 2]:
            node = Node(value)
            self.linked_list.add_in_tail(node)
        self.linked_list.clean()
        self.assertIsNone(self.linked_list.head,
                          'head is not clean')
        self.assertIsNone(self.linked_list.tail,
                          'tail is not clean')

    def test_len(self):
        self.assertEqual(self.linked_list.len(), 0, 'length must be 0')
        for value in [1, 2, 3]:
            node = Node(value)
            self.linked_list.add_in_tail(node)
            self.assertEqual(self.linked_list.len(), value,
                             'length is not correct')
        self.linked_list.clean()
        self.assertEqual(self.linked_list.len(), 0,
                         'length must be 0 agter clean')

    def test_insert(self):
        node_2 = Node(2)
        self.linked_list.insert(None, node_2)
        self.assertEqual(self.linked_list.head, node_2,
                         'linked_list.head is not node_2')
        self.assertEqual(self.linked_list.tail, node_2,
                         'linked_list.tail is not node_2')
        self.assertIsNone(self.linked_list.tail.next, 'tail.next is not None')
        node_1 = Node(1)
        self.linked_list.insert(None, node_1)
        self.assertEqual(self.linked_list.head, node_1,
                         'linked_list.head is not correct')
        self.assertEqual(self.linked_list.tail, node_2,
                         'linked_list.tail is not correct')
        self.assertEqual(self.linked_list.head.next, node_2,
                         'second node is not node_2')
        node_4 = Node(4)
        self.linked_list.insert(node_2, node_4)
        self.assertEqual(self.linked_list.tail, node_4,
                         'linked_list.tail is not correct')
        self.assertEqual(self.linked_list.head.next.next, node_4,
                         'third node is not node_4')
        node_3 = Node(3)
        self.linked_list.insert(node_2, node_3)
        self.assertEqual(self.linked_list.head, node_1,
                         'linked_list.head is not correct')
        self.assertEqual(self.linked_list.tail, node_4,
                         'linked_list.tail is not correct')
        self.assertEqual(self.linked_list.head.next, node_2,
                         'second node is not node_2')
        self.assertEqual(self.linked_list.head.next.next, node_3,
                         'third node is not node_3')
        self.assertEqual(self.linked_list.head.next.next.next, node_4,
                         'fourth node is not node_4')
        self.assertIsNone(self.linked_list.tail.next, 'tail.next is not None')


if __name__ == "__main__":
    unittest.main()
