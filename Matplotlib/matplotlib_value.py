# coding:utf-8
"""
@Function:
使用contour,contourf
描绘等值线图

@author: Minux
@date: 2017-12-21
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

plt.rcParams["axes.unicode_minus"] = False

def cont_line():
    y, x = np.ogrid[-2:2:200j, -3:3:300j]
    z = np.exp( -x**2 - y**2)
    extent = [np.min(x), np.max(x), np.min(y), np.max(y)]
    plt.figure(figsize = (10, 4))
    plt.subplot(121)
    cs = plt.contour(z, 10, extent = extent)
    plt.clabel(cs)

    plt.subplot(122)
    # x和y必须是一维的
    plt.contourf(x.reshape(-1), y.reshape(-1), z, 20)
    plt.show()

if __name__ == "__main__":
    cont_line()