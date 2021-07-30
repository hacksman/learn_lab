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
        for l_i, node in enumerate(linked_list):
            if l_i == i:
                linked_list.remove_node(node.data)
                break


if __name__ == '__main__':
    s = SingleLinkedList(['A', 'B', 'C', 'D', 'E', 'F'])
    remove(s, 3)
    print(s)
