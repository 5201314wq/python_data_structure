#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Qian.Wu

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

"""
实现List

无序列表,由一个节点的集合组成，每个节点采用显示引用链接到下一个节点，只要我们知道第一个节点的位置，在这之后
的每个元素都可以通过以下链接找到下一个节点
"""

class Node():
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.data = newnext

class UnorderedList():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        '''必须要考虑到移除节点为第一个的情况'''
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


    def append(self, item):
        temp = Node(item)
        current = self.head
        temp.setNext(current)
        self.head.setNext(temp)

    def insert(self, i, item):
        current = self.head
        previous = None
        count = 0
        found = False
        while current and not found:
            count += 1
            if count == i:
                found = True
            else:
                previous = current
                current = current.getNext()

        if found:
            if not previous:
               self.append(item)
            else:
                temp = Node(item)
                temp.setNext(current)
                previous.setNext(temp)
        else:
            raise 'Index Wrong!'

    def index(self, item):
        current = self.head
        count = 0
        while(current):
            if current.getData() == item:
                return count
            else:
                count += 1
                current = current.getNext()

        if not current:
            return 'Not Found!'

    def pop(self, i):
        current = self.head
        previous = None
        found = False
        count = 0
        while current and not found:
            if count == i:
                found = True
            else:
                previous = current
                current = current.getNext()

        if found:
            if not previous:
                self.head = current.getNext()
            else:
                current = current.getNext()
                previous.setNext(current)
        else:
            raise 'Index Wrong!'

    def list_print(self):
        current = self.head

        while current:
            print(current.getData, end=' ')
            current = current.getNext()



