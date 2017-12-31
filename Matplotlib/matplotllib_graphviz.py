# coding:utf-8
"""
@Function:
将Artist对象的内部关系输出成为Graphviz格式的图形语言

@author:Minux
@date:2017-12-18
"""

import graphviz
import matplotlib.pyplot as plt

def graphviz_plt():
    plt.figure()
    plt.subplot(211)
    plt.bar([1, 2, 3],[1, 2, 3])
    plt.subplot(212)
    plt.plot([1, 2, 3])
    plt.show()

if __name__ == '__main__':
    graphviz_plt()