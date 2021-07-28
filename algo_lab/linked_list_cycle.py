# coding: utf-8
# @Time : 7/28/21 8:24 AM
from algo_lab.single_linked_list import SingleLinkedList


def has_cycle(linked_list):
    result = []
    for node in linked_list:
        if node.next and node.next.data in result:
            node.data = '-.-'
            continue
        result.append(node.data)
        if node.data == '-.-':
            return True
    return False


if __name__ == '__main__':
    # A -> B -> C -> D  -> E
    #             ↖ - - - -
    l = SingleLinkedList(["A", "B", "C", "D", "E"])
    l.head.next.next.next.next.next = l.head.next.next

    # A -> B -> C -> D
    #  ↖ - - - - - -
    l_c = SingleLinkedList(["A", "B", "C", "D"])
    l_c.head.next.next.next.next = l.head

    # A -> B -> C -> D -> E  -> C -> D -> E -> C -> D -> E -> C -> D -> E -> C -> D -> E
    not_l_c = SingleLinkedList(["A", "B", "C", "D", "E", "C", "D", "E", "C", "D", "E", "C", "D", "E", "C", "D", "E"])

    # A->
    only_one_node = SingleLinkedList(["A"])

    print(has_cycle(l))
    print(has_cycle(l_c))
    print(has_cycle(not_l_c))
    print(has_cycle(only_one_node))
