#coding:utf-8
"""
------------------------------------------------
@File Name    : BreathFirstSearch
@Function     : 
@Author       : Minux
@Date         : 2018/10/27
@Revised Date : 2018/10/27
------------------------------------------------
"""
from algorithm_and_data_structure.BFS.Vertex import Vertex
from queue import Queue

class BreadthFirstSearch:
    def bfs(self, root):
        if not isinstance(root, Vertex):
            raise Exception('Type Error')
        else:
            _queue = Queue()
            root.visited = True
            _queue.put(root)

            while not _queue.empty():
                actual_v = _queue.get()
                print(actual_v.data, end=' - ')
                # 利用了队列FIFO的性质
                for v in actual_v.get_neighbour():
                    if ~v.visited:
                        v.visited = True
                        _queue.put(v)


