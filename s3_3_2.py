#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Qian.Wu

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from s3_3 import Stack

"""
进制转换
十进制转换二进制：把十进制转成二进制一直分解至商数为0。从最底左边数字开始读，之后读右边的数字，从下读到上。
"""

def decimal_to_bin(dec):
    stack = Stack()
    while(dec!=0):
        stack.push(dec % 2)
        dec = dec//2

    while(not stack.isEmpty()):
        print(stack.pop(), end='')

    print()

if __name__ == '__main__':
    dec = 100
    decimal_to_bin(dec)
