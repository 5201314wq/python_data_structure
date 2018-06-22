#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Qian.Wu

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

'''
1.编写两个 Python 函数来寻找一个列表中的最小值。数量级是 O(n)
'''

def findMin1(nums):
    return min(nums)

def findMin2(nums):
    max = 0
    for num in nums:
        if num > max:
            max = num
    return max


