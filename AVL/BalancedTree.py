#coding:utf-8
"""
------------------------------------------------
@File Name    : BalancedTree
@Function     : 
@Author       : Minux
@Date         : 2018/10/18
@Revised Date : 2018/10/18
------------------------------------------------
"""

from algorithm_and_data_structure.AVL.Node import Node

class BalancedTree(object):
    def __init__(self):
        self.root_node = None

    def insert(self, data):
        if not self.root_node:
            parent_node = Node(data, None)
            self.root_node = Node(data, parent_node)
        else:
            parent_node = self.root_node.insert(data, self.root_node)

        self.rebalance_tree(parent_node)

    def rebalance_tree(self, parent_node):
        self.set_balance(parent_node)

    def set_balance(self, node):
        node.balance = (self.height(node.right_child)-self.height(node.left_child))

    def height(self, node):
        if node is None:
            return -1
        else:
            return 1 + max(self.height(node.left_child), self.height(node.right_child))

    def traverse_in_order(self):
        if self.root_node:
            self.root_node.traverse_in_order()


