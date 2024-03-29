# coding: utf-8
# @Time : 7/30/21 8:47 AM
from algo_lab.single_linked_list import SingleLinkedList


def remove(linked_list, n):
    length = 0
    for _ in linked_list:
        length += 1
    if length - n < 0:
        return
    else:
        i = length - n
        prev = linked_list
        for l_i, node in enumerate(linked_list):
            if l_i == i:
                prev.next = node.next
                break
            prev = node


if __name__ == '__main__':
    s = SingleLinkedList(['A', 'B', 'C', 'D', 'E', 'F'])
    remove(s, 3)
    print(s)

    s = SingleLinkedList(['A', 'C', 'D', 'C', 'C', 'E', 'F'])
    remove(s, 4)
    print(s)
