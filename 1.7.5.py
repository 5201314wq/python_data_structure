#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Qian.Wu

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import random
import string
'''
这里有一个涵盖了我们所学所有知识的题目。你可能已经听说了无限猴子定理?该定理指出， 猴子随机在打字机键盘键入一个字符，经过无限时间后，肯定会
键入一系列给定的文字，比如莎士 比亚全集。好吧，假设我们用一个 Python 函数替换猴子。你认为多久以后才能生成一句莎士比亚的 名言呢?我们将这句
话定为:“methinks it is a weasel”
你不会希望在浏览器中运行这个程序，所以使用 Python IDE 吧。我们将模拟这个问题的方法是 编写一个函数，该函数生成一个 27 个字符长度的字符串，
从 26 个字母和空格中随机选择一个字 符。我们将编写另一个函数，来比较随机生成的字符串和目标字符串。
第三个函数将反复调用生成和比较函数，那么如果所有目标字母都在随机字符串中出现了，我 们就完成了。如果字母没有全部出现，我们会生成一个全新的字
符串.为了让它更易于跟随你的程序 的过程，第三个函数应该返回出到目前为止产生的最好的字符串，并返回在产生这个字符串之前每 1000 次尝试中产生其
它不合题意的字符串的次数。
'''

def randomly_generate_string():
    generated_string = ''.join(random.sample(string.ascii_letters + ' '))
    return generated_string

def compare(source_string, target_string):
    best_match, best_match_length, worst_match, worst_match_length = 0.0, 100000000
    intersection = set(source_string) & set(target_string)
    convergence = set(source_string) | set(target_string)

    content_match = 1.0 * intersection / convergence
    if len(source_string) > len(target_string):
        length_match = 1.0 * target_string / source_string
    else:
        length_match = 1.0 * source_string / target_string

    # find best match string
    if content_match > best_match:
        best_match_string = source_string
        best_match = content_match
        best_match_length = length_match
    elif content_match == best_match:
        if length_match < best_match_length:
            best_match_string = source_string
            best_match_length = length_match

    # find worst match string


def main():
    flags = False
    content_match, length_macth = 0.0, 0.0
    while(not flags):
        source_string = 'methinks it is a weasel'
        generated_string = randomly_generate_string()
        flags = compare(source_string, generated_string)

