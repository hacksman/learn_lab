# coding: utf-8
# @Time : 7/28/21 8:24 AM
from algo_lab.single_linked_list import SingleLinkedList

l = SingleLinkedList(["A", "B", "C", "D", "E"])
l_cycle = l.head.next.next.next.next.next = l.head.next.next

l_c = SingleLinkedList(["A", "B"])

l_c.head.next.next = l_cycle


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
    not_l_c = SingleLinkedList(["A", "B", "C", "D", "E", "C", "D", "E", "C", "D", "E", "C", "D", "E", "C", "D", "E"])
    print(has_cycle(l_cycle))
    print(has_cycle(l_c))
    print(has_cycle(not_l_c))


