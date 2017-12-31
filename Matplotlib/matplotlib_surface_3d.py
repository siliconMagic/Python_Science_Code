# coding:utf-8
"""
@Function:
使用contour,contourf
使用matplotlib绘制三维曲面

@author: Minux
@date: 2017-12-21
"""
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

plt.rcParams["axes.unicode_minus"] = False

def pic_3d():
    # x和y均为二维数组
    x, y = np.mgrid[-2:2:20j, -2:2:20j]
    z = x * np.exp( -x**2 - y**2)

    ax = plt.subplot(111, projection = '3d')
    ax.plot_surface(x, y, z, rstride=2, cstride = 1, cmap=plt.cm.Blues_r)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()

if __name__ == "__main__":
    pic_3d()