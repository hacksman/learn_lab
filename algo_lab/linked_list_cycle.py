# coding: utf-8
# @Time : 7/28/21 8:24 AM
from algo_lab.single_linked_list import SingleLinkedList, Node


# def has_cycle(linked_list):
#     result = []
#     for node in linked_list:
#         if node.next and node.next.data in result:
#             node.data = '-.-'
#             continue
#         result.append(node.data)
#         if node.data == '-.-':
#             return True
#     return False

# def has_cycle(linked_list):
#     """
#         快慢指针，存在环的话，必定相遇
#     """
#     slow = linked_list
#     fast = linked_list
#
#     for s_step, s_node in enumerate(slow):
#         for f_step, f_node in enumerate(fast):
#             if f_step == s_step * 2 + 1:
#                 if f_node == s_node:
#                     return True
#                 break
#     return False


def has_cycle(linked_list):
    """
     from: https://leetcode-cn.com/problems/linked-list-cycle-lcci/solution/kuai-man-zhi-zhen-python3jie-fa-by-cheri-1l0h/
     需要支持：next 写法
     检查相遇点
    """
    fast = linked_list.head
    slow = linked_list.head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            pre = linked_list.head
            while pre != slow:
                pre = pre.next
                slow = slow.next
            return slow

    return


if __name__ == '__main__':
    # A -> B -> C -> D  -> E
    #             ↖ - - - -
    l = SingleLinkedList(["A", "B", "C", "D", "E"])
    l.head.next.next.next.next.next = l.head.next.next

    # A -> B -> C -> D
    #  ↖ - - - - - -
    l_c = SingleLinkedList(["A", "B", "C", "D"])
    l_c.head.next.next.next.next = l_c.head

    # A -> B -> C -> D -> E  -> C -> D -> E -> C -> D -> E -> C -> D -> E -> C -> D -> E
    not_l_c = SingleLinkedList(["A", "B", "C", "D", "E", "C", "D", "E", "C", "D", "E", "C", "D", "E", "C", "D", "E"])

    # A->
    only_one_node = SingleLinkedList(["A"])

    print(has_cycle(l))
    print(has_cycle(l_c))
    print(has_cycle(not_l_c))
    print(has_cycle(only_one_node))
