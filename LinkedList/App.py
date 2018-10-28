#coding:utf-8
"""
------------------------------------------------
@File Name    : App
@Function     : 
@Author       : Minux
@Date         : 2018/10/15
@Revised Date : 2018/10/15
------------------------------------------------
"""
from algorithm_and_data_structure.LinkedList.LinkedList import LinkedList

linkedList = LinkedList()
linkedList.insert_start(12)
linkedList.insert_start(122)
linkedList.insert_end(123)
linkedList.insert_start(378)
linkedList.insert_end(651)

print('number of points is {}'.format(linkedList.counter))
linkedList.traverse_list()

print()
print('remove point in the linklist')
linkedList.remove(378)
print('number of points is {}'.format(linkedList.counter))
linkedList.traverse_list()
