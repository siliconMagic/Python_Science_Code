#coding:utf-8
"""
------------------------------------------------
@File Name    : AVL_tree
@Function     : AVL_tree的进阶实现
@Author       : Minux
@Date         : 2018/10/18
@Revised Date : 2018/10/18
------------------------------------------------
"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent_node = None
        self.height = 1

class AVL_tree:
    def __init__(self):
        self.root_node = None

    def __repr__(self):
        if self.root_node is None:
            return ''


