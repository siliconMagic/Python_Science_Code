# coding:utf-8

"""
@Function:
使用坐标轴变换绘制一个带有阴影效果的曲线

@author:Minux
@date:2017-12-19
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms

# 设置解决负号问题
plt.rcParams['axes.unicode_minus'] = False

def shadow_curve():
    x = np.arange(0., 2., 0.01)
    y = np.sin(2 * np.pi * x)

    # 设置阴影的条数
    N = 7
    for i in xrange(N, 0 , -1):
        # 向X轴偏移i单位，向Y轴偏移i单位
        offset = transforms.ScaledTranslation(i, -i, transforms.IdentityTransform())
        shadow_trans = plt.gca().transData + offset
        # shadow_trans = plt.gca().transAxes + offset
        # 将shadow_trans参数传给transform
        plt.plot(x, y, lw = 4, color = "black", transform = shadow_trans, alpha = (N-i)/2.0/N)

    plt.plot(x, y, lw = 4, color = "black")
    plt.ylim((-1.5, 1.5))
    plt.show()

if __name__ == "__main__":
    shadow_curve()