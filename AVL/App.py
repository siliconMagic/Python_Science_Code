#coding:utf-8
"""
------------------------------------------------
@File Name    : App
@Function     : 
@Author       : Minux
@Date         : 2018/10/18
@Revised Date : 2018/10/18
------------------------------------------------
"""
from algorithm_and_data_structure.AVL.BalancedTree import BalancedTree

bst = BalancedTree()
bst.insert(1)
bst.insert(2)
bst.insert(-1)
bst.insert(5)
bst.insert(7)

bst.traverse_in_order()
print()
print('balance factor is {}'.format(bst.root_node.balance))