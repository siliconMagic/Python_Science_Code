# coding:utf-8

import matplotlib.pyplot as plt

def draw_circle_line():
    fig = plt.figure()
    # 参数说明[left, bottom, width, height]
    ax = fig.add_axes([0.15, 0.1, 0.7, 0.3])
    # 返回一个Line2D对象
    line = ax.plot([1, 2, 3], [1, 2, 1])
    # 查看对象属性
    # ax.lines包括所有曲线的列表
    print(ax.lines)
    print(line[0])
    # ax.plot()

    # 设置相关属性
    ax.set_xlabel("time")
    plt.show()

def set_patch_object():
    fig = plt.figure()
    fig.show()
    # 将背景颜色设置为绿色
    fig.patch.set_color("g")
    fig.canvas.draw()
    plt.show()

def set_alpha_attr():
    fig = plt.figure()
    line = plt.plot([1, 2, 3, 2, 2, 1.5, 1], lw = 4)[0]
    # line.set_alpha(0.5)
    # 可以使用set一次设置多个属性
    line.set(alpha = 0.5, zorder = 2)
    plt.xlabel("time")
    plt.ylabel("value")
    plt.show()
    # 使用getp()函数可以得到Atrist对象所有属性名及对应值
    plt.getp(fig.patch)

def figure_plt():
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_axes([0.1, 0.1, 0.7, 0.3])
    # 删除子图操作
    '''
    fig.delaxes(ax2)
    '''
    # 使用for循环对axes属性中每个元素进行操作
    for ax in fig.axes:
        # 所有子图进行栅格显示
        ax.grid(True)
    plt.show()

from matplotlib.lines import Line2D
import os
def pic_line():
    fig = plt.figure()
    line1 = Line2D([0, 1],[0, 1], transform = fig.transFigure, figure = fig, color = "r")
    line2 = Line2D([0, 1],[1, 0], transform = fig.transFigure, figure = fig, color = "g")
    fig.lines.extend([line1, line2])
    # 非阻塞式的情况
    # fig.show()
    # os.system("PAUSE")
    plt.show()

import numpy as np
def patch_obj():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    n, bins, rects = ax.hist(np.random.randn(1000), 50, facecolor="blue")
    plt.show()

def patch_axes_trans():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    rect = plt.Rectangle((1,1), width = 5, height=12)
    ax.add_patch(rect)
    # 自动调整X-Y轴的显示范围
    print(ax.get_xlim())
    # print(ax.dataLim._get_bounds())  protected method
    # 适应rect的大小
    ax.autoscale_view()
    print(ax.get_xlim())
    plt.show()

def draw_scatter():
    np.random.seed()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # t = ax.scatter(np.random.rand(20), np.random.rand(20))
    t = ax.scatter(np.random.randn(5), np.random.randn(5))
    fig.show()
    plt.show()
    # 获得散列点数
    print(t.get_sizes())

def axis_container():
    # 获取图像的刻度信息
    plt.plot([1, 2, 3],[4, 5, 6])
    axis = plt.gca().xaxis
    # 获取刻度位置列表
    print(axis.get_ticklocs())
    # 获取刻度标签列表
    # print(axis.get_ticklabels())
    # 获取刻度标签中的文字
    print([x.get_text() for x in axis.get_ticklabels()])
    '''
    # 对标签刻度及文本进行设置
    for label in axis.get_ticklabels():
        label.set_color("red")
        label.set_rotation(45)
        label.set_fontsize(16)

    for line in axis.get_ticklines():
        line.set_color("green")
        line.set_markersize(25)
        line.set_markeredgewidth(3)
    '''
    # 等效操作
    plt.xticks(fontsize=16, color="red", rotation=45)
    plt.show()

def main():
    # set_patch_object()
    # set_alpha_attr()
    # figure_plt()
    # pic_line()
    # patch_obj()
    # atch_axes_trans()
    # draw_scatter()
    axis_container()

if __name__ == '__main__':
    main()
