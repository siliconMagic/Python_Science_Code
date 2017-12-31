# coding:utf-8

"""
@Function:
绘制中国人口的柱状图

@author: Minxu
@date: 2017-12-19
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False

def china_population():
    pop_data = np.loadtxt(r'./data/china_population.txt')
    # width表示绘制柱子的宽度
    width = (pop_data[1, 0] - pop_data[0, 0]) * 0.4
    fig = plt.figure(figsize = (8, 4))
    plt.bar(pop_data[:,0] - width, pop_data[:,1]/1e7, width, color="b", label = u"男")
    plt.bar(pop_data[:,0], pop_data[:,2]/1e7, width, color = "r", label = u"女")
    plt.xlim(-width, 100)
    plt.xlabel(u"年龄")
    plt.ylabel(u"人口(千万)")
    plt.legend()

    plt.show()



if __name__ == "__main__":
    china_population()