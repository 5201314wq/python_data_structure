#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Qian.Wu

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

"""
利用timeit算程序运行时间
timeit模块是被设计成在一个持续稳定的环境中，实现跨平台的时间测量

为使用 timeit 模块，你需要创建一个 Timer 对象，这个对象的参数是两个 Python 语句。
第一个 参数是你想进行计时的 Python 语句;第二个参数是建立这次测试你将要运行的语句。
timeit 模块就 将测量运行这个语句一定次数多花费的时间。如果不加要求，timeit 模块的
默认运行次数是一百万 次。运行结束后，它将以浮点数的形式返回运行的总时间(单位:秒)。
但是，由于它默认运行语 句一百万次，当你执行程序一次时，它返回的结果是以微秒为单位的。
你也可以在 timeit 中附上一个 名叫 number 的参数，这样你就可以指定程序被执行的次数。
下图将展示对我们的每一个程序执行 1000 次，分别需要花费的时间。
"""

from timeit import Timer

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

t1 = Timer('test1()', 'from __main__ import test1')
print('concat', t1.timeit(number=1000), 'milliseconds')

t2 = Timer('test2()', 'from __main__ import test2')
print('concat', t2.timeit(number=1000), 'milliseconds')

t3 = Timer('test3()', 'from __main__ import test3')
print('concat', t3.timeit(number=1000), 'milliseconds')

t4 = Timer('test4()', 'from __main__ import test4')
print('concat', t4.timeit(number=1000), 'milliseconds')