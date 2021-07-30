# coding: utf-8
# @Time : 7/23/21 8:08 AM


class Node:
    def __init__(self, value, next_node=None):
        self.data = value
        self.next = next_node

    def __repr__(self):
        if self:
            result = [_.data for _ in self]
            return f"->{'->'.join(map(str, result))}->None"
        return 'empty Node'

    def __iter__(self):
        """
         当出现循环链表的时候，某个 node 自身也需要支持可迭代性
        """
        node = self
        while node:
            yield node
            node = node.next

    def __ge__(self, other):
        return self.data >= other.data

    def __le__(self, other):
        return self.data <= other.data

    def __gt__(self, other):
        return self.data > other.data

    def __lt__(self, other):
        return self.data < other.data


class SingleLinkedList:

    def __init__(self, link_values=None):
        self.head = None
        if link_values:
            for item in link_values:
                self.add_last(Node(item))

    @property
    def next(self):
        return self.head.next

    @next.setter
    def next(self, n):
        self.head.next = n

    @property
    def data(self):
        if not self.head:
            return None
        return self.head.data

    @data.setter
    def data(self, value):
        self.head.data = value

    def __gt__(self, other):
        return self.head.data > other.data

    def __lt__(self, other):
        return self.head.data < other.data

    def __ge__(self, other):
        return self.head.data >= other.data

    def __le__(self, other):
        return self.head.data <= other.data

    def add_first(self, n):
        if not self.head:
            self.head = n
        else:
            n.next = self.head
            self.head = n

    def add_last(self, n):
        if not self.head:
            self.head = n
        else:
            current_node = None
            for current_node in self:
                pass
            current_node.next = n

    def add_before(self, value, n):
        if not self.head:
            return

        if self.head.data == value:
            self.add_first(n)
            return

        prev_node = self.head
        for current_node in self:
            if current_node.data == value:
                prev_node.next = n
                n.next = current_node
                return
            prev_node = current_node

    def add_after(self, value, n):
        if not self.head:
            return

        if self.head.data == value:
            self.add_last(n)

        for current_node in self:
            if current_node.data == value:
                after_node = current_node.next
                current_node.next = n
                n.next = after_node

    def remove_node(self, value):
        prev_node = self.head
        for current_node in self:
            if current_node.data == value:
                prev_node.next = current_node.next
                return
            prev_node = current_node
        print(f"data =「{value}」 not in linked list")

    def reserve_node(self):
        """
        :💡: 反转好的数据放在左边，中间值存储链表遍历的值，遍历完了之后，中间值的下一步可以把之前存储在左边的反转数据接过来
        """
        if not self.head:
            return

        l, m, r = None, None, self.head

        while r is not None:
            l = m
            m = r
            r = r.next
            m.next = l

        self.head = m

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        if self.head:
            result = [_.data for _ in self]
            return f"->{'->'.join(map(str, result))}->None"
        return 'empty linked list'


if __name__ == '__main__':
    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')

    s = SingleLinkedList()
    s.add_last(A)
    s.add_last(B)
    s.add_last(C)
    s.add_last(D)
    s.add_last(E)

    # 中环链表
    s.head.next.next.next.next.next = s.head.next.next

    #     pass
    # s.add_after('B', E)
    # s.remove_node('F')
    # print(next(s))
    # print(next(s))
    # print(next(s))
    # print(next(s))
    # s.reserve_node()

    print(s)
