#coding:utf-8
"""
------------------------------------------------
@File Name    : Vertex
@Function     : 
@Author       : Minux
@Date         : 2018/10/27
@Revised Date : 2018/10/27
------------------------------------------------
"""
class Vertex:
    def __init__(self, data):
        self.__data = data
        self.__visited = False
        self.__neighbour_list = list()

    def add_neighbour(self, vertex):
        if isinstance(vertex, Vertex):
            self.__neighbour_list.append(vertex)
        else:
            raise Exception('Type Error')

    def get_neighbour(self):
        return self.__neighbour_list

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def visited(self):
        return self.__visited

    @visited.setter
    def visited(self, visited):
        self.__visited = visited

