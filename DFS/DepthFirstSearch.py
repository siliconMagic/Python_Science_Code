#coding:utf-8
"""
------------------------------------------------
@File Name    : DepthFirstSearch
@Function     : 
@Author       : Minux
@Date         : 2018/10/28
@Revised Date : 2018/10/28
------------------------------------------------
"""
def DFS(node):
    node.visited = True
    print(node.name, end=' - ')
    '''[]的布尔值为False'''
    if not node.adjcent_list:
        print('^')
    for _node in node.adjcent_list:
        if not _node.visited:
            DFS(_node)
