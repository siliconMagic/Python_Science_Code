# coding:utf-8

from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np

'''
matplotlib只搜索TTF字体文件,需要TTC字体文件,通过创建字体文件的FontProperties对象,并对此使用指定图表中的各种字体文字
'''

def font_manager():
    # plt.rcParams["font.family"] = "SimHei"
    # 使用ttc字体对象
    font = FontProperties(r'c:\windows\fonts\simsun.ttc', size=14)
    t = np.linspace(0, 10, 100)
    y = np.sin(t)
    plt.plot(t, y)
    plt.xlabel(u"Time", fontproperties = font)
    plt.ylabel(u"Ap", fontproperties = font)
    plt.title(u"Sin Wave", fontproperties = font)
    plt.show()

if __name__ == "__main__":
    font_manager()