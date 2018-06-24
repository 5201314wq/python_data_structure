#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Qian.Wu

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

"""
让我们来考虑一个叫做热土豆的儿童游戏。小孩子们围成一个圆圈并以最快的速度接连传递物品，并在游戏的一个
特定时刻停止传递，这时手中拿着物品的小孩就离开圆圈，游戏进行至只剩下一个小孩。
"""

from q3_4 import Queue

def hot_potato(namelist, num):
    queue = Queue()

    for name in namelist:
        queue.enqueue(name)

    while queue.size() > 1:

        for i in range(num):
            queue.enqueue(queue.dequeue())

        queue.dequeue()

    return queue.dequeue()

print(hot_potato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Bard'], 2))
