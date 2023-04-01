import sys
sys.path.insert(0,'..')

import unittest
from linkedlist import Node, LinkedList
from mergelinkedlist import merge_linked_list


class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.llist_1 = LinkedList()
        self.llist_2 = LinkedList()

    def test_merge_linked_list(self):
        # two empty linked lists
        result = merge_linked_list(self.llist_1, self.llist_2)
        self.assertEqual(
            result.len(), 0, 'result for two empty linked lists is not empty')
        self.assertIsNone(
            result.head, 'result.head for two empty linked lists is not None')
        self.assertIsNone(
            result.tail, 'result.tail for two empty linked lists is not None')

        # empty and non_empty linked lists
        for value in [1, 0, -2]:
            node = Node(value)
            self.llist_1.add_in_tail(node)
        result = merge_linked_list(self.llist_1, self.llist_2)
        self.assertIsNone(
            result, 'result for empty and non_empty linked lists is not None')

        # two linked lists with different length
        for value in [9, 10]:
            node = Node(value)
            self.llist_2.add_in_tail(node)
        result = merge_linked_list(self.llist_1, self.llist_2)
        self.assertIsNone(
            result, 'result for two linked lists with different length is not None')

        # two non-empty linked lists with same length
        node = Node(2)
        self.llist_2.add_in_tail(node)
        result = merge_linked_list(self.llist_1, self.llist_2)
        self.assertEqual(
            result.len(), 3, 'result.len for same linked lists is not correct')
        self.assertEqual(result.head.value, 10,
                         'result.head.value for two non-empty linked lists with same length is not correct')
        self.assertEqual(result.head.next.value, 10,
                         'result second value for two non-empty linked lists with same length is not correct')
        self.assertEqual(result.head.next.next.value, 0,
                         'result third value for two non-empty linked lists with same length is not correct')
        self.assertIsNone(result.head.next.next.next,
                          'result last next for two non-empty linked lists is not None')
        self.assertIsNone(
            result.tail.next, 'result.tail.next for two non-empty linked lists is not None')


if __name__ == '__main__':
    unittest.main()
