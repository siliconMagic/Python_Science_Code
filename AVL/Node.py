#coding:utf-8
"""
------------------------------------------------
@File Name    : Node
@Function     : 
@Author       : Minux
@Date         : 2018/10/18
@Revised Date : 2018/10/18
------------------------------------------------
"""

'''
AVL树节点
'''


class Node(object):

    def __init__(self, data, parent_node):
        self.data = data
        self.parent_node = parent_node
        self.right_child = None
        self.left_child = None
        self.balance = 0

    def insert(self, data, parent_node):
        if data < self.data:
            if not self.left_child:
                self.left_child = Node(data, parent_node)
            else:
                self.left_child.insert(data, parent_node)

        else:
            if not self.right_child:
                self.right_child = Node(data, parent_node)
            else:
                self.right_child.insert(data, parent_node)

        return parent_node # for checking the balance

    def traverse_in_order(self):
        if self.left_child:
            self.left_child.traverse_in_order()
        print(self.data, end=' ')
        if self.right_child:
            self.right_child.traverse_in_order()

    def get_min_value(self):
        if self.left_child:
            return self.left_child.get_min_value()
        else:
            return self.data

    def get_max_value(self):
        if self.right_child:
            return self.right_child.get_max_value()
        else:
            return self.data









