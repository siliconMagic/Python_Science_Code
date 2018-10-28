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
from algorithm_and_data_structure.Dijkstra.Vertex import Vertex
from algorithm_and_data_structure.Dijkstra.Edge import Edge
from algorithm_and_data_structure.Dijkstra.Algorithm import *

if __name__ == '__main__':
    # make the directed graph
    node_1 = Vertex('A')
    node_2 = Vertex('B')
    node_3 = Vertex('C')
    node_4 = Vertex('D')
    node_5 = Vertex('E')

    edge_1 = Edge(1, node_1, node_2)
    edge_2 = Edge(1, node_2, node_3)
    edge_3 = Edge(1.5, node_1, node_3)
    edge_4 = Edge(3, node_2, node_5)
    edge_5 = Edge(5, node_2, node_4)
    edge_6 = Edge(2.5, node_5, node_4)
    edge_7 = Edge(5, node_4, node_2)
    edge_8 = Edge(6, node_3, node_4)

    node_1.adjacent_list.append(edge_1)
    node_1.adjacent_list.append(edge_3)
    node_2.adjacent_list.append(edge_2)
    node_2.adjacent_list.append(edge_4)
    node_3.adjacent_list.append(edge_8)
    node_4.adjacent_list.append(edge_7)
    node_5.adjacent_list.append(edge_6)

    # make a set for vertex
    vertex_list = {node_1, node_2, node_3, node_4, node_5}

    calculate_shortest_path(vertex_list , node_1)
    get_shortest_path_to(node_4)

