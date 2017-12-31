# coding:utf-8

"""
@Function:
Traits安装需要添加Microsoft VC++ 9.0的支持
同时需要安装的还有traitsui和pyface
Traits:为Python添加类型定义，降低错误率

图像化编程使用CanoPy比较好


@author: Minux
@date:2017-12-22
"""

from traits.api import HasTraits, Color
from traitsui import *



class Circle(HasTraits):
    '''
    所有拥有Trait属性的类都需要从HasTraits继承
    '''
    color = Color

class Parent(HasTraits):
    last_name = str('Min')

class Child(HasTraits):
    age = int


if __name__ == "__main__":
    circle = Circle()
    # 类Circle没有属性color
    # print(Circle.color)
    # 需要实例c = Circle()
    print(circle.color)
    # circle.configure_traits()
