#coding:utf-8
"""
------------------------------------------------
@File Name    : Node
@Function     : 
@Author       : Minux
@Date         : 2018/10/28
@Revised Date : 2018/10/28
------------------------------------------------
"""
class Node:
    def __init__(self, name):
        self.name = name
        self.adjcent_list = []
        self.visited = False


