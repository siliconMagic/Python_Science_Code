#coding:utf-8
"""
------------------------------------------------
@File Name    : Node
@Function     : 
@Author       : Minux
@Date         : 2018/10/20
@Revised Date : 2018/10/20
------------------------------------------------
"""

class Node(object):
    def __init__(self, character):
        self.character = character
        self.left_node   = None
        self.right_node  = None
        self.middle_node = None

