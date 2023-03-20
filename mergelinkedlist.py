'''
merge_linked_list() - the function accepts two linked lists
and returns a linked list of the same length, the node values of which are
equal to the sum of the values of the original lists
'''

from linkedlist import LinkedList, Node


def merge_linked_list(llist_1: LinkedList,
                      llist_2: LinkedList) -> None | LinkedList:
    '''
    The function accepts two linked lists and returns a linked list
    of the same length, the node values of which are
    equal to the sum of the values of the original lists.
    If the length of the source lists differs, the function returns None
    '''
    if llist_1.len() != llist_2.len():
        return None
    sum_llist: LinkedList = LinkedList()
    node_1: None | Node = llist_1.head
    node_2: None | Node = llist_2.head
    while node_1 is not None and node_2 is not None:
        node: Node = Node(node_1.value + node_2.value)
        sum_llist.add_in_tail(node)
        node_1 = node_1.next
        node_2 = node_2.next
    return sum_llist
