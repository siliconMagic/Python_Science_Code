#coding:utf-8
"""
------------------------------------------------
@File Name    : BinarySearchTree
@Function     : 
@Author       : Minux
@Date         : 2018/10/16
@Revised Date : 2018/10/16
------------------------------------------------
"""
from algorithm_and_data_structure.BinarySearchTree.Node import Node

class BST(object):
    def __init__(self):
        self.root_node = None

    def insert(self, data):
        if not self.root_node:
            self.root_node = Node(data)
        else:
            self.root_node.insert(data) # call the method in the Node file

    def remove(self, data_to_remove):
        if self.root_node:
            if self.root_node.data == data_to_remove: # 当前根节点存在并且需要删除的节点就是根节点
                # 由于root_node不存在父节点所以生成一个父节点，并将当前根节点作为左子节点
                temp_node = Node(None)
                temp_node.left_child = self.root_node
                t_node = self.root_node.remove(data_to_remove, temp_node)
                self.root_node = t_node

            else:
                self.root_node.remove(data_to_remove, None)

    def get_max(self):
        if self.root_node:
            return self.root_node.get_max_value()

    def get_min(self):
        if self.root_node:
            return self.root_node.get_min_value()

    def traverse_in_order(self):
        if self.root_node:
            return self.root_node.traverse_in_order()


