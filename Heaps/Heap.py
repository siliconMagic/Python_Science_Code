#coding:utf-8
"""
------------------------------------------------
@File Name    : Heap
@Function     : 
@Author       : Minux
@Date         : 2018/10/19
@Revised Date : 2018/10/19
------------------------------------------------
"""

class Heap(object):
    HEAP_SIZE = 10

    def __init__(self):
        self.heap = [0]*Heap.HEAP_SIZE
        self.current_position = -1

    def insert(self, item):
        if self.is_full(): # 判断是否溢出
            print('Heap is Full')
            return
        self.current_position += 1
        self.heap[self.current_position] = item
        self.fix_up(self.current_position) # 堆调整函数

    def is_full(self):
        if self.current_position == Heap.HEAP_SIZE:
            return True
        else:
            return False

    def fix_up(self, index):
        parent_index = int((index-1)/2)
        while parent_index >= 0 and self.heap[parent_index] < self.heap[index]:
            # swap
            temp = self.heap[index]
            self.heap[index] = self.heap[parent_index]
            self.heap[parent_index] = temp
            index = parent_index
            parent_index = int((index-1)/2)

    def get_max_value(self):
        '''
        删除了原始的最大节点（根节点），需要进行从root_node向下的结构调整
        '''
        result = self.heap[0]
        self.current_position -=1
        self.heap[0] = self.heap[self.current_position]
        del self.heap[self.current_position+1]
        # 调整堆结构
        self.fix_down(0,-1)
        return result

    def fix_down(self, index, up_to_index):
        if up_to_index < 0:
            up_to_index = self.current_position

        while index <= up_to_index:
            left_child = 2*index+1
            right_child = 2*index+2

            # 确定与那个子节点进行交换
            '''交换原则
            1.index <= up_to_index
            2.swap_child = max(value(left_child), value(right_child)
            '''
            if left_child <= up_to_index:
                child_to_swap = None

                if right_child > up_to_index:
                    child_to_swap = left_child
                else:
                    if self.heap[left_child] > self.heap[right_child]:
                        child_to_swap = left_child
                    else:
                        child_to_swap = right_child
                if self.heap[index] < self.heap[child_to_swap]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[child_to_swap]
                    self.heap[child_to_swap] = temp
                else:
                    break
                index = child_to_swap
            else:
                break

    # perform O(N*log N) sorting in-place
    def heap_sort(self):
        for i in range(0, self.current_position+1):
            temp = self.heap[0]
            print(temp, end=' ')
            self.heap[0] = self.heap[self.current_position-i]
            self.heap[self.current_position-i] = temp
            self.fix_down(0, self.current_position-i-1)






