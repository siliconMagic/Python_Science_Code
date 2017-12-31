# coding:utf-8
"""
@Function: 坐标变换和注释

@author:Minux
@date:2017-12-18
"""

import numpy as np
import matplotlib.pyplot as plt

'''
处理中文图例的问题,中文和负号
'''
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def func_1(x):
    '''

    :param x:x的值
    :return:直线方程
    '''
    return 0.6 * x + 0.3

def func_2(x):
    '''

    :param x:x的值
    :return:二次曲线方程
    '''
    return 0.4*x*x + 0.1*x + 0.2

def find_curve_intersects(x, y1, y2):
    d = y1 - y2
    index = np.where(d[:-1] * d[1:]<=0)[0]
    x1, x2 = x[index], x[index+1]
    d1, d2 = d[index], d[index+1]
    return -d1 * (x2 - x1)/(d2 - d1) + x1

from matplotlib import transforms

def plot_intersect():
    x = np.linspace(-3, 3, 100)
    f1 = func_1(x)
    f2 = func_2(x)
    plt.figure(figsize=(8, 4))
    plt.plot(x, f1)
    plt.plot(x, f2)

    x1, x2 = find_curve_intersects(x, f1, f2)
    print(x1, x2)
    plt.plot(x1, func_1(x1), 'o')
    plt.plot(x2, func_2(x2), 'o')

    # 对f1 > f2的区域填充为green
    plt.fill_between(x, f1, f2, where=f1 > f2, facecolor = 'green', alpha=0.5)

    # 对坐标轴进行变换处理，对f1 > f2所在的矩形进行染色
    ax = plt.gca()
    trans = transforms.blended_transform_factory(ax.transData, ax.transAxes)
    '''
    程序使用blended_transform_factory()创建混合坐标系,他的两个参数坐标变换对象，从第一个参数获得X轴坐标变换，
    第二参数获得Y的坐标变换
    '''
    plt.fill_between([x1, x2], 0, 1, transform = trans, alpha=0.2)

    # 绘制右上边的标题
    a = plt.text(0.05, 0.95, u"直线和二次曲线的交点",
                 transform = ax.transAxes,
                 verticalalignment = "top",
                 fontsize = 18,
                 bbox = {"facecolor":"red", "alpha":0.4, "pad":10}
                 )


    # 箭头图例的表示
    arrow = {"arrowstyle":"fancy,tail_width=0.6",
             "facecolor":"gray",
             "connectionstyle":"arc3,rad=-0.3"}

    plt.annotate(u"交点",
                 xy = (x1, func_1(x1)), xycoords = "data",
                 xytext=(0.05, 0.5), textcoords = "axes fraction",
                 arrowprops = arrow)

    plt.annotate(u"交点",
                 xy = (x2, func_2(x2)), xycoords = "data",
                 xytext=(0.05, 0.5), textcoords = "axes fraction",
                 arrowprops = arrow)

    xm = (x1 + x2)/2
    ym = (func_1(xm) - func_2(xm))/2+func_2(xm)
    o = plt.annotate(u"直线大于曲线区域",
                     xy = (xm, ym), xycoords = "data",
                     xytext = (30, -30), textcoords = "offset points",
                     fontsize = 16,
                     arrowprops = {"arrowstyle":"->"},
                     bbox = {"boxstyle":"round", "facecolor":(1.0, 0.7, 0.7), "edgecolor":"none"}
    )

    plt.show()





if __name__ == '__main__':
    plot_intersect()