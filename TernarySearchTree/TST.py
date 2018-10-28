#coding:utf-8
"""
------------------------------------------------
@File Name    : TST
@Function     : 
@Author       : Minux
@Date         : 2018/10/20
@Revised Date : 2018/10/20
------------------------------------------------
"""

from algorithm_and_data_structure.TernarySearchTree.Node import Node

class TST(object):
    def __init__(self):
        self.root_node = None

    def put(self, key, value):
        self.root_node = self.put_item(self.root_node, key, value, 0)

    def put_item(self, node, key, value, index):
        c = key[index]
        if node is None:
            node = Node(c)

        # c与存储节点中的字母不匹配，则进行递归调用
        if c < node.character:
            node.left_node = self.put_item(node.left_node, key, value, index)

        elif c > node.character:
            node.right_node = self.put_item(node.right_node, key, value, index)

        elif index < len(key)-1: # equal, but index is less than the key means the string is not at the end...
            node.middle_node = self.put_item(node.middle_node, key, value, index+1)

        else: # string is at the end, insert the value
            node.value = value

        return node

    def get(self, key):
        node = self.get_item(self.root_node, key, 0)
        if node is None:
            return None

        else:
            return node.value

    def get_item(self, node, key, index):
        if node is None: # 如果 root node 不存在，直接返回None
            return None

        c = key[index]
        if c < node.character:
            return self.get_item(node.left_node, key, index)
        elif c > node.character:
            return self.get_item(node.right_node, key, index)
        elif index < len(key)-1:
            return self.get_item(node.middle_node, key, index+1)
        else:
            return node







