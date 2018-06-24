#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Qian.Wu

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

"""
对比列表和字典的包含操作的效率
"""

import timeit
import random

'''比较list 和 dict之间的时间差'''
for i in range(10000, 1000001, 20000):
    t = timeit.Timer("random.randrange(%d) in x"%i, "from __main import x, random")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    dict_time = t.timeit(number=1000)

    print("%d, %10.3f, %10.3f" %(i, lst_time, dict_time))


'''设计实现证明列表的索引操作是o(1)的'''
for i in range(10000, 1000001, 20000):
    t = timeit.Timer("x[random.randrange(%d)]"%(i), "from __main__ import x, random")
    x = list(range(i))
    list_index_time = t.timeit(number=1000)

    print("%d, %10.3f" %(i, list_index_time))

'''设计实现证明字典的读取和赋值操作都是O(1)的'''
for i in range(1000, 1000001, 20000):
    t = timeit.Timer("x[random.randrange(%d)]"%i, "from __main__ import x, random")
    x = {j:None for j in range(i)}
    dict_read_time = t.timeit(number=1000)

    t = timeit.Timer("x[random.randrange(%d)]=random.randrange(%d)" % (i, i), "from __main__ import x, random")
    x = {j: None for j in range(i)}
    dict_assign_time = t.timeit(number=1000)

    print("%d,readtime %10.3f,assign_time %10.3f"%(i, dict_read_time, dict_assign_time))
