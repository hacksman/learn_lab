# coding: utf-8
# @Time : 7/23/21 8:08 AM


class Node:
    def __init__(self, value, next_node=None):
        self.data = value
        self.next = next_node

    def __repr__(self):
        return self.data


class SingleLinkedList:

    def __init__(self):
        self.head = None

    def add_first(self):
        pass

    def add_last(self, n):
        if not self.head:
            self.head = n
        else:
            current_node = None
            for current_node in self:
                pass
            current_node.next = n

    def add_before(self):
        pass

    def add_after(self):
        pass

    def remove_node(self):
        pass

    def reserve_node(self):
        pass

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        result = [_.data for _ in self]
        return f"->{'->'.join(result)}->None"


if __name__ == '__main__':
    A = Node('A')
    B = Node('B')
    C = Node('C')

    s = SingleLinkedList()
    s.add_node(A)
    s.add_node(B)
    s.add_node(C)

    for i in s:
        print(i)
    print(s)
