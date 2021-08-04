# coding: utf-8
# @Time : 8/4/21 7:42 AM


def sort(l):
    n = len(l)
    for i in range(n):
        for j in range(i):
            if l[i] < l[j]:
                v = l.pop(i)
                l.insert(j, v)
                break


l_l = [1, 3, 4, 2, 5, 6]
sort(l_l)
print(l_l)
