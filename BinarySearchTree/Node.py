#coding:utf-8
"""
------------------------------------------------
@File Name    : Node
@Function     : 
@Author       : Minux
@Date         : 2018/10/16
@Revised Date : 2018/10/16
------------------------------------------------
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        if data < self.data:
            if not self.left_child:
                self.left_child = Node(data)
            else:
                self.left_child.insert(data) # call this function recursively
        else:
            if not self.right_child:
                self.right_child = Node(data)
            else:
                self.right_child.insert(data)

    def remove(self, data, parent_node):
        # 定位将被删除的节点
        if data < self.data:
            if self.left_child is not None:
                self.left_child.remove(data, self)
        elif data > self.data:
            if self.right_child is not None:
                self.right_child.remove(data, self)
        # 定位到需要被删除的节点
        else:
            # 如果被删除节点存在两个子节点
            if self.left_child is not None and self.right_child is not None:
                # 定位中继后续节点
                # 先将中继后续节点值赋给当前节点，然后将中继后续节点值删除
                self.data = self.right_child.get_min_value()
                self.right_child.remove(self.data, self)

            # 如果当前节点为父节点的左子节点
            elif parent_node.left_child == self:
                # 当前节点仅存在左子节点
                if self.left_child is not None:
                    temp_node = self.left_child
                # 当前节点仅存在右子节点
                else:
                    temp_node = self.right_child
                parent_node.left_child = temp_node
                return temp_node

            # 如果当前节点为父节点的右子节点
            elif parent_node.right_child == self:
                # 当前节点仅存在左子节点
                if self.left_child is not None:
                    temp_node = self.left_child
                else:
                    temp_node = self.right_child
                parent_node.right_child = temp_node
                return temp_node


    def get_min_value(self):
        if self.left_child is None:
            return self.data
        else:
            return self.left_child.get_min_value()

    def get_max_value(self):
        if self.right_child is None:
            return self.data
        else:
            return self.right_child.get_max_value()

    def traverse_in_order(self):
        if self.left_child is not None:
            self.left_child.traverse_in_order()

        print(self.data, end=' ')

        if self.right_child is not None:
            self.right_child.traverse_in_order()




