# coding:utf-8

import matplotlib.pyplot as pl
from matplotlib.ticker import MultipleLocator, FuncFormatter
import numpy as np

def pi_formatter(x, pos):
    '''

    :param x:
    :param pos:
    :return:
    '''
    m = np.round(x / (np.pi/4))
    n = 4
    while m!=0 and m%2==0: m, n = m//2, n//2
    if m == 0:
        return "0"
    if m == 1 and n == 1:
        return "$\pi$"
    if n == 1:
        return r"$%d \pi$" %m
    if m == 1:
        return r"$\frac{\pi}{%d}$" %n
    return r"$\frac{%d \pi}{%d}$" %(m,n)

def main():
    x = np.arange(0, 4*np.pi, 0.01)
    y = np.sin(x)
    pl.figure(figsize = (8, 4))
    pl.plot(x, y)
    ax = pl.gca()
    pl.ylim(-1.5, 1.5)
    pl.xlim(0, np.max(x))
    pl.subplots_adjust(bottom = 0.15)
    # 开启网格
    pl.grid()
    # 主刻度为pi/4
    ax.xaxis.set_major_locator(MultipleLocator(np.pi/4))
    # 主刻度文本,传入回调函数
    ax.xaxis.set_major_formatter(FuncFormatter(pi_formatter))
    # 副刻度pi/20
    ax.xaxis.set_minor_locator(MultipleLocator(np.pi/20))

    # 设置刻度文本大小
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(16)
    pl.show()



if __name__ == '__main__':
    main()