# coding:utf-8

import matplotlib.pyplot as plt
import numpy as np


def scatter_pic():
    fig = plt.figure()
    x = np.random.random(100)
    y = np.random.random(100)
    '''
    参数解释：
    marker表示多边形的样式，取值范围为0,1,2,3
    第一个元素表示边数
    0表示多边形
    1表示星型
    2表示放射型
    3表示圆形
    '''
    plt.scatter(x, y, s = x*1000, c=y, marker=(3, 2), alpha = 0.8, lw = 2, facecolors = "none")
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()

if __name__ == "__main__":
    scatter_pic()