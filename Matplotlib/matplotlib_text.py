# coding:utf-8

"""
@Function:
在数据坐标系，子图坐标系和图表坐标系中添加文字

@author:Minux
@date:2017-12-19
"""

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["axes.unicode_minus"] = False

def text_coor():
    x = np.linspace(-1, 1, 10)
    y = np.cos(x) + x**2 + 1

    fig = plt.figure(figsize=(8, 4))
    ax = plt.subplot(111)

    plt.plot(x, y)

    for i, (_x, _y) in enumerate(zip(x, y)):
        plt.text(_x, _y, str(i), color = "red", fontsize=i+10)

    # 在子图中绘制文字
    plt.text(0.5, 0.8, u"子图坐标系中的文字", color="blue", ha="center", transform = ax.transAxes)

    # 在坐标系中绘制文字
    plt.figtext(0.1, 0.92, u"图表坐标系中的文字", color = "green")

    plt.show()

if __name__ == "__main__":
    text_coor()