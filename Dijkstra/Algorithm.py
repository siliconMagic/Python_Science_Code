#coding:utf-8
"""
------------------------------------------------
@File Name    : Algorithm
@Function     : 
@Author       : Minux
@Date         : 2018/10/28
@Revised Date : 2018/10/28
------------------------------------------------
"""
import heapq

def calculate_shortest_path(vertex_list, start_vertex):
    queue = [] # 建立一个辅助队列
    start_vertex.min_distance = 0
    heapq.heappush(queue, start_vertex)

    while len(queue) > 0:
        actual_vertex = heapq.heappop(queue)

        '''对vertex的ajacent edge进行遍历'''
        for edge in actual_vertex.adjacent_list:
            u = edge.start_vertex
            v = edge.target_vertex
            if not u in vertex_list or not v in vertex_list:
                raise Exception('Error Point')

            new_distance = u.min_distance + edge.weight

            if new_distance < v.min_distance:
                v.predecessor = u
                v.min_distance = new_distance
                heapq.heappush(queue, v)

def get_shortest_path_to(target_vertex):
    print('shortest path to target is {}'.format(target_vertex.min_distance))
    node = target_vertex

    while node is not None:
        print('{} ->'.format(node.name), end='')
        node = node.predecessor


