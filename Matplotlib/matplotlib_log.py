# coding:utf-8

"""
@Function:
用4种不同的坐标系绘制低通滤波器的频率响应,
存在latex字体问题

@author: Minxu
@date: 2017-12-19
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["axes.unicode_minus"] = False

def four_diff_filter():
    w = np.linspace(0.1, 1000, 1000)
    p = np.abs(1/(1+0.1j*w))

    plt.subplot(221)
    plt.plot(w, p, lw = 2)
    plt.ylim(0, 1.5)

    plt.subplot(222)
    plt.semilogx(w, p, lw = 2)
    plt.ylim(0, 1.5)

    plt.subplot(223)
    plt.semilogy(w, p, lw = 2)
    plt.ylim(0, 1.5)

    plt.subplot(224)
    plt.loglog(w, p, lw = 2)
    plt.ylim(0, 1.5)


    plt.show()

if __name__ == "__main__":
    four_diff_filter()