# coding: utf-8
# @Time : 7/29/21 8:12 AM
from algo_lab.single_linked_list import SingleLinkedList


def merge(h1, h2):
    """
        https://stackoverflow.com/questions/22507197/merging-two-sorted-linked-lists-into-one-linked-list-in-python/40794749
    """
    if h1 is None:
        return h2
    if h2 is None:
        return h1

    if (h1.data < h2.data):
        h1.next = merge(h1.next, h2)
        return h1
    else:
        h2.next = merge(h2.next, h1)
        return h2


if __name__ == '__main__':
    l_a = SingleLinkedList(link_values=[1, 3, 7, 9])
    l_b = SingleLinkedList(link_values=[2, 4, 6, 8])
    print(merge(l_a, l_b))
