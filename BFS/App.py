#coding:utf-8
"""
------------------------------------------------
@File Name    : App
@Function     : 
@Author       : Minux
@Date         : 2018/10/27
@Revised Date : 2018/10/27
------------------------------------------------
"""
from algorithm_and_data_structure.BFS.Vertex import Vertex
from algorithm_and_data_structure.BFS.BreathFirstSearch import BreadthFirstSearch

if __name__ == '__main__':
    BFS = BreadthFirstSearch()
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    v4 = Vertex(4)
    v5 = Vertex(5)

    v1.add_neighbour(v2)
    v1.add_neighbour(v4)
    v4.add_neighbour(v5)
    v2.add_neighbour(v3)

    BFS.bfs(v1)