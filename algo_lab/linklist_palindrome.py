# coding: utf-8
# @Time : 7/22/21 8:06 AM


# 单链表结构
# 快慢指针
from copy import deepcopy


class Node:

    def __init__(self, data, n=None):
        self.data = data
        self.next = n


def is_palindrome(node):
    before = []
    after = []

    middle = None

    if node == "" or node is None:
        return False

    if node.next is None:
        return True

    fast = deepcopy(node)

    while node:
        if middle is None:
            before.insert(0, node.data)
        else:
            after.append(node.data)
        node = node.next
        if fast and middle is None:
            fast = fast.next.next
        if fast and fast.next is None and not middle:
            middle = node.data
    return before == after[1:]


if __name__ == '__main__':
    l = Node('l')
    l.next = Node('e')
    l.next.next = Node('i')
    l.next.next.next = Node('v')
    l.next.next.next.next = Node('i')
    l.next.next.next.next.next = Node('e')
    l.next.next.next.next.next.next = Node('l')

    print(is_palindrome(l))
