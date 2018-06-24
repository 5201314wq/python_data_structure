#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Qian.Wu

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from s3_3 import Stack

"""
后缀记法

使用一个栈，见到一个数时入栈，遇到一个运算符时就作用于从栈弹出的两个元素，将结果弹入栈中
"""