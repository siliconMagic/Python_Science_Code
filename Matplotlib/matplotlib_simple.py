# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

# 将图像保存到StringIO中，可以得到一个表示图像的字符串
from StringIO import StringIO

def mat_simple():
    x = np.linspace(0, 10, 1000)
    y = np.sin(x)
    z = np.cos(x**2)
    # dpi参数可以指定分辨率
    plt.figure(figsize=(8,4), dpi = 80)

    # 在label中有$符号，会使用Latex内嵌引擎 linewidth可以使用缩写lw
    plt.plot(x, y, label="$sin(x)$", color="red", linewidth=2)
    # b--表示线型为蓝色虚线
    plt.plot(x, z, "b-.", label="$cos(x^2)$")

    plt.xlabel("Time(S)")
    plt.ylabel("Volt")
    plt.title("PyPlot First Example")
    plt.ylim(-1.2, 1.2)
    plt.legend()

    # 保存图像操作，dpi为120*8
    # plt.savefig("sin_cos(x)", dpi=120)
    buf = StringIO()
    plt.savefig(buf, fmt="png")
    # plt.show()
    # 在IPython中有wthread参数时，不会进行阻塞程序
    # print("Are youn waiting...?")
    print(buf.getvalue()[:20])

if __name__ == "__main__":
    mat_simple()