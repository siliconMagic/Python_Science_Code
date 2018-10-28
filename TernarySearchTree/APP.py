#coding:utf-8
"""
------------------------------------------------
@File Name    : APP
@Function     : 
@Author       : Minux
@Date         : 2018/10/20
@Revised Date : 2018/10/20
------------------------------------------------
"""
from algorithm_and_data_structure.TernarySearchTree.TST import TST

tree = TST()
tree.put('apple', 100)
tree.put('orange', 200)
tree.put('apx',25)
tree.put('appl',30)

print(tree.get('apple'))
print(tree.get('apx'))

