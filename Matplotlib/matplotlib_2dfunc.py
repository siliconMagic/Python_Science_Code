# coding:utf-8
"""
@Function:
可视化一个二元函数 f(x, y) = x*e^(x^2-y^2)

@author: Minux
@date: 2017-12-21
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


plt.rcParams["axes.unicode_minus"] = False

def visible_2d_func():
    y, x = np.ogrid[-2:2:200j, -2:2:200j]
    z = x * np.exp(- y**2 - x**2)
    # 使用extent参数给定x,y的取值范围
    extent = [np.min(x), np.max(x), np.min(y), np.max(y)]
    fig = plt.figure()
    plt.subplot(131)
    plt.imshow(z, extent = extent, origin = "lower")
    plt.colorbar()
    plt.subplot(132)
    plt.imshow(z, extent = extent, cmap = cm.gray, origin="lower")
    plt.colorbar()
    # plt.subplot(133)
    plt.show()


if __name__ == "__main__":
    visible_2d_func()