#coding:utf-8
"""
------------------------------------------------
@File Name    : App
@Function     : 
@Author       : Minux
@Date         : 2018/10/28
@Revised Date : 2018/10/28
------------------------------------------------
"""
from algorithm_and_data_structure.DFS.Node import Node
from algorithm_and_data_structure.DFS.DepthFirstSearch import DFS

if __name__ == '__main__':
    node_1 = Node('A')
    node_2 = Node('B')
    node_3 = Node('C')
    node_4 = Node('D')
    node_5 = Node('E')

    node_1.adjcent_list.append(node_2)
    node_1.adjcent_list.append(node_3)
    node_2.adjcent_list.append(node_4)
    node_4.adjcent_list.append(node_5)

    DFS(node_1)