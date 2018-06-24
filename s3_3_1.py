#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Qian.Wu

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from s3_3 import Stack
"""
检查程序中成对的符号

做一个空栈，如果字符是开放符号('({[')则将其push栈中。如果符号是个闭合符号(')]}'),则当栈空时报错，对应'()}'
的错误。否则，将栈pop，如果弹出的符号不是对应的开放符号，则报错，对应'(}'的错误。文件末尾，如果栈为空，则报
错，对应'({}'的错误。
"""
def match(i, j):
    opens = '({['
    closes = ')}]'
    return opens.index(i)==closes.index(j)


def pair_bracket_checker(str):
    stack = Stack()
    opening_brackets = '({['
    closing_brackets = ')}]'
    i = 0
    still_ok = True
    while i<len(str) and still_ok:
        if str[i] in opening_brackets:
            stack.push(str[i])
        elif str[i] in closing_brackets:
            item = stack.pop()
            if not match(item, str[i]):
                still_ok = False
        else:
            raise 'Wrong type of brackets!'

        i += 1
    if still_ok==True and stack.isEmpty():
        return True
    else:
        return False

if __name__ == '__main__':
    str='{[()]}'
    check_brace = pair_bracket_checker(str)
    print(check_brace)





