# coding: utf-8
# @Time : 8/3/21 8:13 AM


def sort(l):
    n = len(l)
    for i in range(n):
        for j in range(n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]


l_l = [1, 3, 4, 2, 5, 6]
sort(l_l)
print(l_l)
