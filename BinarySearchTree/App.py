#coding:utf-8
"""
------------------------------------------------
@File Name    : App
@Function     : 
@Author       : Minux
@Date         : 2018/10/16
@Revised Date : 2018/10/16
------------------------------------------------
"""
from algorithm_and_data_structure.BinarySearchTree.BinarySearchTree import BST

bst = BST()
bst.insert(-2)
bst.insert(11)
# bst.insert(-3)
bst.insert(12)
bst.insert(9)
bst.insert(3)
bst.insert(15)

bst.traverse_in_order()

print()
print('-'*10)
bst.remove(12)
bst.traverse_in_order()
print()
print('-'*10,'try to delete the root node','-'*10)
bst.remove(-2)
bst.traverse_in_order()
print()

print('the minimun element is {}'.format(bst.get_min()))
print('the maximum element is {}'.format(bst.get_max()))
print('the root node of the tree is {}'.format(bst.root_node.data))