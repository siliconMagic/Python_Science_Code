# coding:utf-8
"""
@Function:
使用contour,contourf
使用隐函数绘图

@author: Minux
@date: 2017-12-21
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

plt.rcParams["axes.unicode_minus"] = False

def implicit_function():
    x, y = np.ogrid[-1.5:1.5:200j, -1.5:1.5:200j]
    f = (x**2 + y**2)**4 - (x**2 - y**2)**2

    fig = plt.figure()
    plt.figure(figsize = (9, 4))
    plt.subplot(121)
    extent = [np.min(x), np.max(x), np.min(y), np.max(y)]
    # 绘制出f=0和f=0.1
    cs = plt.contour(f, extent = extent, levels = [0, 0.1],
                     color=["b", "r"], linestyles = ["solid", "dashed"],
                     linewidths = [2, 2])

    plt.subplot(122)
    for c in cs.collections:
        data = c.get_paths()[0].vertices
        plt.plot(data[:,0], data[:,1], color = c.get_color()[0], linewidth = c.get_linewidth()[0])

    plt.show()

if __name__ == "__main__":
    implicit_function()