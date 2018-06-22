#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Qian.Wu

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

"""
经典的字符串变位词检测问题是比较不同数量级函数算法的一个典型例子。如果一个字符串是 另一个字符串的
重新排列组合，那么这两个字符串互为变位词。比如，”heart”与”earth”互为变位 词，”python”与”typhon”
也互为变位词
"""

'''
解法 1:检查标记
变位词问题的第一种解法是检查第一个字符串中的所有字符是不是都在第二个字符串中出现。 如果能够把每一个
字符都“检查标记”一遍，那么这两个字符串就互为变位词。检查标记一个字符 要用特定值 None 来代替，作为标记。
然而，由于字符串不可变，首先要把第二个字符串转化成一个列表。第一个字符串中的每一个字符都可以在列表的字
符中去检查，如果找到，就用 None 代替以示 标记。
'''

def anagram_solution1(s1, s2):
    pos1 = 0
    still_ok = True
    list_s2 = list(s2)
    while pos1<len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2<len(s2) and not found:
            if list_s2[pos2] == s1[pos1]:
                found = True
            else:
                pos2 += 1

        if found:
            list_s2[pos2] = None
        else:
            still_ok = False
        pos1 += 1

    return still_ok


'''
解法 2:排序比较法
尽管 s1 和 s2 并不相同，但若为变位词它们一定包含完全一样的字符，利用这一特点，我们可以 采用另一种方法。
我们首先从 a 到 z 给每一个字符串按字母顺序进行排序，如果它们是变位词，那么 我们将得到两个完全一样的字符串。
此外，我们可以先将字符串转化为列表，再利用 Python 中内建 的 sort 方法对列表进行排序
'''
def anagram_solution2(s1, s2):
    list_s1 = list(s1)
    list_s2 = list(s2)

    list_s1.sort()
    list_s2.sort()

    pos = 0
    matches = True
    while pos < len(s1) and matches:
        if list_s1[pos]!=list_s2[pos]:
            matches = False
        else:
            pos += 1

    return matches

'''
解法 3：技术比较法
解决变位词问题的最后一个方法利用了任何变位词都有相同数量的 a，相同数量的 b，相同数量 的 c 等等。
为判断两个字符串是否为变位词，我们首先计算每一个字符在字符串中出现的次数。由于 共有 26 个可能的字符，
我们可以利用有 26 个计数器的列表，每个计数器对应一个字符。每当我们 看到一个字符，就在相对应的计数器上加一。
最终，如果这两个计数器列表相同，则这两个字符串 是变位词。
'''
def anagram_solution3(s1, s2):
    index_s1 = [0] * 26
    index_s2 = [0] * 26

    for item in s1:
        index_s1[ord(item) - ord('a')] += 1

    for item in s2:
        index_s2[ord(item) - ord('a')] += 1

    pos = 0
    still_ok = True
    while pos < 26 and still_ok:
        if index_s1[pos] != index_s2[pos]:
            still_ok = False
        else:
            pos += 1

    return still_ok

if __name__ == '__main__':
    s1 = 'dada'
    s2 = 'adad'
    status = anagram_solution1(s1, s2)
    print("status", status)
    status = anagram_solution2(s1, s2)
    print("status", status)
    status = anagram_solution3(s1, s2)
    print("status", status)

