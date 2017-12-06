# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

def Line_2D():
    x = np.arange(-5, 5, 0.1)
    line = plt.plot(x, x*x)[0] # plot返回一个Line_2D列表
    # 使用set_*设置属性值,使用set_antialiased(False)来关闭抗锯齿功能
    line.set_antialiased(False)

    # 同时绘制正玄和余弦曲线
    lines = plt.plot(x, np.sin(x), x, np.cos(x))
    # 调用setp()同时配置多个对象的属性
    plt.setp(lines, color="r", lw=2.0)
    plt.ylim(-2,2)
    plt.xlim(-5,5)
    plt.xlabel("$x$")
    plt.ylabel("$f(x)$")
    plt.title("$antiased$")

    # gcf()返回当前图表 gca()返回当前子图
    f = plt.gcf()
    print(plt.getp(f))
    plt.show()

if __name__ == "__main__":
    Line_2D()