#coding:utf-8
"""
------------------------------------------------
@File Name    : Node
@Function     : 
@Author       : Minux
@Date         : 2018/10/15
@Revised Date : 2018/10/15
------------------------------------------------
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def remove(self, data, previous_node):
        if self.data == data:
            previous_node.next_node = self.next_node
            del self.data
            del self.next_node
        else:
            if self.next_node is not None:
                self.next_node.remove(data, self)
