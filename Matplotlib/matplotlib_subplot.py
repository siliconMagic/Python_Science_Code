# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

def draw_subs():
    for idx, color in enumerate('rgbyck'):
        plt.subplot(321+idx, axisbg=color)

    plt.show()

def draw_multi_figure():
    # 创建图表1
    plt.figure(1, figsize=(8,5))
    # 创建图表2
    plt.figure(2, figsize=(8,5))
    # 在图表2中创建子图1
    sub_1 = plt.subplot(211)
    # 在图表2中创建子图2
    sub_2 = plt.subplot(212)
    # sca = set the current axes
    # sca(ax) set the current axes instance to *ax*

    x = np.linspace(0, 3, 100)
    for i in xrange(5):
        # 选择图表1
        plt.figure(1)
        plt.plot(x, np.exp(i*x/3))
        # 选择图表2中的子图1
        plt.sca(sub_1)
        plt.plot(x, np.sin(i*x))
        plt.sca(sub_2)
        plt.plot(x, np.cos(i*x))

    plt.show()

# 显示所有中文字体
from matplotlib.font_manager import fontManager
import os
import os.path

def show_all_chinese():
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(111)
    plt.subplots_adjust(0, 0, 1, 1, 0, 0)
    plt.xticks([])
    plt.yticks([])
    x, y = 0.05, 0.08
    # 找出路径中大于1M的中文字体
    fonts = [font.name for font in fontManager.ttflist if os.path.exists(font.fname) and os.stat(font.fname).st_size>1e6]
    # 将fonts放到集合当中进行排序
    font = set(fonts)
    print(len(fonts))
    dy = (1.0-y) / (len(fonts) / 4 + (len(fonts) % 4 != 0))
    for font in fonts:
        t = ax.text(x, y, u"中文字体", {'fontname':font, 'fontsize':14}, transform=ax.transAxes)
        ax.text(x, y - dy / 2, font, transform=ax.transAxes)
        x += 0.25
        if x >= 1.0:
            y += dy
            x = 0.05
    plt.show()

def show_all_ch():
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(111)
    plt.subplots_adjust(0, 0, 1, 1, 0, 0)
    plt.xticks([])
    plt.yticks([])
    x, y = 0.05, 0.08
    fonts = [font.name for font in fontManager.ttflist if
             os.path.exists(font.fname) and os.stat(font.fname).st_size > 1e6]
    font = set(fonts)
    dy = (1.0 - y) / (len(fonts) / 4 + (len(fonts) % 4 != 0))
    for font in fonts:
        t = ax.text(x, y, u"中文字体", {'fontname': font, 'fontsize': 14}, transform=ax.transAxes)
        ax.text(x, y - dy / 2, font, transform=ax.transAxes)
        x += 0.25
        if x >= 1.0:
            y += dy
            x = 0.05
    plt.show()

if __name__ == "__main__":
    # draw_subs()
    # draw_multi_figure()
    show_all_chinese()
    # show_all_ch()









