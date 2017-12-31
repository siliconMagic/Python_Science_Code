# coding:utf-8

"""
@Function:
在极坐标系中绘制图像

@author: Minxu
@date: 2017-12-19
"""

import numpy as np
import matplotlib.pyplot as plt

def polar_axis():
    theta = np.arange(0, 2 * np.pi, 0.02)
    plt.subplot(121, polar = True)
    plt.plot(theta, 1.6 * np.ones_like(theta), lw = 2)
    plt.plot(3 * theta, theta/3, '--', lw = 2)

    plt.plot(theta, 1.4 * np.cos(5 * theta), '--', color = 'green', lw = 2)
    plt.plot(theta, 1.8 * np.cos(4 * theta), lw = 2)

    # 设置同心圆栅格的大小和文字标准的角度
    plt.rgrids(np.arange(0.5, 2, 0.5), angle = 45)

    # 设置放射线栅格的角度
    plt.thetagrids([0, 45])

    plt.show()

if __name__ == "__main__":
    polar_axis()