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
import sys

class Vertex:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacent_list = []
        self.min_distance = sys.maxsize

    def __cmp__(self, other_v):
        return self < other_v

    def __lt__(self, other_v):
        self_priority = self.min_distance
        other_priority = other_v.min_distance

        return self_priority < other_priority

    def __repr__(self):
        return self.name


# test the class
if __name__ == '__main__':
    v1 = Vertex('A')
    v1.min_distance = 3
    v2 = Vertex('B')
    v2.min_distance = 5
    v3 = Vertex('C')
    v3.min_distance = 1
    print(sorted([v1, v2, v3]))

