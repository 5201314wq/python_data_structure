#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Qian.Wu

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

"""
判断回文
"""
from dq3_5 import Deque

def palchecker(str):
    dqueue = Deque()
    for ch in str:
        dqueue.addFront(ch)

    stillEqual = True
    while dqueue.size() > 1 and stillEqual:
        if dqueue.removeFront() != dqueue.removeRear():
            stillEqual = False

    return stillEqual

print(palchecker('asdffdsa'))