# coding: utf-8
# @Time : 7/22/21 8:06 AM


# 单链表结构
# 快慢指针
from copy import deepcopy
from algo_lab.single_linked_list import SingleLinkedList


def is_palindrome(linked_list):
    before = []
    after = []

    middle = None

    if linked_list == "" or linked_list is None:
        return False

    fast = deepcopy(linked_list)

    for step, slow in enumerate(linked_list):
        if middle is None:
            before.insert(0, slow.data)
        else:
            after.append(slow.data)

        tail = True
        f_node = ''
        for f_step, f_node in enumerate(fast):
            if f_step == step * 2 + 1:
                tail = False
                break
        if tail:
            middle = f_node.data

    return before[1:] == after[:]


if __name__ == '__main__':
    level = SingleLinkedList(['l', 'e', 'v', 'e', 'l'])
    lo = SingleLinkedList(['l', 'o'])
    assert is_palindrome(level) is True
    assert is_palindrome(lo) is False
