from linkedlist import Node, LinkedList


def merge_linked_list(llist_1, llist_2):
    if llist_1.len() != llist_2.len():
        return
    sum_llist = LinkedList()
    node_1 = llist_1.head
    node_2 = llist_2.head
    while node_1 is not None:
        node = Node(node_1.value + node_2.value)
        sum_llist.add_in_tail(node)
        node_1 = node_1.next
        node_2 = node_2.next
    return sum_llist
