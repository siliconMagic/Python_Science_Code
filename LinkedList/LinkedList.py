#coding:utf-8
"""
------------------------------------------------
@File Name    : LinkedList
@Function     : 
@Author       : Minux
@Date         : 2018/10/15
@Revised Date : 2018/10/15
------------------------------------------------
"""
from algorithm_and_data_structure.LinkedList.Node import Node

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.counter = 0 # counter 记录节点数量

    # O(1) 头插法
    def insert_start(self, data):
        new_node = Node(data)
        self.counter += 1

        # 如果头结点为空，新节点即为头结点
        if not self.head:
            self.head = new_node
        else:
            # 如果头结点不为空，新节点插入到头结点前面
            new_node.next_node = self.head
            self.head = new_node

    # O(1)
    def size(self):
        return self.counter

    # O(N)
    def insert_end(self, data):
        # new_node = Node(data)
        # self.counter += 1

        if self.head is None:
            self.insert_start(data)
            return

        # if not self.head:
        #     self.head = new_node
        else:
            # 如果头结点不为空节点
            new_node = Node(data)
            actual_node = self.head
            while actual_node.next_node:
                actual_node = actual_node.next_node # keep iterating
            actual_node.next_node = new_node
            self.counter += 1

    # O(N)
    def remove(self, data):
        self.counter -= 1
        if self.head:
            # 如果删除节点为头结点
            if data == self.head.data:
                self.head = self.head.next_node
            else:
                self.head.remove(data, self.head)

    # O(N)
    def traverse_list(self):
        actual_node = self.head
        while actual_node:
            print(actual_node.data, end=' ')
            actual_node = actual_node.next_node











